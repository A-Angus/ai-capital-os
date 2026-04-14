---
description: "Pipeline intelligence on demand — deals by stage, velocity, stale deals, revenue forecast, and top deals most likely to close this week."
argument-hint: "[pipeline-name] [--stage new|contacted|qualified|negotiating|proposal-sent|closed-won|closed-lost] [--stale-only] [--forecast] [--top-deals]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebSearch, TodoWrite]
---

# Pipeline Sync

The user wants pipeline intelligence — an analysis of their deal pipeline with stage breakdown, velocity metrics, stale deal detection, revenue forecasting, and deal prioritization.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract pipeline name (optional — filter deals to a specific category/vertical)
- `--stage` — filter to a specific pipeline stage
- `--stale-only` — show only stale deals that need attention
- `--forecast` — show only the revenue forecast section
- `--top-deals` — show only the top 3 deals most likely to close this week
- If no arguments provided, generate the full pipeline intelligence report

### Step 1: Load Pipeline Data
- Read all deal files from `brain/pipeline/leads/`
- Read `brain/pipeline/README.md` for dashboard context
- Read `brain/pipeline/kpis.md` for targets and KPI cross-referencing (if exists)
- Read `brain/goals.md` for revenue targets and quarterly context
- If `brain/pipeline/leads/` does not exist or is empty, report the empty state and suggest next steps

### Step 2: Extract Deal Data
For each deal file, extract:
- Name, company, stage, deal value, created date, last updated date
- Follow-up date, next action, source, interaction count
- Use fallback values for any missing fields (see SKILL.md for fallback table)

### Step 3: Generate the Report

**Full report (default):**

```markdown
# Pipeline Intelligence Report — {Date}

> **Total Active Deals:** {count}
> **Total Pipeline Value:** ${amount}
> **Weighted Forecast (this month):** ${amount}
> **Pipeline Health:** {STRONG / HEALTHY / ATTENTION NEEDED / CRITICAL}

## Executive Summary
{3-4 sentences: health, biggest opportunity, biggest risk, recommended action}

## Pipeline by Stage
| Stage | Deals | Value | Avg Days | Longest |
|-------|-------|-------|----------|---------|
| New | {X} | ${Y} | {Z} days | {name} ({N}d) |
| Contacted | | | | |
| Qualified | | | | |
| Negotiating | | | | |
| Proposal Sent | | | | |
| **Active Total** | **{X}** | **${Y}** | | |

## Top 3 Deals to Close This Week
### 1. {Name} — ${Value}
- **Stage:** {stage} | **Last Activity:** {days} ago
- **Why it's hot:** {signals}
- **Next Action:** {specific action}
(repeat for 2 and 3)

## Stale Deals
| Deal | Value | Stage | Days Inactive | Action |
|------|-------|-------|--------------|--------|
| {name} | ${val} | {stage} | {days} | {action} |
**Value at risk: ${total}**

## Deal Velocity
| Transition | Avg Days | Status |
|-----------|----------|--------|
| New → Contacted | {X} | {OK/SLOW} |
| Contacted → Qualified | {X} | {OK/SLOW} |
| Qualified → Negotiating | {X} | {OK/SLOW} |
| Negotiating → Closed | {X} | {OK/SLOW} |
| **Full Cycle** | **{X}** | **{OK/SLOW}** |
**Bottleneck:** {slowest stage}

## Revenue Forecast
| | This Month | This Quarter |
|--|-----------|-------------|
| Closed | ${X} | ${Y} |
| Weighted Pipeline | ${X} | ${Y} |
| **Projected** | **${X}** | **${Y}** |
| Target | ${X} | ${Y} |
| Gap | ${X} | ${Y} |

## Recommendations
1. **{Action}** — {why and expected impact}
2. **{Action}** — {why and expected impact}
3. **{Action}** — {why and expected impact}
```

**Filtered reports:**
- `--stale-only`: Show only the Stale Deals section with expanded recommendations
- `--forecast`: Show only Revenue Forecast with month and quarter projections
- `--top-deals`: Show only Top 3 Deals with expanded scoring breakdown
- `--stage {X}`: Show only deals in the specified stage with individual deal details

### Step 4: Save and Report
- Display the report in terminal
- Save full report to `brain/research/pipeline-report-{YYYY-MM-DD}.md`
- Append condensed summary to `brain/daily/{YYYY-MM-DD}.md`
- Update KPIs in `brain/pipeline/kpis.md` if pipeline-related KPIs exist
- Flag any data quality issues (missing values, inconsistent formats)
