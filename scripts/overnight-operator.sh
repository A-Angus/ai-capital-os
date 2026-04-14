#!/usr/bin/env bash
# Overnight Operator — runs at 2:03 AM Pacific (9:03 AM UTC)
# Executes the highest-leverage overnight task from goals.md

set -euo pipefail

LOG_DIR="/home/lexbot/.local/share/lex/night-operator-output/daily"
LOG_FILE="${LOG_DIR}/$(date +%Y-%m-%d)-overnight.log"
mkdir -p "$LOG_DIR"

exec >> "$LOG_FILE" 2>&1
echo "=== Overnight Operator started at $(date) ==="

cd /home/lexbot

claude -p --allowedTools "Read,Write,Glob,Grep,WebSearch,WebFetch,Bash(readonly)" \
  "You are Lex, the AI operator for Liberty Equity Xchange. It is $(date). Run the overnight operator task.

Read brain/goals.md for the overnight task priorities list. Pick the single highest-leverage task and execute it fully. Save output to the correct directory under /home/lexbot/.local/share/lex/ per the standard output locations in goals.md.

Rules:
- No hyphens in any written content
- Do not name specific lenders in any external-facing content
- Use the LEX brand voice: confident, credible, educational
- Read brain/deals/deals.md for current pipeline context
- Read MEMORY.md for relationship context
- File naming: YYYY_MM_DD format

After completing the task, write a summary to /home/lexbot/.local/share/lex/reports/$(date +%Y-%m-%d)-overnight-report.md in this format:
OPENCLAW OVERNIGHT REPORT — $(date +%Y-%m-%d)
Task completed: [what you did]
Output saved to: [file path]
Key finding or result: [1 to 2 sentences]
Recommended next action for Alex: [one clear next step]"

echo "=== Overnight Operator finished at $(date) ==="
