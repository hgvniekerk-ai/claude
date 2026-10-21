#!/usr/bin/env bash
# Stage this candidate build next to the canonical local workspace without touching it.
# Default target: ~/pe-brain-candidate. Your ~/pe-brain is never written by this script.
# Usage: tools/install.sh [target-dir]
set -euo pipefail
SRC="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${1:-$HOME/pe-brain-candidate}"
if [ "$(cd "$DEST" 2>/dev/null && pwd)" = "$(cd "$HOME/pe-brain" 2>/dev/null && pwd)" ]; then
  echo "Refusing to write into ~/pe-brain. It is canonical. Use the default target and merge with _system/local-integration.md." >&2
  exit 1
fi
mkdir -p "$DEST"
cp -Rn "$SRC/." "$DEST/"
echo "Candidate staged at $DEST (existing files there were kept)."
echo "Next: open Claude Code in ~/pe-brain and paste the kickoff prompt from $DEST/_system/local-integration.md"
