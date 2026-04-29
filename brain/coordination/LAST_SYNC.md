# Last Sync

**Purpose:** Snapshot of current state and recommended next actions. Updated every session.

**Last Sync:** 2026-04-29 01:21 UTC

---

## What Was Done This Session (Atlas / Claude Code)

1. Tightened lexx8 file-editing rules in agent.json (avoid Edit failures on small status files)
2. Created comprehensive backup at `/home/lexbot/backups/openclaw-hermes-20260425-0542/` (190M openclaw config, 16M /root/drafts, 58K /root/memory)
3. Mapped and verified Hermes ↔ openclaw integration (cron jobs healthy, both lastRunStatus=ok)
4. Patched Hermes phase oscillation in `/root/drafts/hermes_worker.py` — now correctly reports phase 8 instead of clamping to 5
5. **Upgraded OpenClaw 2026.3.24 → 2026.4.23** (one month of fixes including Telegram cron delivery, per-model rate-limit cooldowns, codex/anthropic 1M context, native Claude CLI plugin)
6. Set up Claude OAuth via CLI bridge — first via community proxy, then migrated to native `claude-cli` plugin in 4.23, retired the proxy
7. Final cascade: **codex primary** (1025k ctx, ~4s response), claude-cli/opus-4-7 fallback, claude-cli/sonnet-4-6 fallback
8. **Reset bloated lexx8 telegram session** (569 msgs, 336K tokens) — backup at `/home/lexbot/backups/lexx8-session-reset-20260425/`
9. Populated `/root/IDENTITY.md`, `/root/USER.md`, `/root/AGENTS.md` for openclaw 4.23's bootstrap loader (Lexx persona + Alex profile + workspace operating manual)
10. **Refreshed Gmail OAuth token** — was expired (`invalid_grant`); new token at `/home/openclaw/.config/gogcli/token.json` writes Apr 25 08:40
11. **Reconciled Parkhill/Tiara status** — was wrongly marked closed in last sync; deal actually died at the closing table

---

## Infrastructure Status

| Service | Status | Notes |
|---------|--------|-------|
| atlas-bridge (PM2) | ✅ Running | Stable |
| openclaw (systemd) | ✅ Running | **v2026.4.23** (upgraded today) |
| claude-max-api (proxy) | 🛑 Disabled | Replaced by native claude-cli plugin |
| n8n (systemd) | ❌ Dead | Stopped since Mar 27 |
| Email triage cron | ❌ Dead | Script never deployed |
| Morning briefing cron | ✅ Active | 7am daily |
| Brain sync cron | ✅ Active | 2am daily |
| Hermes operator-loop | ✅ Active | every 30 min, lastStatus=ok |
| Hermes status-pulse | ✅ Active | every 10 min, lastStatus=ok |
| inbox-wave / morning-brief / evening-brief | ⚠️ Telegram delivery errors | broken on outbound channel — separate fix |
| gmail_tool.py | ✅ Working | Token refreshed Apr 25 |

---

## Pipeline Snapshot

| Category | Count | Key Items |
|----------|-------|-----------|
| 🔴 Urgent | 2 | Paul Brown call (queued 4/15, 10 days stale, 801-698-7171) — call or kill; API token rotation (GitGuardian alert, 11 days open) |
| 🟡 Active | 6+ | Bryan/DFS review queue (Draw Schedule Prelim, Trades District deck, West Campus Towers reply), Capital intake (ResCap Partners CyclSales decision) |
| ⚪ Stalled | 3 | Coalson Excavation (~19d), ACJ Built (~38d), Gheorghe Cucu (~41d+) |
| ☠️ Dead | 1 | **Parkhill Drive / Tiara Williams** — failed at closing table (no cash to close); operating rule: don't treat as live unless new buyer/structure appears |
| 🔒 Security | 1 | Token rotation outstanding |

---

## Recent Context (Apr 23–28)

- **Parkhill: dead** (Apr 23 confirmed, Apr 24 reconfirmed). LAST_SYNC was wrong on this for 10 days. No $4,600 fee — that was based on a faulty close assumption.
- **Bryan invited Alex** to "Capital for Warren Green Hotel" call Tue May 5 8am PT (with Brandon at Legends Acquisitions, Kash at Madison Dale).
- **Other Apr 24 deal updates** in `/root/memory/`: `2026-04-24-malve-capital.md`, `2026-04-24-craig-fournier-dead-deal.md` (Craig Fournier deal also dead).
- LexxBot identity scaffolding now in place — Lexx persona, Alex profile, workspace ops manual are loaded on every new session via openclaw bootstrap.
- Inbox waves on Apr 28 were low-signal until the late pass surfaced a **new urgent live deal**: `700 W La Veta Ave Unit E4` Orange CA DSCR takeout with a June 1 bridge maturity. RCN capped around 70% LTV; borrower cannot fill the gap.
- **Mike Kelly / Highlands moved another step forward** on Apr 28: Bryan asked for exclusivity, Mike said he is amenable depending on timeframe, and Bryan also forwarded the file docs to Brandon. The blocker is no longer silence; it is getting exclusivity terms nailed down and activating the lender push.
- **Racquel Collier / Gibson Development** also progressed: entity docs + operating agreement landed, so that DSG file is now review-ready instead of passive wait-state.

---

## Recommended Next Actions (Priority Order)

1. **700 W La Veta Ave / Orange CA refinance rescue** — June 1 bridge maturity. RCN is only at ~70% LTV due to HOA drag; borrower says he cannot bring the gap. Need alternate lender / no-ratio / IO path or fresh cash plan fast.
2. **Paul Brown call** — most time-sensitive stale outreach. 801-698-7171. Either call or formally kill.
3. **Highlands / Mike Kelly exclusivity** — Mike is amenable depending on timeframe; Bryan/Brandon now need to set the exclusivity window and actually activate lender outreach.
4. **Gibson Development / Racquel Collier** — org docs + operating agreement arrived; file is now review-ready.
5. **ResCap Partners decision** — does it go into CyclSales? Capital intake.
6. **Rotate exposed API tokens** — Telegram + HighLevel (GitGuardian, now 11+ days open).
7. **Fix Telegram outbound** for inbox-wave / morning-brief / evening-brief crons (broken delivery).
8. **Confirm Warren Green Hotel** call attendance for May 5 8am PT.

---

## Evening Brief Addendum (2026-04-29 01:00 UTC)

- No later inbox pass changed the core picture after the 22:21 UTC wave.
- Biggest email change today was the **700 W La Veta Ave / Orange CA** refinance rescue becoming a live June 1 fire-drill after RCN capped proceeds around 70% LTV and borrower said he cannot cover the gap.
- Other real movement today: **Highlands / Mike Kelly** moved from chase mode toward exclusivity/lender activation, and **Gibson Development / Racquel Collier** became review-ready when entity docs landed.
- **CRM:** no confirmed CRM writes/logged record changes today. CRM-adjacent work remains blocked or pending decision (ResCap/CyclSales disposition; broader CRM record-ID population still approval-gated in memory).

## Late Inbox Addendum (2026-04-29 01:21 UTC)

- Another pass confirmed **no new business urgency** after the 22:21 UTC wave.
- New unread was mostly personal clutter: **Walmart order / cancellation traffic**, rental alerts, Skool digests, and generic lender marketing.
- One minor cleanup signal: **Josh Lahr / CoreVest** acknowledged the dead Crownsville MD fix-and-flip thread, so that one can be treated as closed-loop with no further action needed.

---

## Items Requiring Alex's Decision

- Paul Brown — call or kill?
- ResCap Partners — into CyclSales or skip?
- Whether to rebuild a fresh "active deals" board now that the queue is 10+ days stale
- Atlanta All Sports Dome — role and fee structure (still pending from Apr 22)
- Whether to attempt Anthropic Extra Usage activation so claude-cli/anthropic fallbacks have headroom (currently inert without it)

---

## Next Sync Target

Next inbox-wave or end of day.
