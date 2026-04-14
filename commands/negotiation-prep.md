---
description: "Build a complete negotiation strategy — counterparty research, BATNA analysis, leverage points, positions, objection scripts, and conversation flow."
argument-hint: "[counterparty name] [context of negotiation]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebSearch, TodoWrite]
---

# Negotiation Prep

The user wants to prepare a comprehensive negotiation strategy.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract counterparty name from $ARGUMENTS
- Extract negotiation context (what's at stake, terms, etc.)
- If arguments are incomplete, ask for:
  1. Who are you negotiating with? (name, company, role)
  2. What's at stake? (price, terms, contract, partnership)
  3. What's your ideal outcome? (best case)
  4. What's your walk-away point? (minimum acceptable)
  5. When is this happening? (date if known)
  6. One-time deal or ongoing relationship?

### Step 1: Research

**Check the brain first:**
- Search `brain/people/` for any file on the counterparty
- Search `brain/research/` for relevant market data or previous negotiation preps
- Check `brain/daily/` for any notes about this person or deal

**Web research (if available):**
- Search for counterparty's company, role, recent news
- Research industry-standard terms/pricing for this type of deal
- Look for leverage indicators (funding, layoffs, expansion, market pressure)

**If no web search:** Work with user-provided info. Note what additional research would help.

### Step 2: Build BATNA Analysis

Analyze both sides:

**User's BATNA:**
- What happens if no deal?
- What are the alternatives?
- How strong is the user's position without this deal?

**Counterparty's BATNA:**
- What are their alternatives?
- How easily can they replace what the user offers?
- What's their time pressure?

Determine: Who needs this deal more?

### Step 3: Map Leverage

Identify leverage across 7 dimensions:
1. Information edge
2. Time pressure
3. Alternative options
4. Expertise/unique value
5. Relationship/trust
6. Market conditions
7. Scarcity of what each side controls

### Step 4: Define Positions

Calculate three positions:
- **Opening (Ambitious):** First offer. Aggressive but defensible. Leaves room to move.
- **Target (Realistic):** Where the user actually wants to land.
- **Walk-Away (Floor):** Absolute minimum. Below this, user walks.

For each: specific terms, supporting rationale, and framing language.

### Step 5: Predict Objections & Write Scripts

Identify top 5-10 likely objections. For each:
- Their exact words (predicted)
- The underlying concern driving the objection
- Word-for-word response script
- Redirect question to move forward

### Step 6: Design Conversation Flow

Map the negotiation structure:
1. Opening — set tone, frame discussion
2. Information gathering — strategic questions
3. Present position — anchor with opening offer
4. Handle pushback — concession strategy with trade rules
5. Close — summarize terms, lock in writing
6. If stalled — deadlock breakers and tabling strategy

### Step 7: Compile & Save

Generate the full negotiation prep document including:
- Executive summary
- Counterparty profile
- BATNA analysis
- Leverage map
- Three positions with rationale
- Concession strategy (what to give, in what order, what to get back)
- Objection scripts
- Conversation flow with timing
- Do's, Don'ts, and Wild Cards

Save to: `brain/research/negotiation-prep-{counterparty-slug}-{YYYY-MM-DD}.md`

### Step 8: Deliver Summary

Print a concise summary to terminal:
- Your opening position and how to frame it
- The #1 leverage point to emphasize
- The most likely objection and your best response
- The walk-away trigger and exit script

Then: "Full strategy saved to brain/research/negotiation-prep-{name}-{date}.md — review it before the meeting and practice the scripts out loud."