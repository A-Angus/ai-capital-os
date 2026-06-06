# Two account-level actions only YOU can complete — ~5 min total

These unlock the last revenue capabilities. I staged them; they need your hands
because they require your credentials / OAuth consent.

## 1. Gmail SEND scope  (unlocks Follow-Up Automation end-to-end)
Today Gmail is **draft-only** — the scanner writes drafts to brain/drafts/ but
nothing can send them. To enable sending:
- Re-authorize the Gmail connector with **send** scope (in the Claude/MCP
  connector settings for mr.alexangus@gmail.com), OR
- Configure the VPS `himalaya` email CLI (already installed at
  /home/hermes/.hermes/skills/email/himalaya) with an app password so the VPS
  can send directly.
Recommended: connector send-scope (no password storage on VPS).

## 2. GitHub auth on VPS  (unlocks VPS-side brain/vault versioning)
`gh` is not logged in on the VPS and /home/lexbot/CentralBrain is not a git repo.
Run, on the VPS, as the right user:
```
ssh vps
gh auth login            # choose GitHub.com > HTTPS > paste a token or device code
# then version the VPS CentralBrain mirror:
cd /home/lexbot/CentralBrain && git init && \
  git remote add origin https://github.com/A-Angus/centralbrain.git && \
  git add -A && git commit -m "VPS CentralBrain baseline" 
```
(The Mac/mini already hold the canonical git repo — this just gives the VPS a
versioned mirror so nightly sync is auditable.)

## Optional next build (I can do on approval): self-updating calendar
Make the morning brief pull calendar without the MCP seam by having `hermes`
(which holds /home/hermes/.hermes/google_token.json) write brain/calendar/today.json
nightly. ~1-2 hrs. Say the word and I'll wire it.
