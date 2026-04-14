---
description: "Create a Standard Operating Procedure from a process description — structured, repeatable, AI-executable."
argument-hint: "[process name or description] [--category deals|marketing|sales|operations|tech|training]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, TodoWrite]
---

# SOP Builder

The user wants to turn a process description (or brain dump about how something works) into a structured, repeatable SOP that AI can follow autonomously.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract the process name or description
- `--category` — SOP category (default: auto-detect)
- If only a name is given, ask the user to describe the process step by step
- If a brain dump is provided, parse it into structured steps

### Step 1: Load the SOP Template
- Read `~/.claude/brain/sops/_TEMPLATE.md` for the standard format
- Read `~/.claude/brain/sops/README.md` to understand existing SOPs and avoid duplicates

### Step 2: Structure the Process
Break the user's description into:
- **Trigger:** What kicks off this process?
- **Prerequisites:** What needs to be true before starting?
- **Steps:** Numbered, specific, actionable steps
- **Decision Points:** Any if/then branches in the process
- **Tools/Systems:** What tools or platforms are involved?
- **Output:** What's the deliverable or end state?
- **Handoff:** Who/what takes over after this SOP completes?

### Step 3: Write the SOP

```markdown
# SOP: [Process Name]

> **Category:** [category]
> **Owner:** [who owns this process]
> **Created:** YYYY-MM-DD
> **Status:** Active

## Purpose
[One sentence: what this SOP accomplishes]

## Trigger
[What event or request kicks off this process]

## Prerequisites
- [ ] [Required before starting]

## Steps

### Step 1: [Action]
**Who:** [person or AI]
**Tool:** [system/tool used]
**Action:** [specific instructions]
**Output:** [what this step produces]

### Step 2: [Action]
...

## Decision Points
- **If [condition]:** → [do this]
- **If [other condition]:** → [do that]

## Tools & Access Required
| Tool | Access Level | Notes |
|------|-------------|-------|
| [tool] | [level] | [notes] |

## Common Issues & Fixes
| Issue | Fix |
|-------|-----|
| [problem] | [solution] |

## Metrics / Success Criteria
- [How you know this was done right]
```

### Step 4: Save the SOP
- Save to `~/.claude/brain/sops/[kebab-case-name].md`
- Update `~/.claude/brain/sops/README.md` index table with the new entry

### Step 5: Report
- Show the user the completed SOP
- Confirm it's saved and indexed
- Ask if any steps need refinement or if there are edge cases to add
