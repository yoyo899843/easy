#!/usr/bin/env bash
# Startup script for easy CTF machine

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

LOG="$SCRIPT_DIR/log.txt"
exec > >(tee "$LOG") 2>&1
echo "=== $(date '+%Y-%m-%d %H:%M:%S') ==="

# Derive a unique Docker Compose project name from a relative path
# e.g. "BreakAll - Crypto/CBC/build" → "breakall-crypto-cbc-build"
make_proj() {
    echo "$1"         | tr '[:upper:]' '[:lower:]'         | sed 's|/docker-compose\.yml||'         | tr -cs 'a-z0-9' '-'         | sed 's/^-*//;s/-*$//'         | cut -c1-63
}

echo "[0/1] Cleaning up unused networks and ensuring ctf_chals_network exists..."
docker network prune -f
docker network inspect ctf_chals_network >/dev/null 2>&1 \
    || docker network create ctf_chals_network
echo ""

# NOTE: no reverse-proxy / cloudflared step here — this platform has never
# had cloudflared set up and nginx_server was removed. Add that step back
# once a routing layer exists.

echo "[1/1] Starting challenge containers..."
ERRORS=0

while IFS= read -r compose_file; do
    rel="${compose_file#./}"
    proj="$(make_proj "$rel")"
    echo "  -> $rel"
    if ! docker compose -p "$proj" -f "$compose_file" up -d --build; then
        echo "  [ERROR] Failed: $rel" >&2
        ERRORS=$((ERRORS + 1))
    fi
done < <(find . -name "docker-compose.yml" \
    -path "*/build/*" \
    ! -path "*/nginx_server/*" \
    ! -path "*/build/tomcat/*" \
    ! -path "*/my_challenge/build/forging_chunk/*" \
    ! -path "*/my_challenge/build/math_teacher/*" \
    ! -path "*/my_challenge/build/unlink/*" \
    ! -path "*/docker_MyfirstCTF_pwn/build/*/*.yml" \
    | sort)

echo ""
if [ "$ERRORS" -eq 0 ]; then
    echo "All services started successfully."
else
    echo "Done with $ERRORS error(s). Check output above." >&2
    exit 1
fi
