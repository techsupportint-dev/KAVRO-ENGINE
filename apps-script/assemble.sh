#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
cat parts/Code.gs.part* > Code.gs
cat parts/Portal.html.part* > Portal.html
echo "Wrote Code.gs ($(wc -c < Code.gs) bytes) and Portal.html ($(wc -c < Portal.html) bytes)"
