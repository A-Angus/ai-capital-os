---
description: "Set up a new client — creates 5 files: contact record, project file, welcome email draft, onboarding checklist, and kickoff meeting agenda."
argument-hint: "[client name] [--type consulting|tc|buyer|seller|partner|student] [--company name] [--email address] [--phone number] [--service description] [--value amount]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, TodoWrite]
---

# Client Onboarding

The user wants to fully onboard a new client — create all 5 necessary files, update indexes, and set up tracking.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract client name (required — ask if missing)
- `--type` — client type: consulting, tc, buyer, seller, partner, student
- `--company` — company or entity name
- `--email` — email address
- `--phone` — phone number
- `--service` — description of the engagement/service
- `--value` — dollar value of the engagement
- If name not provided, ask for it along with engagement type
- If engagement type not provided, ask: "What type of work are you doing for this client?"

### Step 1: Check for Existing Records
- Search `brain/people/` for a file matching the client name
  - If found, inform user: "A contact entry already exists for {name}. I'll update it with the new client engagement instead of creating a duplicate."
  - If not found, proceed with new file creation
- Check `brain/projects/` for a file with a matching client slug
  - If found, use a date or number suffix for the new project file

### Step 2: Create File 1 — Contact Record
- Path: `brain/people/{firstname-lastname}.md`
- Use the template from the SKILL.md (full contact record with relationship context)
- Fill in all known details from arguments
- Mark missing fields as "TBD"
- Set Role: Client, Status: Active, Priority: High
- Add "Linked Files" section pointing to the project file and invoice folder
- Update `brain/people/README.md` index to include the new contact

### Step 3: Create File 2 — Project File
- Path: `brain/projects/{client-slug}-{engagement-type}.md`
- Use the template from the SKILL.md (scope, milestones, tasks)
- Link back to the contact file
- Set Status: In Progress, Priority: High
- Add initial milestones: Onboarding complete, first deliverable, etc.
- Add initial tasks from the checklist
- Update `brain/projects/README.md` dashboard to include the new project

### Step 4: Create File 3 — Welcome Email Draft
- Path: `brain/drafts/welcome-{client-slug}.md`
- Read CLAUDE.md for brand voice and user info (name, company, contact details)
  - If CLAUDE.md not available, use professional default tone
- Personalize to the client type and engagement
- Include: greeting, what to expect, next steps (kickoff call, info needed, communication plan, timeline)
- Sign off with user's name, title, and contact info from CLAUDE.md
- Create `brain/drafts/` directory if it does not exist

### Step 5: Create File 4 — Onboarding Checklist
- Path: `brain/projects/{client-slug}-onboarding-checklist.md`
- Include three sections: Pre-Kickoff, During Kickoff, Post-Kickoff
- Universal items:
  - [ ] Contact entry created in brain/people/
  - [ ] Project file created in brain/projects/
  - [ ] Contract signed
  - [ ] Payment received
  - [ ] Access granted
  - [ ] Kickoff call scheduled
  - [ ] Welcome email sent
  - [ ] Intro email sent
- Add engagement-specific items based on client type:
  - **TC Client:** collect vehicle info, verify titles, confirm buyer details, TC agreement signed
  - **Buyer:** collect buyer criteria, pre-qualification, match with inventory
  - **Seller:** collect property/vehicle details, pricing agreement, marketing materials, agreement sent
  - **Consulting:** define deliverables, set meeting cadence, establish reporting format
  - **Partner:** define partnership terms, revenue split documented, joint marketing plan
  - **Student:** enrollment confirmed, course access granted, orientation scheduled
- Mark the first two items as [x] complete (since we just created them)

### Step 6: Create File 5 — Kickoff Meeting Agenda
- Path: `brain/drafts/kickoff-agenda-{client-slug}.md`
- Structured 30-60 minute agenda:
  1. Introductions and Context (5 min)
  2. Goals and Expectations (10 min)
  3. Scope and Deliverables (10 min)
  4. Process and Communication (10 min)
  5. Information and Access Needed (10 min)
  6. Next Steps (5 min)
- Include post-meeting action items template
- Customize sections based on engagement type

### Step 7: Cross-Link Everything
- Contact file links to project file and invoice folder
- Project file links to contact file
- Checklist references all file paths
- All files use consistent client slug naming

### Step 8: Report What Was Created
Present a clear summary:

```
CLIENT ONBOARDING COMPLETE — {Client Name}
============================================

Files Created:
  1. Contact:   brain/people/{firstname-lastname}.md
  2. Project:   brain/projects/{client-slug}-{type}.md
  3. Checklist: brain/projects/{client-slug}-onboarding-checklist.md
  4. Welcome:   brain/drafts/welcome-{client-slug}.md
  5. Agenda:    brain/drafts/kickoff-agenda-{client-slug}.md

Indexes Updated:
  - brain/people/README.md
  - brain/projects/README.md

Next Steps:
  1. Review and send the welcome email
  2. Schedule the kickoff call
  3. Collect required info from the client
  4. Work through the onboarding checklist
```
