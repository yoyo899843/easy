#!/usr/bin/env python3
"""
Register every CTF challenge that has real Docker infra as an Uptime Kuma monitor.

Run this ON the machine that hosts a given platform (easy / medium / hard) — it
assumes Uptime Kuma is running on the same host and auto-detects the host's own
IP unless --kuma-url is given. Requires: pip install uptime-kuma-api

Usage:
    # --web-host is the host's own IP (not the public domain) — HTTP monitors
    # check http://<web-host>:<challenge-port>/ directly, bypassing
    # nginx/cloudflared, so they reflect the backend's own health.
    python3 upload_to_uptime_kuma.py \
        --web-host 192.168.0.244 \
        --nc-host 192.168.0.244 \
        --username admin --password 'secret'

    # dry run first to see what would be created/updated, without touching Kuma:
    python3 upload_to_uptime_kuma.py --web-host 1.2.3.4 --nc-host 1.2.3.4 \
        --username admin --password 'secret' --dry-run

Safe to re-run: matches existing monitors by name and updates them in place
instead of creating duplicates.
"""
import argparse
import glob
import os
import re
import socket
import sys


def detect_local_ip():
    """Best-effort local IP detection (the address this host would use to
    reach the internet) — used to build the Kuma URL when --kuma-url is not given."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def scan_challenges(root):
    """Parse every challenge.yml under root into a flat list of dicts."""
    out = []
    for path in sorted(glob.glob(os.path.join(root, "**", "challenge.yml"), recursive=True)):
        text = read(path)
        name_m = re.search(r"^name:\s*(.+)$", text, re.M)
        cat_m = re.search(r"^category:\s*(.+)$", text, re.M)
        conn_m = re.search(r"^connection_info:\s*(.*)$", text, re.M)
        port_m = re.search(r"^\s*port:\s*(\d+)", text, re.M)
        chal_dir = os.path.dirname(path)
        has_compose = bool(glob.glob(os.path.join(chal_dir, "build", "**", "docker-compose.yml"), recursive=True))
        out.append(dict(
            dir=chal_dir,
            name=(name_m.group(1).strip().strip("'\"") if name_m else os.path.basename(chal_dir)),
            category=(cat_m.group(1).strip().strip("'\"") if cat_m else "(未分類)"),
            connection_info=(conn_m.group(1).strip().strip("'\"") if conn_m else ""),
            port=(int(port_m.group(1)) if port_m else None),
            has_compose=has_compose,
        ))
    return out


def build_targets(chals, web_host, nc_host):
    """Turn scanned challenges (with real infra) into Uptime Kuma monitor specs."""
    from uptime_kuma_api import MonitorType

    targets = []
    skipped = []
    for c in chals:
        if not c["has_compose"]:
            continue
        monitor_name = f"[{c['category']}] {c['name']}"
        conn = c["connection_info"]
        if conn.startswith("http://{{WEB_HOST}}/") and c["port"]:
            # monitor the container's port directly (ip:port) instead of going
            # through nginx/cloudflared — checks the backend itself is healthy,
            # independent of whether the public routing layer is up
            targets.append(dict(
                name=monitor_name,
                type=MonitorType.HTTP,
                url=f"http://{web_host}:{c['port']}/",
            ))
        elif conn.startswith("nc {{NC_HOST}}") and c["port"]:
            targets.append(dict(
                name=monitor_name,
                type=MonitorType.PORT,
                hostname=nc_host,
                port=c["port"],
            ))
        else:
            skipped.append((c["dir"], conn))
    return targets, skipped


def sync_to_kuma(kuma_url, username, password, group_name, targets, interval, dry_run):
    from uptime_kuma_api import UptimeKumaApi, MonitorType

    print(f"connecting to {kuma_url} ...")
    api = UptimeKumaApi(kuma_url)
    api.login(username, password)
    try:
        # uptime-kuma-api 1.2.1 (latest on PyPI) predates the server's
        # "monitor conditions" feature and never sends a `conditions` value
        # when creating a monitor, but newer Kuma servers added a NOT NULL
        # `conditions` column with no DB-level default -> SQLITE_CONSTRAINT.
        # Patch the low-level call to fill it in until the client catches up.
        orig_call = api._call

        def _call_with_conditions(event, data=None):
            if event == "add" and isinstance(data, dict) and "conditions" not in data:
                data = dict(data, conditions=[])
            return orig_call(event, data)

        api._call = _call_with_conditions

        existing = api.get_monitors()
        by_name = {m["name"]: m for m in existing}

        group = by_name.get(group_name)
        group_id = group["id"] if group else None
        if group_id is None:
            if dry_run:
                print(f"[dry-run] would create monitor group: {group_name}")
            else:
                res = api.add_monitor(type=MonitorType.GROUP, name=group_name)
                group_id = res["monitorID"]
                print(f"created monitor group '{group_name}' (id={group_id})")
        else:
            print(f"using existing monitor group '{group_name}' (id={group_id})")

        created, updated = 0, 0
        for t in targets:
            fields = dict(t)
            name = fields.pop("name")
            fields["parent"] = group_id
            fields["interval"] = interval

            existing_monitor = by_name.get(name)
            if existing_monitor:
                if dry_run:
                    print(f"[dry-run] would update: {name}")
                else:
                    api.edit_monitor(existing_monitor["id"], name=name, **fields)
                updated += 1
            else:
                if dry_run:
                    print(f"[dry-run] would create: {name}")
                else:
                    api.add_monitor(name=name, **fields)
                created += 1

        print(f"\ndone. created={created} updated={updated} total={created + updated}")
    finally:
        api.disconnect()


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=".", help="challenge repo root to scan (default: current directory)")
    p.add_argument("--platform", default=None,
                    help="label used in the monitor group name, e.g. easy/medium/hard "
                         "(default: basename of --root)")
    p.add_argument("--kuma-url", default=None,
                    help="Uptime Kuma base URL, e.g. http://1.2.3.4:3001 "
                         "(default: auto-detect this host's IP, port 3001)")
    p.add_argument("--username", required=True)
    p.add_argument("--password", required=True)
    p.add_argument("--web-host", required=True, help="real host/domain to substitute for {{WEB_HOST}}")
    p.add_argument("--nc-host", required=True, help="real host/domain to substitute for {{NC_HOST}}")
    p.add_argument("--interval", type=int, default=60, help="heartbeat interval in seconds (default: 60)")
    p.add_argument("--dry-run", action="store_true", help="print what would happen, don't touch Kuma")
    args = p.parse_args()

    root = os.path.abspath(args.root)
    platform = args.platform or os.path.basename(root.rstrip("/")) or "ctf"
    kuma_url = args.kuma_url or f"http://{detect_local_ip()}:3001"

    chals = scan_challenges(root)
    targets, skipped = build_targets(chals, args.web_host, args.nc_host)

    print(f"platform: {platform}")
    print(f"scanned {len(chals)} challenge.yml under {root}")
    print(f"{len(targets)} have real Docker infra and a recognizable connection_info -> will sync")
    if skipped:
        print(f"{len(skipped)} have infra but an unrecognized connection_info format, skipped:")
        for d, conn in skipped:
            print(f"  - {d}: {conn!r}")

    if not targets:
        print("nothing to sync.")
        return

    group_name = f"CTF - {platform}"
    sync_to_kuma(kuma_url, args.username, args.password, group_name, targets, args.interval, args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
