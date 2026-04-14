---
description: "Build a complete pre-meeting intelligence brief — person/company research, agenda, talking points, objection handling, and follow-up templates."
argument-hint: "[person/company] [topic] [--date YYYY-MM-DD] [--type pitch|negotiation|intro|partnership|client|internal]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch, TodoWrite]
---

# Meeting Prep

The user wants to prepare for an upcoming meeting, call, or conversation with thorough intelligence and structure.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract the person or company name
- Extract the meeting topic or purpose
- `--date` — meeting date (default: tomorrow or next business day)
- `--type` — meeting type: pitch, negotiation, intro, partnership, client, internal (auto-detected if not provided)
- If no person/company specified, ask: "Who is the meeting with?"
- If no topic specified, ask: "What is the meeting about?"

### Step 1: Internal Research
- Check `~/.claude/brain/people/` for existing contact file on the person
- Check `~/.claude/brain/projects/` for shared projects or active deals
- Check `~/.claude/brain/daily/` for recent mentions or interactions
- Check `~/.claude/brain/research/` for prior research on this person/company
- Read `~/.claude/brain/goals.md` for context on current priorities (useful for framing the meeting)

### Step 2: External Research
Research the person and their company:
- **Person:** Name + title, career background, recent activity, content they have published, social profiles
- **Company:** What they do, size, funding, recent news, competitive landscape
- **Mutual connections:** Anyone in brain/people/ connected to them
- **Signals:** Hiring activity (growth), recent launches, press mentions, podcast appearances
- Use WebSearch for all external lookups. Use WebFetch on their company website or LinkedIn if needed.

### Step 3: Build Intelligence Profile
Compile a concise dossier:
- Name, title, company, role
- Background and career trajectory
- Communication style (inferred from content/public presence)
- What they care about (priorities, pain points, goals)
- Recent activity (last 3-6 months)
- Mutual connections from the brain

### Step 4: Construct Agenda
Build a meeting-type-appropriate agenda:
- **Opening** — rapport builder + frame setter
- **Discovery** — questions to understand their situation
- **Core discussion** — key points with supporting evidence
- **Handling concerns** — space for anticipated pushback
- **Next steps & close** — specific proposed outcome

### Step 5: Develop Talking Points
For each agenda section:
- Key message (one sentence)
- Supporting evidence (data, example, anecdote)
- 5 strategic questions to ask them
- Power phrases that position the user well

### Step 6: Anticipate Objections
Identify 3-5 most likely objections based on meeting type:
- The objection (what they will say)
- Why they might say it (root cause)
- Prepared response (non-defensive, addresses the concern)
- Pivot (how to redirect productively)

### Step 7: Create Follow-Up Templates
Generate 3 post-meeting email templates:
- **Meeting went well** — accelerate next steps
- **Meeting was lukewarm** — add value, keep the door open
- **Meeting went poorly** — leave a professional impression

### Step 8: Save and Report
- Compile everything into a single brief
- Save to `~/.claude/brain/research/meeting-prep-{person-slug}-{YYYY-MM-DD}.md`
- Present: intelligence profile summary, proposed agenda, top 3 talking points, #1 objection to prepare for
- Remind the user to update brain/people/ after the meeting