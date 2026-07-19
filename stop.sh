#!/usr/bin/env bash
# Stop all CTF containers for easy machine

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

make_proj() {
    echo "$1"         | tr '[:upper:]' '[:lower:]'         | sed 's|/docker-compose\.yml||'         | tr -cs 'a-z0-9' '-'         | sed 's/^-*//;s/-*$//'         | cut -c1-63
}

echo "[1/1] Stopping challenge containers..."
ERRORS=0

while IFS= read -r compose_file; do
    rel="${compose_file#./}"
    proj="$(make_proj "$rel")"
    abs="$(cd "$(dirname "$compose_file")" && pwd)/docker-compose.yml"
    echo "  -> $rel"
    if ! docker compose -p "$proj" -f "$compose_file" down; then
        echo "  [ERROR] Failed: $rel" >&2
        ERRORS=$((ERRORS + 1))
    fi

    # safety net: containers started manually (e.g. `cd <dir> && docker
    # compose up` with no -p) get the default project name "build" — every
    # challenge's compose file lives in a directory literally named "build",
    # so that never matches this script's own unique project name above and
    # `down` silently leaves them running. Docker still tags every container
    # with the absolute path of the compose file that created it regardless
    # of project name, so use that to catch and remove any stragglers.
    ids=$(docker ps -aq --filter "label=com.docker.compose.project.config_files=$abs")
    if [ -n "$ids" ]; then
        echo "     (stopping stragglers started under a different project name)"
        docker stop $ids >/dev/null
        docker rm $ids >/dev/null
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
    echo "All services stopped."
else
    echo "Done with $ERRORS error(s). Check output above." >&2
    exit 1
fi
