---
description: "Add, update, view, or manage leads in your deal pipeline — track contacts through stages from New Lead to Closed."
argument-hint: "[add|update|status|pipeline|follow-ups] [name] [--stage new|contacted|qualified|negotiating|closed-won|closed-lost] [--value amount] [--source where-from] [--next-action text] [--notes text] [--follow-up YYYY-MM-DD]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, TodoWrite]
---

# Lead Tracker

The user wants to manage leads in their deal pipeline — add new leads, update existing ones, view pipeline status, or check follow-ups.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract the action: `add`, `update`, `status`, `pipeline`, or `follow-ups`
- Extract lead name (if applicable)
- `--stage` — pipeline stage: new, contacted, qualified, negotiating, closed-won, closed-lost
- `--value` — estimated deal value (parse $5K, $5,000, 5000, etc.)
- `--source` — where the lead came from (referral, social media, website, etc.)
- `--next-action` — what needs to happen next
- `--notes` — additional context or notes to log
- `--follow-up` — follow-up date (YYYY-MM-DD, or "3 days", "next week", etc.)
- If no action specified, default to `pipeline` (show full pipeline overview)
- If no arguments at all, show pipeline summary

### Step 1: Initialize Pipeline (if first run)
- Check if `brain/pipeline/` exists
- If not, create:
  - `brain/pipeline/` directory
  - `brain/pipeline/leads/` directory
  - `brain/pipeline/README.md` with the dashboard template (see SKILL.md for format)
- If it already exists, proceed

### Step 2: Execute the Action

**`add` — Add a New Lead:**
1. Verify a name was provided. If not, ask: "What is the lead's name?"
2. Check if `brain/pipeline/leads/{firstname-lastname}.md` already exists
   - If yes, warn user and suggest using `update` instead
   - If user confirms it is a different person with the same name, use `{firstname-lastname}-2.md`
3. Create the lead file at `brain/pipeline/leads/{firstname-lastname}.md` using this template:

```markdown
# {Full Name}

> **Stage:** new
> **Created:** {YYYY-MM-DD}
> **Last Updated:** {YYYY-MM-DD}
> **Follow-Up Date:** {YYYY-MM-DD — default 3 days from now}

## Contact Info

| Field | Value |
|-------|-------|
| Name | {name} |
| Company | {company or "—"} |
| Phone | {phone or "—"} |
| Email | {email or "—"} |
| Source | {where the lead came from or "—"} |

## Deal Info

| Field | Value |
|-------|-------|
| Estimated Value | ${amount or "TBD"} |
| Product/Service | {what they need} |
| Timeline | {when they need it} |
| Decision Maker | {yes/no/unknown} |

## Notes

- {YYYY-MM-DD}: Lead added. {any initial notes}

## Interaction History

| Date | Type | Summary |
|------|------|---------|
| {date} | Added | Lead created |
```

4. Update `brain/pipeline/README.md` dashboard table with the new lead
5. Confirm: "Lead added: {Name} ({Company}). Stage: New. Follow-up set for: {date}."

**`update` — Update a Lead:**
1. Search `brain/pipeline/leads/` for the lead by name (fuzzy match if exact not found)
2. If not found, list existing leads and ask which one they meant
3. Read the lead file
4. Update the specified fields:
   - Stage change: update `> **Stage:**` line
   - Value change: update Deal Info table
   - Notes: append to Notes section with timestamp
   - Follow-up: update `> **Follow-Up Date:**` line
   - Next action: append to Notes
5. Update `> **Last Updated:**` to today
6. Add entry to Interaction History table
7. Rebuild the dashboard in `brain/pipeline/README.md`
8. Confirm: "{Name} moved from {old stage} to {new stage}. Notes logged."

**`status` — View a Specific Lead:**
1. Search for the lead by name
2. Read and display their full file: contact info, deal info, stage, notes, history
3. Highlight if follow-up is overdue or if the lead has been stale (no update in 7+ days)

**`pipeline` — Full Pipeline Dashboard:**
1. Read ALL files in `brain/pipeline/leads/`
2. For each lead, extract: name, company, stage, value, next action, follow-up date, last updated
3. Rebuild and display the pipeline summary:
   - Count of leads per stage
   - Total pipeline value (active leads only — exclude closed-won and closed-lost)
   - Total won value
   - Leads needing follow-up (overdue)
   - Stale leads (no update in 7+ days)
4. Update `brain/pipeline/README.md` with fresh data
5. Present the formatted dashboard

**`follow-ups` — Who Needs Follow-Up:**
1. Read ALL files in `brain/pipeline/leads/`
2. Check each lead's follow-up date against today
3. Flag leads where:
   - Follow-up date is today or past
   - Lead has been in the same stage for 7+ days with no activity
   - Lead is in "contacted" or "negotiating" (high-priority stages)
4. Sort by urgency (most overdue first)
5. Present the follow-up list with recommended actions

### Step 3: Report
- Confirm the action taken
- Show the relevant output (lead details, pipeline summary, or follow-up list)
- Flag any leads with no next action or overdue follow-ups
- Suggest next steps if appropriate
