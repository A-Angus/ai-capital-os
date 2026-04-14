---
description: "Summarize the past week — what got done, what slipped, goal alignment check, and plan next week's priorities."
argument-hint: "[--week YYYY-MM-DD] [--plan-next true|false]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, TodoWrite]
---

# Weekly Review

The user wants to review the past week's progress, check alignment with goals, and plan the upcoming week.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- `--week` — start date of the week to review (default: current week)
- `--plan-next` — whether to also plan next week (default: true)
- Calculate the date range: Monday through Sunday of the target week

### Step 1: Gather Weekly Data
- Read all daily logs from the week: `~/.claude/brain/daily/YYYY-MM-DD.md` (Mon-Sun)
- Read `~/.claude/brain/goals.md` for quarterly and weekly priorities
- Read `~/.claude/brain/projects/README.md` for current project statuses
- Check for any completed or newly created project files

### Step 2: Analyze the Week
Categorize all logged activity:
- **Completed:** Tasks and deliverables that shipped
- **In Progress:** Work that started but isn't done
- **Slipped:** Planned tasks that didn't happen
- **Unplanned:** Work that came up unexpectedly
- **Revenue Activity:** Anything that generated or moved toward revenue
- **Build Activity:** System/product building work

### Step 3: Goal Alignment Check
Compare actual work against:
- Weekly priorities from goals.md
- Monthly focus area
- Quarterly objectives
- Flag any misalignment between stated priorities and actual time spent

### Step 4: Generate the Review

```markdown
# Weekly Review: [Mon Date] — [Sun Date]
> Generated: YYYY-MM-DD

## Score: [X/10]

## What Got Done
- [Accomplishment with context]
...

## What Slipped
- [Planned but didn't happen] — **Why:** [reason] — **Impact:** [consequence]
...

## Revenue vs. Build Split
- **Revenue-generating work:** X% of logged activity
- **Building/investing work:** X% of logged activity
- **Admin/other:** X% of logged activity

## Goal Alignment
| Goal | Status This Week | On Track? |
|------|-----------------|-----------|
| [Q1 goal] | [what happened] | [Yes/No/At Risk] |
...

## Key Wins
1. [Biggest win of the week]
2. [Second biggest]
3. [Third]

## Key Lessons
1. [What you learned or should adjust]

## Bottleneck Check
- **Biggest bottleneck this week:** [what held things back]
- **Suggested fix:** [how to address it]
```

### Step 5: Plan Next Week (if --plan-next)

```markdown
## Next Week Plan: [Mon Date] — [Sun Date]

### Top 3 Priorities
1. [Highest priority — specific and measurable]
2. [Second priority]
3. [Third priority]

### Day-by-Day Focus
| Day | Primary Focus | Key Tasks |
|-----|--------------|-----------|
| Mon | [focus area] | [specific tasks] |
| Tue | [focus area] | [specific tasks] |
...

### Must-Hit Deadlines
- [Deadline and what's due]

### Carries Over from This Week
- [Unfinished items that need to move forward]
```

### Step 6: Save the Review
- Save to `~/.claude/brain/daily/weekly-review-YYYY-MM-DD.md`
- Update `~/.claude/brain/goals.md` weekly priorities section if planning next week
- Report the review summary and file location to the user
