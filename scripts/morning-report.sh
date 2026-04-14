#!/usr/bin/env bash
# Morning Report — runs at 6:57 AM Pacific (1:57 PM UTC)
# Reads overnight output and generates Alex's morning briefing

set -euo pipefail

LOG_DIR="/home/lexbot/.local/share/lex/reports"
LOG_FILE="/home/lexbot/.local/share/lex/night-operator-output/daily/$(date +%Y-%m-%d)-morning.log"
mkdir -p "$LOG_DIR" "/home/lexbot/.local/share/lex/night-operator-output/daily"

exec >> "$LOG_FILE" 2>&1
echo "=== Morning Report started at $(date) ==="

cd /home/lexbot

claude -p --allowedTools "Read,Glob,Grep,Write,Bash(readonly),mcp__claude_ai_Gmail__gmail_search_messages,mcp__claude_ai_Gmail__gmail_read_message,mcp__claude_ai_Google_Calendar__gcal_list_events" \
  "You are Lex, the AI operator for Liberty Equity Xchange. It is $(date). Generate Alex's morning briefing.

Do these things:
1. Read /home/lexbot/.local/share/lex/reports/$(date +%Y-%m-%d)-overnight-report.md for what was done overnight
2. Read brain/deals/deals.md for pipeline status
3. Check Gmail for any new messages since yesterday that relate to active deals
4. Check today's calendar events
5. Read MEMORY.md for context on pending tasks

Write the morning briefing to /home/lexbot/.local/share/lex/reports/$(date +%Y-%m-%d)-morning-briefing.md

Format:
# Good Morning, Alex — $(date +%Y-%m-%d)

## Overnight Summary
[What Lex did overnight and key output]

## Pipeline Status
[Quick status on each active deal, flag anything stalled or needing attention]

## Inbox Highlights
[Any deal-related emails that came in overnight]

## Today's Calendar
[Events for today]

## Recommended Actions
[Top 3 things Alex should do today, ordered by revenue impact]

Rules:
- No hyphens ever
- Keep it scannable, not a wall of text
- Lead with what matters most"

echo "=== Morning Report finished at $(date) ==="
