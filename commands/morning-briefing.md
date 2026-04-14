---
description: "Generate a CEO-level morning briefing — today's priorities, project status, deadlines, carry-overs, and what matters most."
argument-hint: "[--save] [--location city]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebSearch, TodoWrite]
---

# Morning Briefing

The user wants a structured executive-level morning briefing pulled from their goals, projects, calendar, daily logs, and follow-ups.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Check for `--save` flag — if present, save briefing to today's daily log after printing
- Check for `--location [city]` — if present, use for weather lookup
- If no arguments, print briefing to terminal only (ask about saving after)

### Step 1: Gather Intelligence

Read these files in order. Stop early if context is sufficient.

**Required:**
1. Read `brain/goals.md` — Extract: weekly priorities, monthly focus, what's slipping, decision framework
2. Read `brain/projects/README.md` — Extract: active project dashboard, statuses, next actions
3. Glob `brain/daily/*.md` — Find most recent 1-2 daily logs. Read them for carry-overs and continuity.

**Conditional:**
4. Glob `brain/calendar/*.md` — Find current month file. Read for this week's plan and deadlines.
5. Check if `brain/pipeline/follow-ups.md` exists. If yes, read for due/overdue items.
6. Skim `brain/people/README.md` if any contacts are referenced in today's tasks.

### Step 2: Check External Context
- If `--location` provided or location is known from brain files, search for today's weather
- Check if today is a notable holiday or event
- If web search is unavailable, skip and note it

### Step 3: Analyze and Prioritize

Apply the Decision Framework from goals.md to determine:
1. **The #1 thing** — Single most important task or decision today
2. **Top 3 priorities** — What MUST get done (not what COULD get done)
3. **Active fires** — Anything 🔥 Behind or with deadline within 48 hours
4. **Carry-overs** — Incomplete tasks from yesterday's log
5. **Upcoming deadlines** — Due within 7 days
6. **Slipping items** — Patterns of avoidance or repeated delays
7. **Follow-ups due** — Commitments due today or overdue

### Step 4: Generate Briefing

Print the briefing using this exact structure:

```
================================================================
  MORNING BRIEFING — [Day of Week], [Month DD, YYYY]
================================================================

THE ONE THING
─────────────
[Single sentence: the most important thing today]

TODAY'S TOP 3
─────────────
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]

ACTIVE FIRES
─────────────
- [Description and recommended action]
(Or: "All clear. No emergencies.")

CARRY-OVERS FROM YESTERDAY
───────────────────────────
- [Task — context — action]
(Or: "Clean slate.")

DEADLINES THIS WEEK
────────────────────
| Deadline | What | Days Left |
|----------|------|-----------|

PROJECT PULSE
─────────────
- [Project] — [Status] — [Next action]

WHAT'S SLIPPING
───────────────
- [Item — duration — suggested fix]
(Or: "Everything's on track.")

FOLLOW-UPS DUE
──────────────
- [Person/topic — commitment — due date]
(Or: "No pending follow-ups.")

WEATHER & CONTEXT
─────────────────
[Weather or "Not checked."]

THE MINDSET
───────────
[One grounded, motivational sentence tied to their actual goals]
================================================================
```

### Step 5: Save (If Requested)
- If `--save` flag was used OR user confirms they want it saved:
  - Create `brain/daily/{YYYY-MM-DD}.md` if it doesn't exist
  - Append briefing under `## Morning Briefing` section
  - Confirm: "Briefing saved to brain/daily/{YYYY-MM-DD}.md"
- If not saving, ask: "Want me to save this to today's daily log?"

### Step 6: Transition
After delivering the briefing, ask:
"What do you want to tackle first?"

This naturally transitions the user from planning mode into execution mode.