#!/usr/bin/env bash
# Stop all CTF containers for easy machine

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

make_proj() {
    echo "$1"         | tr '[:upper:]' '[:lower:]'         | sed 's|/docker-compose\.yml||'         | tr -cs 'a-z0-9' '-'         | sed 's/^-*//;s/-*$//'         | cut -c1-63
}

echo "[1/2] Stopping challenge containers..."
ERRORS=0

while IFS= read -r compose_file; do
    rel="${compose_file#./}"
    proj="$(make_proj "$rel")"
    echo "  -> $rel"
    if ! docker compose -p "$proj" -f "$compose_file" down; then
        echo "  [ERROR] Failed: $rel" >&2
        ERRORS=$((ERRORS + 1))
    fi
done < <(find . -name "docker-compose.yml"     -path "*/build/*"     ! -path "*/nginx_server/*"     ! -path "*/build/tomcat/*"     | sort)

echo ""
echo "[2/2] Stopping nginx server..."
docker compose -p "easy-nginx" -f nginx_server/docker-compose.yml down

echo ""
if [ "$ERRORS" -eq 0 ]; then
    echo "All services stopped."
else
    echo "Done with $ERRORS error(s). Check output above." >&2
    exit 1
fi
