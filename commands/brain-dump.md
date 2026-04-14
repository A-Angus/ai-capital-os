---
description: "Quick capture any idea, note, or info — AI automatically files it in the right brain/ location."
argument-hint: "[text to capture] [--category goals|projects|people|research|sops|daily]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, TodoWrite]
---

# Brain Dump

The user wants to quickly capture information and have AI automatically file it in the correct location within `~/.claude/brain/`.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract the content to capture from $ARGUMENTS
- Check for optional `--category` flag to override auto-detection
- If no arguments provided, ask the user what they want to capture

### Step 1: Classify the Content
Analyze the content and determine which brain/ location it belongs in:

| Content Type | Destination |
|-------------|-------------|
| Goal, priority, or milestone | `brain/goals.md` (append to relevant section) |
| New project or project update | `brain/projects/` (new file or update existing) |
| Person/contact info | `brain/people/` (new file from template or update) |
| Process/workflow | `brain/sops/` (new SOP from template) |
| Research finding | `brain/research/` (new file or append) |
| Idea, thought, random note | `brain/daily/YYYY-MM-DD.md` (append to today's log) |
| Deal info | `brain/deal-packages/` or `brain/projects/` |
| Knowledge/reference | `brain/knowledge-base/` (appropriate subfolder) |

### Step 2: Read the Target File
- If appending to an existing file, read it first to understand structure
- If creating a new file, read the relevant `_TEMPLATE.md` for format

### Step 3: Write the Content
- Format the captured info to match the target file's structure
- Include a timestamp: `<!-- Brain dump: YYYY-MM-DD HH:MM -->`
- If creating a new file, use kebab-case naming convention
- If updating an index (README.md), add the new entry

### Step 4: Update Daily Log
- Always append a one-line summary to `brain/daily/YYYY-MM-DD.md`
- Format: `- **Brain dump:** [summary of what was captured and where it was filed]`
- Create today's daily log if it doesn't exist

### Step 5: Confirm
Report back to the user:
- What was captured
- Where it was filed
- Any follow-up actions suggested (e.g., "This sounds like a new project — want me to create a full project file?")
