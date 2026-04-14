---
description: "Parse meeting notes or transcript into structured action items, decisions, and follow-ups."
argument-hint: "[paste notes or path to file] [--attendees name1,name2] [--meeting-type call|zoom|in-person]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, TodoWrite]
---

# Meeting to Actions

The user wants to convert raw meeting notes or a transcript into structured action items, decisions, and follow-ups.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Check if $ARGUMENTS contains a file path — if so, read the file
- Check if $ARGUMENTS contains raw text/notes — if so, use directly
- `--attendees` — list of people in the meeting
- `--meeting-type` — context for formatting
- If no notes provided, ask the user to paste them or provide a file path

### Step 1: Parse the Content
- Identify speakers/participants (from names, "I said", attribution patterns)
- Identify topics discussed
- Flag anything that sounds like a decision, commitment, or action
- Note any deadlines or dates mentioned
- Identify any unresolved questions or parking lot items

### Step 2: Extract Action Items
For each action item, capture:
- **What:** The specific task
- **Who:** Person responsible (if mentioned)
- **When:** Deadline or timeframe (if mentioned)
- **Priority:** High/Medium/Low (inferred from context)
- **Context:** Brief note on why this matters

### Step 3: Structure the Output

```markdown
# Meeting Notes: [Topic/Title]
> **Date:** YYYY-MM-DD | **Type:** [call/zoom/in-person]
> **Attendees:** [names]

## Key Decisions
1. [Decision made, with context]
2. ...

## Action Items
| # | Task | Owner | Deadline | Priority |
|---|------|-------|----------|----------|
| 1 | [task] | [who] | [when] | [H/M/L] |
...

## Discussion Summary
[3-5 sentence summary of what was discussed]

## Open Questions / Parking Lot
- [Unresolved items that need follow-up]

## Raw Notes
<details>
[Original notes preserved for reference]
</details>
```

### Step 4: Cross-Reference People
- Check `~/.claude/brain/people/` for any attendees
- If a person doesn't exist in the CRM, suggest creating an entry

### Step 5: File the Notes
- Save to `~/.claude/brain/daily/YYYY-MM-DD.md` (append under a Meeting Notes section)
- If action items relate to a specific project, suggest updating that project file
- Report the structured output and file location to the user
