---
description: "Research competitors for a business or product — pricing, features, positioning, strengths, weaknesses, and opportunities."
argument-hint: "[business/product name] [--industry sector] [--competitors name1,name2,name3]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch, TodoWrite]
---

# Competitor Analysis

The user wants a competitive intelligence report for a specific business, product, or market.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract the business or product to analyze
- `--industry` — sector/vertical to focus on (auto-detected if not provided)
- `--competitors` — specific competitors to include (AI will also discover others)
- If no arguments provided, ask what business/product to analyze

### Step 1: Load Existing Intel
- Check `~/.claude/brain/research/competitor-intelligence.md` for prior research
- Check `~/.claude/brain/knowledge-base/` for relevant domain knowledge
- Avoid duplicating work already done

### Step 2: Identify Competitors
- Search for direct competitors (same product/service, same market)
- Search for indirect competitors (different approach, same customer problem)
- Search for emerging/disruptive competitors (new entrants, adjacent markets)
- Aim for 5-10 competitors total

### Step 3: Research Each Competitor
For each competitor, gather:
- **Company:** Name, founded, size, funding, location
- **Product:** Core offering, features, unique selling proposition
- **Pricing:** Plans, tiers, free trial, enterprise pricing
- **Positioning:** Tagline, target market, brand voice
- **Traction:** User count, revenue (if public), growth signals, social following
- **Strengths:** What they do well
- **Weaknesses:** Gaps, complaints, negative reviews
- **Tech Stack:** Platform, integrations, mobile apps (if relevant)

### Step 4: Build Comparison Matrix
Create a feature/capability comparison table:

| Feature | Our Product | Competitor A | Competitor B | Competitor C |
|---------|------------|-------------|-------------|-------------|
| Feature 1 | Yes/No | Yes/No | Yes/No | Yes/No |
...

### Step 5: SWOT Analysis
For the user's business relative to the competitive landscape:
- **Strengths** — Where we win
- **Weaknesses** — Where we're behind
- **Opportunities** — Gaps no one is filling
- **Threats** — Risks from competitors

### Step 6: Strategic Recommendations
- Top 3 differentiation opportunities
- Pricing positioning recommendation
- Feature gaps to prioritize
- Marketing angles competitors are missing

### Step 7: Save Report
- Save to `~/.claude/brain/research/competitor-analysis-[topic-slug]-YYYY-MM-DD.md`
- Report key findings and the file location to the user
