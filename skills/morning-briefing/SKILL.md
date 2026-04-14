---
name: morning-briefing
description: This skill should be used when the user says "morning briefing", "what's on my plate today", "brief me", "what should I focus on today", "what's happening today", "today's priorities", "start my day", "daily brief", "morning report", "CEO briefing", "what matters today", "give me the rundown", "what's the plan today", "top priorities today", "daily rundown", "kick off my day", "what do I need to know today", "morning update", or wants a structured executive-level summary of the day ahead pulled from their goals, projects, calendar, and recent activity.
version: 1.0.0
---

# Morning Briefing — CEO-Level Daily Intelligence Report

## Overview

Morning Briefing generates a structured, executive-level daily report that tells you exactly what matters today. It reads your goals, active projects, calendar, recent daily logs, and pending follow-ups to produce a single briefing that replaces the mental overhead of figuring out where to start. This is the difference between waking up and reacting vs. waking up and executing. Your AI reads your entire operating context so you don't have to.

## When This Skill Applies

- User says "morning briefing" or "brief me"
- User says "what should I focus on today" or "what's on my plate"
- User says "start my day" or "kick off my day"
- User says "daily brief" or "morning report" or "CEO briefing"
- User says "today's priorities" or "what matters today"
- User says "give me the rundown" or "daily rundown"
- User says "what do I need to know today"
- User triggers the `/morning-briefing` command
- It's the start of a work session and the user wants to orient

## Category

Clone Your Decision-Making

## How It Works

### Step 1: Gather Intelligence

Read the following files to build a full picture of the user's current state. Do NOT load everything at once — read in order of priority and stop early if context is sufficient.

**Required reads:**
1. `brain/goals.md` — Current weekly priorities, monthly focus, what's slipping, decision framework
2. `brain/projects/README.md` — Active project dashboard, status, next actions
3. `brain/daily/` — Check for yesterday's log and today's log (if it exists). Read the most recent 1-2 daily logs for continuity.

**Conditional reads (if they exist):**
4. `brain/calendar/` — Current month's calendar file (e.g., `brain/calendar/2026-03.md`) for this week's plan and deadlines
5. `brain/pipeline/follow-ups.md` — Any pending follow-ups due today or overdue
6. `brain/people/README.md` — Quick scan for any contacts referenced in today's tasks

### Step 2: Analyze and Prioritize

Using the Decision Framework from goals.md, analyze everything you've read and determine:

1. **The #1 thing that matters today** — The single most important task or decision
2. **Top 3 priorities** — What must get done today (not what could get done)
3. **Active fires** — Anything marked 🔥 Behind or with a deadline within 48 hours
4. **Carry-overs** — Tasks from yesterday that didn't get completed
5. **Upcoming deadlines** — Anything due in the next 7 days
6. **What's slipping** — Patterns of avoidance or repeated delays

### Step 3: Check External Context

If web search is available:
- Check weather for the user's location (relevant for outdoor meetings, commute, energy)
- Check if today is a holiday or notable date that affects business operations

If web search is not available:
- Skip this step. Note in the briefing that weather/external context was not checked.

### Step 4: Generate the Briefing

Produce the briefing in the format specified in the Output Format section below. The tone should be direct and actionable — like a chief of staff handing a CEO a one-page brief before the first meeting of the day. No pleasantries. No filler. Just what matters.

### Step 5: Save to Daily Log (Optional)

If the user wants the briefing saved:
- Create or append to `brain/daily/{YYYY-MM-DD}.md`
- Add the briefing under a `## Morning Briefing` section
- If today's log already exists, append — do not overwrite

If the user does not specify, print to terminal only. Ask: "Want me to save this to today's daily log?"

## Output Format

```
================================================================
  MORNING BRIEFING — [Day of Week], [Month DD, YYYY]
================================================================

THE ONE THING
─────────────
[Single sentence: the most important thing to accomplish today]

TODAY'S TOP 3
─────────────
1. [Priority 1 — specific, actionable]
2. [Priority 2 — specific, actionable]
3. [Priority 3 — specific, actionable]

ACTIVE FIRES
─────────────
[If any items are marked 🔥 Behind or have imminent deadlines]
- [Fire 1 — what it is, why it's urgent, what to do about it]
- [Fire 2]
(If no fires: "All clear. No emergencies.")

CARRY-OVERS FROM YESTERDAY
───────────────────────────
[Tasks from yesterday's log that weren't completed]
- [Task — original context — recommended action today]
(If none: "Clean slate. Yesterday's tasks were handled.")

DEADLINES THIS WEEK
────────────────────
| Deadline | What | Days Left |
|----------|------|-----------|
| [Date] | [Description] | [X days] |

PROJECT PULSE
─────────────
[One-line status for each active project from the dashboard]
- [Project Name] — [Status emoji] — [Next action or current blocker]

WHAT'S SLIPPING
───────────────
[Patterns of delay or avoidance identified from goals.md and recent logs]
- [Item — how long it's been slipping — suggested intervention]
(If nothing: "Everything's on track.")

FOLLOW-UPS DUE
──────────────
[Any follow-ups due today or overdue from brain/pipeline/follow-ups.md]
- [Person/topic — what was promised — due date]
(If none or file doesn't exist: "No pending follow-ups tracked.")

WEATHER & CONTEXT
─────────────────
[Weather summary if available, or "External context not checked."]
[Any relevant holidays, market events, or calendar notes]

THE MINDSET
───────────
[One sentence — motivational but grounded. Tied to the user's actual
goals and current situation. Not generic inspiration. Something that
connects today's work to the bigger vision from goals.md.]
================================================================
```

## Example Usage

**User:** "Morning briefing"

**AI reads:** goals.md, projects/README.md, daily/2026-03-02.md (yesterday), calendar/2026-03.md

**AI output:**
```
================================================================
  MORNING BRIEFING — Monday, March 3, 2026
================================================================

THE ONE THING
─────────────
Get the investor pitch deck finalized and sent to Sarah Chen before 5pm.

TODAY'S TOP 3
─────────────
1. Finalize investor pitch deck — Sarah is expecting it today
2. Run /deal-analyzer on the Elm Street fourplex lead from Friday
3. Record and post this week's YouTube video (script is ready)

ACTIVE FIRES
─────────────
- Syndication fund docs — 🔥 Behind by 3 weeks. Attorney needs your
  feedback on PPM draft. This has been pushed twice. Block 1 hour today.

CARRY-OVERS FROM YESTERDAY
───────────────────────────
- Follow up with Tom Bradley on commitment amount — was on Friday's
  list, didn't happen. Do it before lunch today.

DEADLINES THIS WEEK
────────────────────
| Deadline | What | Days Left |
|----------|------|-----------|
| Mar 5 | Inspection deadline, Elm Street | 2 days |
| Mar 7 | Monthly investor newsletter | 4 days |

PROJECT PULSE
─────────────
- Portfolio Redesign — 🟡 In Progress — Designer mockups under review
- Q1 Acquisitions — 🟢 On Track — 3 new leads to analyze
- Tenant Portal — 🔴 Not Started — Deprioritized until Q2
- Tax Prep — ⏸️ Paused — Waiting on Q4 receipts

WHAT'S SLIPPING
───────────────
- YouTube content: 2 weeks behind schedule. You've skipped the last
  2 planned recording sessions. Block 90 minutes Wednesday — non-negotiable.
- Investor updates: No newsletter sent since January. Erodes trust.
  Draft one this week even if it's short.

FOLLOW-UPS DUE
──────────────
- Tom Bradley — committed to $50K, needs confirmation — due today
- Marcus (CPA) — send Q4 receipts — overdue by 5 days

WEATHER & CONTEXT
─────────────────
Phoenix, AZ: 72°F, sunny, clear all day. Good energy day.
No holidays. Market open — check positions if trading.

THE MINDSET
───────────
You're 17 units away from your year-end goal of 40. Every deal you
analyze today is a step toward that number. The pitch deck isn't
paperwork — it's the key that unlocks the fund. Ship it.
================================================================
```

## Error Handling

- **If `brain/goals.md` does not exist or is empty:** Warn the user: "Your goals.md is empty. I can't generate a meaningful briefing without knowing your priorities. Run /brain-dump to add your goals first, or fill in goals.md manually." Generate a minimal briefing with just project status if available.
- **If `brain/projects/README.md` does not exist or is empty:** Skip the Project Pulse section. Note: "No active projects tracked. Add projects to brain/projects/README.md to see them here."
- **If no daily logs exist yet:** Skip Carry-Overs section. Note: "No previous daily logs found. This briefing will improve as you use the system — your AI learns your patterns over time."
- **If `brain/calendar/` has no current month file:** Skip the Deadlines This Week section unless deadlines are mentioned in goals.md. Note: "No monthly calendar found. Create brain/calendar/YYYY-MM.md to get deadline tracking."
- **If `brain/pipeline/follow-ups.md` does not exist:** Skip Follow-Ups section. Note: "No follow-up tracker found. Use /follow-up add to start tracking commitments."
- **If web search is unavailable:** Skip Weather & Context or note "External context not checked — web search unavailable." Do not let this block the rest of the briefing.
- **If today's daily log already has a morning briefing:** Ask: "Today's log already has a morning briefing. Want me to overwrite it with a fresh one, or just print this to terminal?"
- **If the user runs this at night or late afternoon:** Adjust the tone. Instead of "morning briefing" frame it as "end-of-day status check" or "evening review" depending on the time. The structure stays the same but the framing shifts from "what to do today" to "where do things stand."

## Cost Estimate

| Scenario | Estimated Cost |
|----------|---------------|
| Standard morning briefing (reads 4-6 files, generates report) | $0.05–$0.15 |
| Briefing with web search (weather, market data) | $0.10–$0.25 |
| Briefing saved to daily log | Same as above (minimal write cost) |

## What Makes This Premium

A human executive assistant doing this would need to:
1. Read your entire goal framework and remember what matters this quarter
2. Check every active project and know the current status
3. Review yesterday's work and identify what carried over
4. Scan your calendar and flag upcoming deadlines
5. Remember your follow-up commitments
6. Check the weather and any relevant external factors
7. Synthesize all of that into a one-page brief in under 5 minutes

That's a $180K/year chief of staff doing a 30-minute morning routine. This skill does it in seconds, every single day, without forgetting anything, without bias, and without needing coffee first.