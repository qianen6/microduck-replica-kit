#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
if [ "$#" -ne 1 ]; then printf '%s\n' 'Usage: ROLLBACK.sh TARGET_README'; exit 2; fi
cp -- "$ROOT/proof/README.original.md" "$1"
cmp --silent -- "$ROOT/proof/README.original.md" "$1"
printf '%s\n' 'ROLLBACK_COPY PASS readme=PRE_R9 hash=MATCH'
