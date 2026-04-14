---
description: "Quick status check across all active projects — what's on track, what's behind, what needs attention now."
argument-hint: "[--project specific-project-name] [--detail brief|full]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, TodoWrite]
---

# Project Pulse

The user wants a quick pulse check on all active projects (or a specific one) to understand what's on track, what's slipping, and what needs attention.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- `--project` — specific project to check (default: all active projects)
- `--detail` — level of detail (default: brief)
- If no arguments, run a full pulse check across all projects

### Step 1: Load Project Data
- Read `~/.claude/brain/projects/README.md` for the project dashboard
- Read `~/.claude/brain/goals.md` for current priorities and deadlines
- Read today's daily log if it exists: `~/.claude/brain/daily/YYYY-MM-DD.md`
- Read the most recent daily logs (last 3-5 days) for recent activity
- If `--project` specified, also read that project's dedicated file

### Step 2: Assess Each Project
For each active project, evaluate:
- **Status vs. Last Check:** Has it moved forward or stalled?
- **Goal Alignment:** Does current progress match the timeline in goals.md?
- **Blockers:** Any mentioned blockers or dependencies?
- **Last Activity:** When was the last logged work on this project?
- **Next Action:** Is there a clear next step defined?

### Step 3: Generate the Pulse Report

```markdown
# Project Pulse — YYYY-MM-DD

## Overall Health: [GREEN / YELLOW / RED]

## Quick Status
| Project | Status | Health | Last Activity | Next Action | Deadline Risk |
|---------|--------|--------|--------------|-------------|---------------|
| [name] | [status] | [G/Y/R] | [date] | [action] | [ok/at-risk/overdue] |
...

## Needs Attention NOW
1. **[Project]** — [Why it needs attention, what's at risk]
...

## On Track
- [Project] — [Brief note on progress]
...

## Stalled / No Activity
- [Project] — Last activity: [date], [X] days ago
...

## Goal Alignment Check
- **Q1 Objective 1:** [On track / Behind / At risk] — [brief note]
- **Q1 Objective 2:** [On track / Behind / At risk] — [brief note]
...

## Recommended Focus Today
1. [Highest-impact action based on current state]
2. [Second priority]
3. [Third priority]
```

### Step 4: Flag Critical Issues
- Any project with no activity in 7+ days gets flagged
- Any project past its deadline gets a red alert
- Any goal-critical project that's behind gets highlighted

### Step 5: Report to User
- Display the pulse report
- Lead with the most critical items
- End with the recommended focus for today
