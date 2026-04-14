---
description: "Comprehensive personal or business brand audit — social presence, content strategy, positioning, gap analysis, 30-day improvement plan, content pillars, and bio/tagline suggestions."
argument-hint: "[name-or-handles] [--website url] [--platforms instagram,twitter,linkedin] [--industry niche]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch, TodoWrite]
---

# Personal Brand Audit

The user wants a comprehensive analysis of their personal or business brand across digital channels.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract the person/brand name or social media handles
- `--website` — website URL to audit
- `--platforms` — specific platforms to focus on (default: all discoverable)
- `--industry` — niche/industry for competitive comparison (auto-detected if not provided)
- If no handles or name provided, ask: "Who or what am I auditing? Give me a name, social handles, or website URL."

### Step 1: Load Internal Context
- Check `~/.claude/brain/knowledge-base/` for existing brand voice or identity files
- Check `~/.claude/brain/goals.md` for business objectives (brand should serve these)
- Check `~/.claude/brain/research/` for prior brand or competitor research
- Check `~/.claude/brain/projects/` for brand-related projects

### Step 2: Audit Digital Presence
Research and evaluate each channel:

**Website:**
- Messaging clarity, value proposition, CTA strength, overall impression
- Score 1-10

**Social Media (for each active platform):**
- Profile setup (photo, bio, handle consistency, link)
- Content quality and visual consistency
- Posting frequency and consistency
- Engagement rate (relative to follower count)
- Content mix (educational vs. promotional vs. personal)
- Calls to action effectiveness
- Score 1-10 per platform

**Google Search:**
- What appears when you search the name/brand
- Digital first impression assessment
- Score 1-10

### Step 3: Build Brand Snapshot
- Overall brand score (X/100)
- Brand identity summary (message, value prop, audience, visual identity, tone, credibility, differentiation)
- Platform overview table with scores and top issues

### Step 4: Gap Analysis
- Compare where the brand IS vs. where it NEEDS to be (based on goals)
- Score 7 dimensions: authority, visibility, trust, clarity, consistency, engagement, conversion
- Rank top 5 gaps by business impact

### Step 5: Competitive Positioning
- Identify 3-5 competitors in the same personal brand space
- Compare: platform focus, positioning, audience size, strengths, user's edge
- Create a positioning map
- Recommend positioning strategy

### Step 6: Build 30-Day Improvement Plan
- Week 1: Foundation (fix bios, photos, pinned content)
- Week 2: Content consistency (start posting on pillars)
- Week 3: Authority building (longer content, engagement, outreach)
- Week 4: Optimize and scale (double down on what works)
- Total time: 30-45 min/day

### Step 7: Content Pillar Recommendations
- 3-5 core content pillars tied to business goals
- For each: why it matters, content types, 3 example post ideas
- Recommended content mix ratio

### Step 8: Bio & Tagline Suggestions
- 3 universal bio options (authority-led, value-led, story-led)
- Platform-specific bio versions (Instagram, Twitter/X, LinkedIn, TikTok)
- 5 tagline options

### Step 9: Save and Report
- Save to `~/.claude/brain/research/brand-audit-{YYYY-MM-DD}.md`
- Create brain/research/ if it does not exist
- Present: overall score, top 3 gaps, positioning recommendation, Week 1 priorities, top bio/tagline
- Recommend quarterly re-audit