#!/bin/bash
# LEX AI Capital OS — fresh VPS restore script
set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
TARGET="/home/lexbot"

echo "Restoring LEX AI Capital OS to $TARGET..."

# Identity and context files
cp "$REPO_DIR/CLAUDE.md" "$TARGET/"
cp "$REPO_DIR/AGENTS.md" "$TARGET/"
cp "$REPO_DIR/MEMORY.md" "$TARGET/"
cp "$REPO_DIR/SOUL.md" "$TARGET/"
cp "$REPO_DIR/USER.md" "$TARGET/"
cp "$REPO_DIR/TOOLS.md" "$TARGET/"
cp "$REPO_DIR/HEARTBEAT.md" "$TARGET/"
cp "$REPO_DIR/IDENTITY.md" "$TARGET/"

# Brain
cp -r "$REPO_DIR/brain/." "$TARGET/brain/"

# Scripts
cp "$REPO_DIR/scripts/morning_briefing.py" "$TARGET/"
cp "$REPO_DIR/scripts/night_operator.py" "$TARGET/"
cp "$REPO_DIR/scripts/healthcheck.sh" "$TARGET/"
cp -r "$REPO_DIR/scripts/." "$TARGET/scripts/"

# Telegram bridge
cp "$REPO_DIR/bots/telegram-bridge/telegram_bridge.py" "$TARGET/telegram-bridge/"

echo "Restore complete."
echo "Remember to:"
echo "  1. Copy telegram-bridge-config.json from your secrets store"
echo "  2. Set up cron: crontab -e"
echo "  3. Restart openclaw: systemctl restart openclaw"
