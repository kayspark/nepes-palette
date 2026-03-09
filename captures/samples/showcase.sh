#!/usr/bin/env bash
# Nepes Colorscheme Showcase — Shell syntax highlighting demo

set -euo pipefail

# ── Variables & strings ────────────────────────────────────
HOSTNAME="$(hostname -s)"
VERSION="2.4.1"
TIMESTAMP=$(date +%Y-%m-%dT%H:%M:%S)
readonly LOG_DIR="/var/log/nepes"
declare -a SERVICES=("fdc-api" "fdc-extractor" "nginx" "postgres")

# ── Functions ──────────────────────────────────────────────
check_service() {
    local name="$1"
    local status

    if systemctl is-active --quiet "$name" 2>/dev/null; then
        status="running"
        echo "  [OK] $name is $status (pid: $(pgrep -f "$name" | head -1))"
        return 0
    else
        status="stopped"
        echo "  [FAIL] $name is $status" >&2
        return 1
    fi
}

get_disk_usage() {
    df -h / | awk 'NR==2 {printf "%s used of %s (%s)\n", $3, $2, $5}'
}

# ── Main logic ─────────────────────────────────────────────
echo "=== System Report: $HOSTNAME ==="
echo "Time: $TIMESTAMP"
echo "Disk: $(get_disk_usage)"
echo ""

PASS=0
FAIL=0

for svc in "${SERVICES[@]}"; do
    if check_service "$svc"; then
        ((PASS++))
    else
        ((FAIL++))
    fi
done

echo ""
echo "Summary: $PASS passed, $FAIL failed out of ${#SERVICES[@]} services"

# ── Heredoc ────────────────────────────────────────────────
cat <<EOF
{
    "host": "$HOSTNAME",
    "version": "$VERSION",
    "services_ok": $PASS,
    "services_fail": $FAIL
}
EOF

# ── Conditional exit ───────────────────────────────────────
if [[ $FAIL -gt 0 ]]; then
    echo "ERROR: $FAIL services are down" >&2
    exit 1
fi
