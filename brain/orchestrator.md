# lex-orchestrator.py — Single-Voice Routing

Runs on port 5005. Enforces: Alex talks to LexxBot only. Atlas and LexCapital never speak in Alex's chat.

## Routing matrix

| Source | Destination | Notes |
|--------|-------------|-------|
| Alex (Telegram) | LexxBot | Always. No exceptions. |
| Website / GHL webhook | LexCapital | Borrower intake |
| LexxBot dispatch | Atlas | Background task |
| Atlas reply | LexxBot | NEVER directly to Alex's chat |
| LexCapital qualified lead | LexxBot | Surfaces as LexxBot message |
| Atlas → Alex direct | REJECT | Hard rule |
| LexCapital → Alex direct | REJECT | Hard rule |
| External → Atlas direct | REJECT | Atlas only takes LexxBot dispatches |

## Single-voice enforcement

The orchestrator is the bouncer. Even if a malformed payload tries to send Atlas or LexCapital output to Alex's chat ID directly, the orchestrator drops it. Only LexxBot's process can write to Alex's Telegram.

## Auth checks before routing

1. Sender Telegram ID matches expected origin
2. Task `from` field matches actual sender process
3. `task_id` present on Atlas requests/replies
4. Reply destination always = LexxBot for any Alex-facing content

## Task tracking

```
tasks = {
  "<task_id>": {
    "created_at": <ts>,
    "from": "lexxbot",
    "to": "atlas",
    "status": "pending | accepted | in_progress | complete | failed",
    "alex_chat_id": "<>",
    "raw_request": "<>",
    "task_type": "<>"
  }
}
```

Timeouts:
- Atlas no-accept in 30s → LexxBot tells Alex "Atlas slow, retry?"
- Atlas accepted but no result in 10min → LexxBot pings Alex "still working on <type>, ETA?"

## Debug routing

`/trace` from Alex returns last task's full path:
```
[Alex msg] → LexxBot (parsed: arv_comps) → dispatch task abc123 → Atlas (accepted 0.4s, completed 8.2s, used arv-comp-analyzer skill) → reply to LexxBot → re-voiced for Alex
```

`/last` returns raw Atlas output of last task (for verification).

`/who` shows routing table for the next inferred task type.

## Logging
/var/log/lex-orchestrator/ — timestamp, from, to, task_type, status. No PII payloads in plaintext.

## Health endpoint
GET /health:
```json
{
  "lexxbot": "up",
  "atlas": "up",
  "lexcapital": "up",
  "active_tasks": 0,
  "stale_tasks": 0,
  "last_dispatch": "<ts>",
  "last_atlas_reply": "<ts>"
}
```

LexxBot calls this when Alex asks "are the bots up".
