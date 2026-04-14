---
description: "Build a complete hiring package — job description, ideal candidate profile, screening questions, interview scorecard, red/green flags, offer letter template, and onboarding checklist."
argument-hint: "[role description] [--type fulltime|parttime|contract|freelance] [--remote yes|no|hybrid] [--budget salary-range]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch, TodoWrite]
---

# Hiring Screener

The user wants to build a complete hiring workflow for a specific role.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract the role title and description
- `--type` — employment type: fulltime, parttime, contract, freelance (default: fulltime)
- `--remote` — remote, on-site, or hybrid (default: remote)
- `--budget` — salary or hourly rate range (optional, will research market rates if not provided)
- If no role description provided, ask: "What role are you hiring for? Give me a title and what they'd do."

### Step 1: Load Context
- Check `~/.claude/brain/goals.md` for business context and priorities
- Check `~/.claude/brain/projects/` for relevant projects the hire might work on
- Check `~/.claude/brain/knowledge-base/` for industry context
- If salary not provided, search market rates for the role via WebSearch

### Step 2: Generate Job Description
Structure:
- About the company (from brain context or user input)
- The role — why it exists, what success looks like
- Responsibilities — 6-8 action-verb, outcome-oriented items
- Requirements — split into Required and Nice-to-Have
- What we offer — compensation, benefits, growth
- How to apply — clear instructions

### Step 3: Build Ideal Candidate Profile
- Background and career trajectory
- Mindset and work style
- Hard skills (testable) and soft skills (observable)
- Non-negotiables and bonus points

### Step 4: Create 10 Screening Questions
Across four categories:
- **Experience** (3 questions) — Do they have the skills?
- **Situational** (3 questions) — Can they think on their feet?
- **Behavioral** (2 questions) — How have they actually performed?
- **Culture Fit** (2 questions) — Will they thrive here?
- Each question includes: what a great answer sounds like + red flag answer
- Plus 1 bonus differentiator question

### Step 5: Build Interview Scorecard
- 8 criteria scored 1-5
- Total and average scoring
- Hire / No Hire recommendation checkboxes
- Free-form notes section

### Step 6: Define Red and Green Flags
- 7 green flags with explanations
- 7 red flags with explanations
- 3 immediate disqualifiers

### Step 7: Create Offer Letter Template
- Position details (title, start date, type, location, compensation)
- Benefits and conditions
- Acceptance signature block
- Legal disclaimer about jurisdiction review

### Step 8: Build Onboarding Checklist
- Before Day 1 — admin prep
- Day 1 — welcome and orientation
- Week 1 — getting up to speed with daily check-ins
- Days 8-30 — ramp-up with weekly 1:1s
- Day 30 — performance check
- Day 60-90 — full integration and quarterly goal setting

### Step 9: Save and Report
- Save to `~/.claude/brain/drafts/hiring-{role-slug}-{YYYY-MM-DD}.md`
- Create brain/drafts/ if it does not exist
- Present: job description, ideal candidate summary, top 3 screening questions, key red/green flags
- Offer to adjust tone for specific job boards (LinkedIn, Indeed, freelancer platforms)