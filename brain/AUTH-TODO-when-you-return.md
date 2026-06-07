# Account-level actions status

## 1. Gmail SEND scope  — STILL PENDING (only you can do this)
Gmail is draft-only. The follow-up scanner writes drafts to brain/drafts/ but
nothing sends them. To enable sending, re-authorize the Gmail connector with
SEND scope (connector settings for mr.alexangus@gmail.com). This is the last
unlock for end-to-end Follow-Up Automation.

## 2. GitHub auth on VPS  — DONE 2026-06-06
- gh authenticated as A-Angus (repo scope), both lexbot + hermes users.
- ROOT CAUSE of broken nightly sync found + fixed: ai-capital-os remote URL had
  a dead embedded token (ghp_fmg...) -> every 2am push failed. Stripped the
  token, set gh credential helper, pushed the backlog. Sync now clean.
- Note: the VPS /home/lexbot/CentralBrain is only a 15-file _SYSTEM/ subset, NOT
  the canonical vault (canonical lives on Mac/mini, 721K). Left untouched.
- Minor: the dead ghp_ token lived only in .git/config (not committed), and is
  invalid anyway — no rotation urgency, but rotate if you reuse it elsewhere.
