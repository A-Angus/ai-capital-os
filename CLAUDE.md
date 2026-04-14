## Project: Liberty Equity Xchange

Stack: React (Lovable) · Supabase · Flask · GHL API V2 · Telegram Bot API

## Execution rules
- Work autonomously until the full task is complete
- Never pause to ask questions — make reasonable decisions and document them inline
- Always read spec.md and docs/ before writing code
- Never mix frontend and backend in the same session
- When context hits 60-70% token usage, /clear and start a new task
- GHL location ID: ZS5wuDbXMdtD5ua94ZPo
- VPS IP: 206.189.71.176, SSH alias: vps
- Flask orchestrator: port 5005

## Decision defaults
- Missing env var → load from .env, add a TODO comment, continue
- Ambiguous field name → use snake_case matching Supabase schema
- Error on first attempt → retry up to 3 times, then report
- Unknown API endpoint → check docs/ folder first, then use most recent known version
