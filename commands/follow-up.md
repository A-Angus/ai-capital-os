---
description: "Track commitments, promises, and follow-ups. Add, list, complete, or get reminders for everything you've promised."
argument-hint: "[add|list|done|remind|nudge] [details]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, TodoWrite]
---

# Follow-Up Tracker

The user wants to manage their follow-ups and commitments.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments

Determine the action from $ARGUMENTS:

| First Word | Action | What Happens |
|-----------|--------|-------------|
| `add` or commitment language | ADD | Add a new follow-up |
| `list` or `show` or `pending` | LIST | Show all pending follow-ups |
| `done` or `complete` or `finished` | DONE | Mark a follow-up as completed |
| `remind` or `check` or `overdue` | REMIND | Show what's due/overdue with suggested actions |
| `nudge` | NUDGE | Draft a follow-up message for an overdue item |
| (no action word, but describes a commitment) | ADD | Treat as adding a new follow-up |
| (no arguments at all) | LIST | Default to showing the full list |

### Step 1: Ensure Data File Exists

Check if `brain/pipeline/follow-ups.md` exists.
- If it does: Read it.
- If it does not: Create `brain/pipeline/` directory and initialize the file with the template:

```markdown
# Follow-Up Tracker
> **Last Updated:** [today's date]
> **Open Items:** 0
> **Overdue:** 0

---

## Pending Follow-Ups

| # | Due | Person | Commitment | Context | Priority | Added |
|---|-----|--------|-----------|---------|----------|-------|

## Waiting On (Others Owe You)

| # | Expected | Person | What They Owe | Context | Last Nudge | Added |
|---|----------|--------|--------------|---------|------------|-------|

## Completed (Last 30 Days)

| # | Completed | Person | Commitment | Original Due |
|---|-----------|--------|-----------|-------------|

---
*Use /follow-up add, /follow-up list, /follow-up done, or /follow-up remind*
```

### Step 2: Execute the Action

---

#### If ADD:

1. Parse from the user's natural language:
   - **Who** — Person involved (or "Self" for personal tasks)
   - **What** — The specific commitment
   - **When** — Due date (parse: "by Friday", "next week", "March 10", "in 3 days", "end of month")
   - **Context** — Background (optional)
   - **Priority** — 🔴 High (revenue, relationships, hard deadlines), 🟡 Medium (important but flexible), 🟢 Low (nice to have)
   - **Direction** — Is this something YOU owe (Pending) or something someone OWES YOU (Waiting On)?

2. If no due date given, default to 3 business days and confirm.

3. Check for duplicates (same person + similar description). If found, ask before creating.

4. Assign the next sequential number.

5. Add to the correct table in the follow-ups file.

6. Update the header counts.

7. Confirm with summary.

---

#### If LIST:

1. Read the follow-ups file.

2. Calculate overdue items (due date < today).

3. Display in priority order:

```
FOLLOW-UP STATUS — [Today's Date]
═══════════════════════════════════

OVERDUE (Action Required)
─────────────────────────
🚨 #[N] [Person] — [What] — was due [date] ([X days ago])

DUE TODAY
─────────
⚡ #[N] [Person] — [What]

DUE THIS WEEK
─────────────
📅 #[N] [Date] — [Person] — [What]

DUE LATER
─────────
📌 #[N] [Date] — [Person] — [What]

WAITING ON OTHERS
─────────────────
⏳ #[N] [Person] — [What] — expected [date]

Open: [X] | Overdue: [X] | Waiting on: [X]
```

---

#### If DONE:

1. Identify which follow-up to complete:
   - By number: "done 3" or "done #3"
   - By person: "done John" or "finished the John thing"
   - By description: "sent the proposal" matches "Send proposal to John"

2. If ambiguous, show numbered list and ask which one.

3. Move item from Pending/Waiting On to Completed table.

4. Add today's date as completion date.

5. Update header counts.

6. Remove completed items older than 30 days from the Completed section.

7. Confirm: "Marked as done: [summary]. [X] items remaining."

---

#### If REMIND:

1. Read follow-ups file and categorize:
   - Overdue (past due date)
   - Due today
   - Due this week
   - Waiting On items that are past expected date

2. For overdue items, suggest specific actions:
   - "This is [X] days overdue. Should I draft a message, reschedule, or mark done?"

3. For overdue Waiting On items, offer to draft a nudge:
   - "[Person] is [X] days late on [item]. Want me to draft a reminder?"

4. If nothing is due: "All clear. Your next follow-up is [item] due on [date]."

---

#### If NUDGE:

1. Identify the person and item to follow up on.

2. Draft a professional follow-up message:
   - Subject line (if email)
   - Body: Brief, respectful, direct. Clear ask. Specific deadline.
   - Tone: "Checking in on..." not "You haven't..."

3. Present draft for user approval.

4. Update "Last Nudge" date in the Waiting On table.

---

### Step 3: Update File

After any action that modifies data:
1. Update the `Last Updated` date in the header.
2. Recalculate and update `Open Items` and `Overdue` counts.
3. Write changes back to `brain/pipeline/follow-ups.md`.

### Step 4: Suggest Next Action

After completing the requested action, suggest what might help:
- After ADD: "Anything else to track, or want to see the full list?"
- After LIST: "Want to mark any of these done, or draft a nudge for overdue items?"
- After DONE: "[X] items left. Next due: [item] on [date]."
- After REMIND: "Want me to draft nudge messages for the overdue items?"
- After NUDGE: "Draft ready. Want to adjust the tone or send as-is?"