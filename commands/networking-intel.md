---
description: "Pre-event intelligence — research attendees, build target profiles, create event strategy, and generate follow-up templates."
argument-hint: "[event-name] [attendee-names-or-url] [--goal your-objective] [--follow-up names-met] [--tier1-only]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch, TodoWrite]
---

# Networking Intel

The user wants pre-event intelligence preparation — attendee research, target profiles, event strategy, and/or follow-up templates.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract event name (required — ask if missing)
- Extract attendee info: names listed directly, event URL, or file path to an attendee list
- `--goal` — the user's specific objective for this event (e.g., "find investors", "recruit 5 students", "close deals")
- `--follow-up` — post-event mode: generate follow-up emails for people already met (provide names + context)
- `--tier1-only` — only research and profile the top 3-5 must-meet targets (saves time for quick prep)
- If no attendee info provided, search for the event online and pull public speaker/sponsor lists

### Step 1: Load Context
- Read `brain/goals.md` for current priorities (used to prioritize who to meet)
- Read `brain/people/README.md` for existing contacts (check for mutual connections)
- Read CLAUDE.md or `brain/identity/` for user's business context and elevator pitch
- If the event is tied to a trip, check `brain/research/travel-*.md` for the trip brief

### Step 2: Research Attendees
For each person on the attendee list (or found via event search):
- Search: `"{name}" {company}` for identity confirmation
- Search: `"{name}" LinkedIn` for professional background
- Search: `"{name}" interview OR podcast OR recent` for recent activity
- Cross-reference with `brain/people/` for existing relationships
- Build a target profile: name, title, company, background, notable achievements, recent activity, relevance to user, conversation starters, what they want, how user can help

### Step 3: Prioritize into Tiers
- **Tier 1 (Must Meet, 3-5 people):** Direct goal alignment, decision-maker level, clear mutual value
- **Tier 2 (Should Meet, 5-10 people):** Strong potential, referral sources, influencers
- **Tier 3 (Nice to Meet):** Worth a handshake if opportunity arises
- Ranking based on: alignment with user's stated goal + quarterly goals from goals.md

### Step 4: Generate the Event Brief

**Pre-event mode (default):**

```markdown
# Networking Intel: {Event Name}
> **Date:** {dates} | **Location:** {venue}
> **Your Goal:** {specific mission}
> **Prepared:** {today}

## Target Profiles

### Tier 1 — Must Meet
#### 1. {Name}
| Field | Details |
|-------|---------|
| Title | {title} |
| Company | {company — what they do} |
| Background | {2-3 sentences} |
| Recent Activity | {last 90 days} |
| Relevance | {why they matter for your goal} |
| Mutual Connections | {from brain/people/} |
**Conversation Starters:**
1. "{personalized opener based on their recent work}"
2. "{opener based on mutual interest}"
3. "{opener based on their challenge you can help with}"
**Your Ask:** {specific desired outcome from this meeting}

(repeat for each Tier 1)

### Tier 2 — Should Meet
(same format, slightly condensed)

### Tier 3 — Brief List
| Name | Title | Company | One-Line Relevance |
|------|-------|---------|-------------------|

## Event Strategy
### Mission: {one sentence}
### Arrival: {when and where to position}
### Session Recommendations
| Session | Time | Why | Target |
|---------|------|-----|--------|
### Networking Blocks
| Time | Strategy | Who to Target |
|------|----------|--------------|
### After-Hours
- {after-party intel}
- {where attendees congregate}

## Follow-Up Templates
### Tier 1: {Name}
**Subject:** {personalized subject}
{personalized email body referencing likely conversation}

### Tier 2: General Template
**Subject:** Good to meet you at {event}
{general follow-up body}

### LinkedIn Connection Note
{universal connection request}

## Post-Event Checklist
- [ ] Follow up with Tier 1 within 24 hours
- [ ] Follow up with Tier 2 within 48 hours
- [ ] Connect on LinkedIn within 1 week
- [ ] Add contacts to brain/people/
- [ ] Post event recap on social media
- [ ] Log debrief to brain/daily/
```

**Follow-up mode (--follow-up):**
- Skip the pre-event research and strategy
- Take the names and conversation context the user provides
- Generate highly personalized follow-up emails for each person
- Suggest optimal timing and channel for each follow-up
- Offer to create `brain/people/` entries for each new contact

**Tier 1 only mode (--tier1-only):**
- Research only the top 3-5 targets
- Deep profiles with full conversation prep
- Skip the event strategy, session recommendations, and Tier 2/3

### Step 5: Save and Report
- Display the networking brief in terminal
- Save to `brain/research/networking-{event-slug}-{YYYY-MM-DD}.md`
- If `brain/research/` does not exist, create it
- If follow-up mode created new contacts, offer to save them to `brain/people/`
- Report the file location to the user
