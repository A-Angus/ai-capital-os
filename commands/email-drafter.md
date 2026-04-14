---
description: "Draft professional emails — cold outreach, follow-ups, proposals, introductions, or any business email."
argument-hint: "[type: cold|follow-up|proposal|intro|thank-you|negotiation] [context/details] [--to recipient] [--tone formal|casual|bold]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebSearch, TodoWrite]
---

# Email Drafter

The user wants to draft a professional email for a specific purpose and recipient.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract the email type (cold, follow-up, proposal, intro, thank-you, negotiation)
- Extract context/details about the situation
- `--to` — recipient name (check brain/people/ for context)
- `--tone` — writing tone (default: bold, direct — Mike's style)
- If insufficient context, ask for: recipient, purpose, key points to hit, desired outcome

### Step 1: Load Context
- Check `~/.claude/brain/people/` for recipient info (relationship, prior interactions)
- Read `~/.claude/brain/knowledge-base/mike-davis/02-brand-voice-and-philosophy.md` for tone
- If related to a deal or project, load relevant project files for context

### Step 2: Draft the Email
Structure based on email type:

**Cold Outreach:**
- Subject line (curiosity-driven, under 50 chars)
- Personal hook (why you're reaching out to THEM specifically)
- Value prop (what's in it for them, 1-2 sentences)
- Social proof (brief credibility)
- CTA (one clear ask)
- Keep under 150 words

**Follow-Up:**
- Reference prior interaction
- Add new value or context
- Restate the ask
- Keep shorter than original

**Proposal:**
- Context recap
- What you're proposing (clear, structured)
- Terms/pricing if applicable
- Next steps
- Timeline

**Introduction:**
- Why you're connecting these two people
- Brief context on each person
- Suggested next step

**Negotiation:**
- Acknowledge their position
- Present your counter with reasoning
- Find middle ground
- Clear next step

### Step 3: Generate Variants
- Draft 2 versions: one concise, one with more detail
- Include 3 subject line options
- Note which version is recommended and why

### Step 4: Present to User
- Show the drafted email(s) in clean format
- Include subject line options
- Note any suggested attachments or follow-up timing
- Offer to adjust tone, length, or angle
