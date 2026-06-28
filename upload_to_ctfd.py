#!/usr/bin/env python3
"""
CTFd 上架腳本 — 將此資料夾下所有 challenge.yml 上傳到 CTFd

使用方式：
  python3 easy/upload_to_ctfd.py
  python3 medium/upload_to_ctfd.py
  python3 hard/upload_to_ctfd.py

設定：
  修改下方 HOST 和 TOKEN，或透過環境變數傳入：
    CTFD_HOST=https://... CTFD_TOKEN=ctfd_... python3 ../upload_to_ctfd.py
"""

import os
import sys
import json
import time
import mimetypes
from pathlib import Path

import yaml
import requests

# ─────────────────────────────────────────────────────────────────────────────
# ★ 請填入以下設定
# ─────────────────────────────────────────────────────────────────────────────

HOST     = os.environ.get('CTFD_HOST',     'https://YOUR_CTFD_HOST')  # CTFd 網址
TOKEN    = os.environ.get('CTFD_TOKEN',    'ctfd_YOUR_TOKEN_HERE')    # Admin API token

# Web 題 connection_info 裡 {{WEB_HOST}} 會被換成這個
WEB_HOST = os.environ.get('CTFD_WEB_HOST', 'YOUR_WEB_HOST')           # 例: chal.myctf.com

# nc/pwn 題 connection_info 裡 {{NC_HOST}} 會被換成這個
NC_HOST  = os.environ.get('CTFD_NC_HOST',  'YOUR_NC_HOST')            # 例: 1.2.3.4 或 nc.myctf.com

# 上傳完後是否立刻設為 visible（否則保持 hidden 讓你先審閱）
PUBLISH = False

# 同一題若已存在，是否更新（flag / 描述 / 分數）
UPDATE_EXISTING = True

# ─────────────────────────────────────────────────────────────────────────────

HOST = HOST.rstrip('/')
HEADERS = {'Authorization': f'Token {TOKEN}', 'Content-Type': 'application/json'}
WORK_DIR = Path(__file__).parent   # 腳本所在目錄（easy/ medium/ hard/）


def _fix_conn(conn) -> str | None:
    """替換 connection_info 的佔位符。"""
    if not conn:
        return None
    s = str(conn)
    s = s.replace('{{WEB_HOST}}', WEB_HOST)
    s = s.replace('{{NC_HOST}}',  NC_HOST)
    return s or None


def api(method: str, path: str, **kwargs):
    url = f'{HOST}/api/v1{path}'
    headers = HEADERS.copy()
    if 'files' in kwargs:
        # multipart upload — remove Content-Type so requests sets boundary
        headers = {'Authorization': f'Token {TOKEN}'}
    resp = getattr(requests, method)(url, headers=headers, **kwargs)
    try:
        data = resp.json()
    except Exception:
        resp.raise_for_status()
        return {}
    if not data.get('success'):
        raise RuntimeError(f'API error {path}: {data}')
    return data.get('data', data)


def get_existing_challenges() -> dict[str, int]:
    """回傳 {challenge_name: id} 所有已存在的題目"""
    result = {}
    page = 1
    while True:
        data = api('get', f'/challenges?page={page}&per_page=500&view=admin')
        items = data if isinstance(data, list) else []
        if not items:
            break
        for ch in items:
            result[ch['name']] = ch['id']
        if len(items) < 500:
            break
        page += 1
    return result


def upload_files(challenge_id: int, challenge_yml: Path, file_paths: list[str]):
    """上傳 challenge.yml 旁的 dist/ 檔案"""
    base = challenge_yml.parent
    uploaded = []
    for rel in file_paths:
        fpath = base / rel
        if not fpath.exists():
            print(f'      [WARN] 找不到附件: {fpath}')
            continue
        mime = mimetypes.guess_type(str(fpath))[0] or 'application/octet-stream'
        with open(fpath, 'rb') as f:
            result = api('post', '/files', files={
                'file': (fpath.name, f, mime),
            }, data={
                'challenge_id': challenge_id,
                'type': 'challenge',
            })
        uploaded.append(fpath.name)
    return uploaded


def delete_flags(challenge_id: int):
    flags = api('get', f'/flags?challenge_id={challenge_id}')
    if isinstance(flags, list):
        for fl in flags:
            api('delete', f'/flags/{fl["id"]}')


def add_flags(challenge_id: int, flags: list):
    for flag in flags:
        api('post', '/flags', json={
            'challenge_id': challenge_id,
            'content': str(flag),
            'type': 'static',
            'data': '',
        })


def sync_tags(challenge_id: int, tags: list):
    # Delete existing
    existing = api('get', f'/tags?challenge_id={challenge_id}')
    if isinstance(existing, list):
        for t in existing:
            api('delete', f'/tags/{t["id"]}')
    # Add new
    for tag in tags:
        api('post', '/tags', json={
            'challenge_id': challenge_id,
            'value': str(tag),
        })


def process_challenge(yml_path: Path, existing: dict[str, int]) -> str:
    """Upload or update one challenge. Returns 'created' / 'updated' / 'skipped'."""
    try:
        ch = yaml.safe_load(yml_path.read_text(encoding='utf-8'))
    except Exception as e:
        print(f'    [ERROR] YAML parse: {e}')
        return 'error'

    name = str(ch.get('name') or '').strip()
    if not name:
        print(f'    [SKIP] 沒有 name: {yml_path}')
        return 'skipped'

    payload = {
        'name':            name,
        'description':     str(ch.get('description') or ''),
        'value':           int(ch.get('value') or 100),
        'category':        str(ch.get('category') or ''),
        'type':            str(ch.get('type') or 'standard'),
        'state':           'visible' if PUBLISH else 'hidden',
        'connection_info': _fix_conn(ch.get('connection_info')),
    }

    flags = ch.get('flags') or []
    tags  = ch.get('tags') or []
    files = ch.get('files') or []

    cid = existing.get(name)

    if cid is None:
        # ── CREATE ──────────────────────────────────────────────────────────
        result = api('post', '/challenges', json=payload)
        cid = result['id']
        add_flags(cid, flags)
        sync_tags(cid, tags)
        uploaded = upload_files(cid, yml_path, files)
        status = 'created'
    else:
        # ── UPDATE ──────────────────────────────────────────────────────────
        if not UPDATE_EXISTING:
            return 'skipped'
        api('patch', f'/challenges/{cid}', json=payload)
        # Re-sync flags
        delete_flags(cid)
        add_flags(cid, flags)
        sync_tags(cid, tags)
        # Note: files are NOT re-uploaded to avoid duplicates.
        # To re-upload files, delete them manually in CTFd admin first.
        uploaded = []
        status = 'updated'

    return status


def main():
    if 'YOUR_CTFD_HOST' in HOST or 'YOUR_TOKEN' in TOKEN or 'YOUR_WEB_HOST' in WEB_HOST or 'YOUR_NC_HOST' in NC_HOST:
        print('ERROR: 請先在腳本頂端填入 HOST、TOKEN、WEB_HOST、NC_HOST。')
        sys.exit(1)

    # Test connectivity
    try:
        me = api('get', '/users/me')
        print(f'已連線到 {HOST}（使用者: {me.get("name","?")}）')
    except Exception as e:
        print(f'ERROR: 無法連線到 CTFd — {e}')
        sys.exit(1)

    print(f'掃描目錄: {WORK_DIR}\n')

    yml_files = sorted(WORK_DIR.rglob('challenge.yml'))
    if not yml_files:
        print('找不到任何 challenge.yml，請確認執行目錄正確。')
        sys.exit(1)

    print(f'找到 {len(yml_files)} 個 challenge.yml，正在取得 CTFd 現有題目...')
    existing = get_existing_challenges()
    print(f'CTFd 目前已有 {len(existing)} 題\n')

    counts = {'created': 0, 'updated': 0, 'skipped': 0, 'error': 0}

    for i, yml_path in enumerate(yml_files, 1):
        rel = yml_path.relative_to(WORK_DIR)
        try:
            ch_name = yaml.safe_load(yml_path.read_text()).get('name', '?')
        except:
            ch_name = '?'

        print(f'[{i:3}/{len(yml_files)}] {ch_name}')
        print(f'        {rel}')

        status = process_challenge(yml_path, existing)
        counts[status] += 1

        marker = {'created': '✓ 新增', 'updated': '↺ 更新', 'skipped': '- 跳過', 'error': '✗ 錯誤'}
        print(f'        → {marker.get(status, status)}')

        # Polite rate limiting
        time.sleep(0.1)

    print('\n' + '─'*50)
    print(f'完成！新增 {counts["created"]} 題 / 更新 {counts["updated"]} 題 / 跳過 {counts["skipped"]} 題 / 錯誤 {counts["error"]} 題')
    if not PUBLISH:
        print('注意：題目狀態為 hidden，請至 CTFd 管理介面手動發布。')


if __name__ == '__main__':
    main()
