---
description: "Draft personalized seller outreach — letters, texts, emails, and phone scripts for motivated seller leads."
argument-hint: "[seller name] [property/vehicle details] [--method letter|text|email|script|all] [--motivation distressed|divorce|relocation|tired-landlord|inherited|pre-foreclosure]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebSearch, TodoWrite]
---

# Seller Outreach Drafter

The user wants to create personalized outreach materials to contact a motivated seller — customized by their situation and the best contact method.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract seller name (if known)
- Extract property or vehicle details
- `--method` — outreach format (default: all)
- `--motivation` — seller's likely motivation/situation
- If no details provided, ask for: seller name, what they're selling, and any known motivation

### Step 1: Load Context
- Read `~/.claude/brain/knowledge-base/mike-davis/02-brand-voice-and-philosophy.md` for tone
- Read `~/.claude/brain/knowledge-base/top-method/01-what-is-the-top-method.md` for value prop
- Check `~/.claude/brain/people/` for any existing relationship with this seller
- If property, search for basic property data to personalize the outreach

### Step 2: Identify the Angle
Based on the seller's motivation, choose the right emotional angle:

| Motivation | Angle | Key Message |
|-----------|-------|-------------|
| Distressed | Relief | "I can take this off your plate" |
| Divorce | Speed + Discretion | "Quick, clean, no hassle" |
| Relocation | Convenience | "Sell without being here" |
| Tired Landlord | Freedom | "Stop dealing with tenants" |
| Inherited | Simplicity | "Turn this into cash without the headache" |
| Pre-Foreclosure | Urgency + Empathy | "There are options — let's talk before the bank does" |
| Generic | Curiosity + Value | "I have buyers looking in your area" |

### Step 3: Draft Direct Mail Letter

```markdown
## Direct Mail Letter

[Seller Name]
[Address]

Dear [First Name],

[Personalized opening — reference their specific situation or property]

[Value proposition — what you can do for them, not what you want from them]

[Brief credibility — who you are, why you're different]

[Call to action — one clear next step]

[Sign-off]

Mike Davis
TOP Wheels | SellFi
[Phone] | [Email]
```

Key rules:
- Handwritten feel (short paragraphs, conversational)
- Lead with THEIR problem, not your offer
- One clear CTA
- Under 200 words

### Step 4: Draft Text Message
Create 2-3 text variations:
- **Version A (Direct):** "[Name], I'm reaching out about [property/vehicle]. I work with buyers in [area] and wanted to see if you'd consider an offer. No pressure — just a conversation. — Mike"
- **Version B (Curiosity):** "Hey [Name], quick question about [address/vehicle] — is that something you'd ever consider selling? I may have a buyer. — Mike"
- **Version C (Value-First):** "[Name], I help people in [situation] get their [property/vehicle] sold fast without the hassle of traditional listings. Worth a 5-min call? — Mike"

All under 160 characters where possible, max 300.

### Step 5: Draft Email
- 3 subject line options
- Personalized email body (under 150 words)
- Professional but warm tone
- Clear CTA
- Follow-up email for 3 days later (if no response)

### Step 6: Draft Phone Script

```markdown
## Phone Script

**Opening (10 sec):**
"Hi [Name], this is Mike Davis. I'm reaching out because [reason — reference their property/situation]. Do you have 2 minutes?"

**If Yes — Value Prop (20 sec):**
"I work with buyers who are specifically looking for [type of property/vehicle] in [area]. I wanted to see if selling is something you've thought about, even casually."

**Handle Objection:**
- "Not interested" → "Totally understand. If anything changes, you've got my number. What would make it worth considering?"
- "What's your offer?" → "I don't throw out blind numbers. I'd want to see it and give you something fair. Can we set up a quick look?"
- "I'm working with an agent" → "No problem. If that doesn't work out, keep me in mind. I can often close faster with fewer headaches."

**Close:**
"Would [day] at [time] work for a quick 10-minute chat? No pressure, just want to see if there's a fit."
```

### Step 7: Save Materials
- Save to `~/.claude/brain/deal-packages/[seller-slug]/outreach/`
- Files: `letter.md`, `texts.md`, `email.md`, `phone-script.md`
- Log outreach in pipeline if lead-tracker is set up

### Step 8: Report
- Display all outreach materials
- Recommend which method to use first based on the situation
- Suggest follow-up timing (text day 1, call day 3, letter day 5)
