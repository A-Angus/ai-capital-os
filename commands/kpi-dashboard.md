---
description: "Define, track, and report on KPIs across all businesses — trend arrows, on/off track status, and specific recommendations for underperforming metrics."
argument-hint: "[setup|update|report] [--kpi name] [--value amount] [--target amount] [--category revenue|pipeline|content|operations|financial|personal]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebSearch, TodoWrite]
---

# KPI Dashboard

The user wants to set up, update, or view their Key Performance Indicator dashboard.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract the action: `setup`, `update`, or `report` (default: `report`)
- `--kpi` — specific KPI name to update or view
- `--value` — new value for a KPI (parse $5K, 5000, 25%, etc.)
- `--target` — new target for a KPI
- `--category` — KPI category for new KPIs: revenue, pipeline, content, operations, financial, personal
- If the user provides raw numbers without flags (e.g., "revenue $18K, closed 6 deals"), parse them as bulk updates
- If no arguments provided and `brain/pipeline/kpis.md` does not exist, auto-switch to `setup`

### Step 1: Load Context
- Read `brain/pipeline/kpis.md` for current KPI definitions and values
- Read `brain/goals.md` for goal alignment context
- Read today's daily log `brain/daily/{YYYY-MM-DD}.md` if it exists
- If `brain/pipeline/kpis.md` does not exist and action is `report` or `update`, switch to `setup`

### Step 2: Execute the Action

**`setup` — Define KPIs:**
1. Read `brain/goals.md` to understand quarterly and monthly objectives
2. Propose KPIs aligned to each active goal — group by category:
   - Revenue & Financial (monthly revenue, average deal size, profit margin, cash runway)
   - Pipeline & Sales (active leads, qualified leads, close rate, deals closed, outreach volume)
   - Content & Marketing (posts/week, followers, engagement rate, email list size, CTR)
   - Operations (tasks completed, SOP compliance, response time)
   - Personal/Growth (hours worked, gym sessions, learning hours)
3. For each KPI, ask the user to confirm and provide: current value, target, update cadence
4. Save to `brain/pipeline/kpis.md` using the SKILL.md template format
5. Confirm setup complete and recommend first update cadence

**`update` — Log New Values:**
1. Parse which KPIs the user is updating (fuzzy match by name if needed)
2. For each matched KPI:
   - Record previous value
   - Set new current value
   - Calculate change (absolute and %)
   - Determine trend: up (improving toward target), down (declining from target), flat (<2% change)
   - Update status: Exceeded / On Track / Approaching / Off Track / Critical
3. Append each change to the History Log section with timestamp
4. Save the updated `brain/pipeline/kpis.md`
5. Report changes and flag any status transitions

**`report` — Generate Dashboard:**
1. Read all KPI data from `brain/pipeline/kpis.md`
2. Cross-reference with `brain/goals.md` for goal alignment
3. Generate the full dashboard:

```markdown
# KPI Dashboard — {Date}

> **Overall Health:** {STRONG / SOLID / MIXED / CRITICAL}
> **KPIs On Track:** {X} of {Y} ({Z}%)

## Executive Summary
{2-3 sentences: what is going well, what needs attention, #1 action item}

## Scorecard

### Revenue & Financial
| KPI | Target | Current | Trend | Status | Gap |
|-----|--------|---------|-------|--------|-----|
| {name} | {target} | {value} | {arrow} | {status} | {distance to target} |

### Pipeline & Sales
| KPI | Target | Current | Trend | Status | Gap |
|-----|--------|---------|-------|--------|-----|

### Content & Marketing
| KPI | Target | Current | Trend | Status | Gap |
|-----|--------|---------|-------|--------|-----|

### Operations & Growth
| KPI | Target | Current | Trend | Status | Gap |
|-----|--------|---------|-------|--------|-----|

## What is Working
- {on-track or exceeded KPI with context}

## What Needs Attention
- {off-track or critical KPI with specific diagnosis and action}

## Top 3 Recommendations
1. **{Action}** — {why, expected impact}
2. **{Action}** — {why, expected impact}
3. **{Action}** — {why, expected impact}

## Goal Alignment
| Goal | Related KPIs | Status | Risk |
|------|-------------|--------|------|
| {goal from goals.md} | {KPI names} | {combined status} | {notes} |
```

4. Display the full dashboard in terminal
5. Append condensed summary to `brain/daily/{YYYY-MM-DD}.md`

### Step 3: Report
- Confirm action taken
- For `report`: display the full dashboard
- For `update`: show what changed and flag any status transitions
- For `setup`: confirm KPIs saved and recommend first review date
- Always flag stale KPIs (not updated in 2x their stated cadence)
- Always flag KPIs in Critical status for 3+ consecutive periods with escalation
