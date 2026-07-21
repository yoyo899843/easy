#!/usr/bin/env python3
"""
Scan every web challenge's challenge.yml under this platform and generate a
cloudflared config.yml ingress list from it.

Only challenges whose connection_info already uses the subdomain form
(http://<slug>.{{WEB_HOST}}) are picked up — that's the convention this
platform's challenge.yml files use for web challenges routed through
cloudflared. Each ingress rule points at http://<ip>:<port>, so it works
whether cloudflared is running with network_mode: host (ip = 127.0.0.1) or
on a bridge network reaching the host by its real address.

Cloudflare Tunnel only routes a single subdomain level off the zone (e.g.
<anything>.yoyo899843.work), not <anything>.<platform>.yoyo899843.work — so
the platform (easy/medium/hard) is folded into the hostname itself as a
suffix: <slug>-<platform>.<domain>.

Also always emits two extra ingress rules for the platform's own admin
services: ctfd-<platform>.<domain> -> CTFd (port 8000 by default, override
with --ctfd-port / CTFD_PORT) and kuma-<platform>.<domain> -> Uptime Kuma
(fixed at port 8001).

Deployment host varies per machine, so --domain/--ip/--platform/--tunnel-id
can come from a .env file (WEB_HOST, DOMAIN, PLATFORM, TUNNEL_ID) next to
this script instead of being retyped every time — see .env.example.
Precedence: CLI flag > real env var > .env file > interactive prompt (domain/
ip only; tunnel-id falls back to the <TUNNEL_ID> placeholder instead).

Usage:
    python3 cloudflared_conf_generator.py
    python3 cloudflared_conf_generator.py --domain yoyo899843.work --ip 127.0.0.1
    python3 cloudflared_conf_generator.py --domain example.com --platform medium --ip 127.0.0.1
    python3 cloudflared_conf_generator.py --root . --out config.yml

Any flag left out is prompted for interactively. Cross-checks each
challenge's declared port against its own docker-compose.yml and warns
(doesn't block) about anything that doesn't line up, missing infra, or
duplicate ports — the same class of bug this repo has hit before.
"""
import argparse
import glob
import os
import re


def load_dotenv(path=".env"):
    """Populate os.environ from a simple KEY=VALUE .env file, without
    overriding variables the real environment already set."""
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip().strip("'\""))


def scan_web_challenges(root):
    """Find every challenge.yml with a subdomain-style HTTP connection_info,
    a declared port, and whether it actually has Docker infra."""
    pattern = re.compile(r"^http://([a-zA-Z0-9_-]+)\.\{\{WEB_HOST\}\}/?$")
    out = []
    skipped = []
    for path in sorted(glob.glob(os.path.join(root, "**", "challenge.yml"), recursive=True)):
        with open(path, encoding="utf-8") as f:
            text = f.read()
        conn_m = re.search(r"^connection_info:\s*(.*)$", text, re.M)
        conn = conn_m.group(1).strip().strip("'\"") if conn_m else ""
        m = pattern.match(conn)
        if not m:
            continue

        port_m = re.search(r"^\s*port:\s*(\d+)", text, re.M)
        chal_dir = os.path.dirname(path)
        has_compose = bool(glob.glob(os.path.join(chal_dir, "build", "**", "docker-compose.yml"), recursive=True))

        if not port_m or not has_compose:
            skipped.append((path, conn, has_compose, bool(port_m)))
            continue

        declared_port = int(port_m.group(1))
        out.append(dict(slug=m.group(1), port=declared_port, dir=chal_dir, challenge_yml=path))
    return out, skipped


def find_compose_ports(chal_dir):
    """Collect the actual host-side port(s) bound in this challenge's own
    docker-compose.yml(s), so the caller can check its declared port is
    among them."""
    real_ports = set()
    for compose_path in glob.glob(os.path.join(chal_dir, "build", "**", "docker-compose.yml"), recursive=True):
        with open(compose_path, encoding="utf-8", errors="ignore") as f:
            text = f.read()
        for match in re.finditer(r"(\d{4,5}):\d+", text):
            real_ports.add(int(match.group(1)))
    return real_ports


def generate_config(challenges, domain, platform, ip, tunnel_id, ctfd_port, kuma_port):
    lines = [
        f"tunnel: {tunnel_id}",
        f"credentials-file: /etc/cloudflared/{tunnel_id}.json",
        "",
        "ingress:",
        f"  - hostname: ctfd-{platform}.{domain}",
        f"    service: http://{ip}:{ctfd_port}",
        f"  - hostname: kuma-{platform}.{domain}",
        f"    service: http://{ip}:{kuma_port}",
    ]
    for c in sorted(challenges, key=lambda c: c["port"]):
        lines.append(f"  - hostname: {c['slug']}-{platform}.{domain}")
        lines.append(f"    service: http://{ip}:{c['port']}")
    lines.append("  - service: http_status:404")
    lines.append("")
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=".", help="challenge repo root to scan (default: current directory)")
    p.add_argument("--env-file", default=".env", help="path to .env file to load (default: .env)")
    p.add_argument("--domain", default=None, help="zone domain, e.g. yoyo899843.work (env: DOMAIN, else prompted)")
    p.add_argument("--platform", default=None,
                    help="platform label appended to each hostname as <slug>-<platform>.<domain>, "
                         "e.g. easy/medium/hard (env: PLATFORM, else basename of --root)")
    p.add_argument("--ip", default=None, help="host address the ingress service targets should point at, e.g. 127.0.0.1 (env: WEB_HOST, else prompted)")
    p.add_argument("--tunnel-id", default=None, help="cloudflared tunnel UUID (env: TUNNEL_ID, else left as <TUNNEL_ID> placeholder)")
    p.add_argument("--ctfd-port", type=int, default=None, help="port CTFd listens on this host (env: CTFD_PORT, default: 8000)")
    p.add_argument("--out", default="config.yml", help="output file (default: config.yml)")
    args = p.parse_args()

    load_dotenv(args.env_file)

    domain = args.domain or os.environ.get("DOMAIN") or input("Enter your domain name: ").strip()
    ip = args.ip or os.environ.get("WEB_HOST") or input("Enter your host IP: ").strip()
    tunnel_id = args.tunnel_id or os.environ.get("TUNNEL_ID") or "<TUNNEL_ID>"
    ctfd_port = args.ctfd_port or int(os.environ.get("CTFD_PORT", 8000))
    kuma_port = 8001  # Uptime Kuma's port on this host — fixed, not configurable

    root = os.path.abspath(args.root)
    platform = args.platform or os.environ.get("PLATFORM") or os.path.basename(root.rstrip("/")) or "ctf"
    challenges, skipped = scan_web_challenges(root)

    print(f"platform: {platform} (hostnames will be <slug>-{platform}.{domain})")
    print(f"  ctfd-{platform}.{domain} -> http://{ip}:{ctfd_port}")
    print(f"  kuma-{platform}.{domain} -> http://{ip}:{kuma_port}")
    print(f"scanned challenge.yml under {root}")
    print(f"{len(challenges)} web challenges with a subdomain connection_info + real infra -> will include\n")

    # cross-check declared port vs what's actually bound in each challenge's
    # own docker-compose.yml, and flag duplicate ports across challenges
    warnings = []
    port_owners = {}
    for c in challenges:
        real_ports = find_compose_ports(c["dir"])
        if c["port"] not in real_ports:
            warnings.append(
                f"  - {c['slug']}: challenge.yml declares port {c['port']}, "
                f"but its docker-compose.yml only binds {sorted(real_ports) or 'nothing'}"
            )
        port_owners.setdefault(c["port"], []).append(c["slug"])

    dupes = {port: slugs for port, slugs in port_owners.items() if len(slugs) > 1}
    for port, slugs in dupes.items():
        warnings.append(f"  - port {port} is declared by more than one challenge: {', '.join(slugs)}")

    if warnings:
        print(f"{len(warnings)} warning(s) — generated anyway, but worth checking:")
        print("\n".join(warnings))
        print()

    if skipped:
        print(f"{len(skipped)} web-looking challenge(s) skipped (no port and/or no docker-compose.yml found):")
        for path, conn, has_compose, has_port in skipped:
            reason = []
            if not has_compose:
                reason.append("no compose")
            if not has_port:
                reason.append("no port")
            print(f"  - {os.path.dirname(path)}: {conn!r} ({', '.join(reason)})")
        print()

    config = generate_config(challenges, domain, platform, ip, tunnel_id, ctfd_port, kuma_port)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(config)

    print(f"wrote {args.out} ({len(challenges)} ingress rules + 1 catch-all)")
    print(f"\nNext step: cp {args.out} ~/.cloudflared/config.yml")


if __name__ == "__main__":
    main()
