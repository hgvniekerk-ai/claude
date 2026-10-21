#!/usr/bin/env bash
# Link company skills from a read-only s3-agent-skills clone into this workspace.
# Creates symlinks only. Never copies, never writes inside the source repo.
# Usage: tools/link-s3-skills.sh [path-to-s3-agent-skills]   (default ~/s3-reference/s3-agent-skills)
set -euo pipefail
SRC="${1:-$HOME/s3-reference/s3-agent-skills}"
DEST="$(cd "$(dirname "$0")/.." && pwd)/.claude/skills"
if [ ! -d "$SRC" ]; then
  echo "Not found: $SRC. Clone it first (see _system/sources.md)." >&2
  exit 1
fi
mkdir -p "$DEST"
n=0
while IFS= read -r skill; do
  dir="$(dirname "$skill")"
  name="s3-$(basename "$dir")"
  if [ -e "$DEST/$name" ] && [ ! -L "$DEST/$name" ]; then
    echo "SKIP $name: a real folder exists there"
    continue
  fi
  ln -sfn "$dir" "$DEST/$name"
  echo "LINK $name -> $dir"
  n=$((n+1))
done < <(find "$SRC" -name SKILL.md -not -path '*/.git/*')
echo "$n skills linked. They are git-ignored (.claude/skills/s3-*). Restart Claude Code to load them."
