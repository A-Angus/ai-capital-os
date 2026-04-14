#!/bin/bash
# LEX AI Capital OS — brain sync to GitHub
set -e

REPO="/home/lexbot/ai-capital-os"
TIMESTAMP=$(date +"%Y-%m-%d %H:%M")

echo "[$TIMESTAMP] Syncing brain to GitHub..."

# Copy latest brain and identity files into repo
cp -r /home/lexbot/brain/. "$REPO/brain/"
cp /home/lexbot/MEMORY.md "$REPO/MEMORY.md"
cp /home/lexbot/CLAUDE.md "$REPO/CLAUDE.md"
cp /home/lexbot/AGENTS.md "$REPO/AGENTS.md"
cp /home/lexbot/SOUL.md "$REPO/SOUL.md"
cp /home/lexbot/USER.md "$REPO/USER.md"
cp /home/lexbot/TOOLS.md "$REPO/TOOLS.md"
cp /home/lexbot/HEARTBEAT.md "$REPO/HEARTBEAT.md"
cp /home/lexbot/IDENTITY.md "$REPO/IDENTITY.md"

# Commit and push
cd "$REPO"
git add -A
git diff --cached --quiet && echo "[$TIMESTAMP] Nothing changed. Skipping." && exit 0
git commit -m "sync: brain update $TIMESTAMP"
git push origin main

echo "[$TIMESTAMP] Done."
