---
description: "Research market size, trends, opportunities, and dynamics for any industry, niche, or product category."
argument-hint: "[market/industry/niche] [--focus size|trends|opportunities|all] [--geography us|global|specific-region]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch, TodoWrite]
---

# Market Research

The user wants to understand the size, dynamics, trends, and opportunities in a specific market.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract the market, industry, or niche to research
- `--focus` — what aspect to emphasize (default: all)
- `--geography` — geographic scope (default: US)
- If no market specified, ask the user

### Step 1: Check Existing Research
- Search `~/.claude/brain/research/` for prior research on this market
- Check `~/.claude/brain/knowledge-base/` for domain knowledge
- Note what's already known vs. what needs fresh research

### Step 2: Market Size Research
Search for and compile:
- **Total Addressable Market (TAM):** Full market size
- **Serviceable Addressable Market (SAM):** Segment you can reach
- **Serviceable Obtainable Market (SOM):** Realistic near-term capture
- **Growth rate:** YoY growth, CAGR
- **Revenue data:** Industry revenue, per-company averages
- Source all numbers with publication dates

### Step 3: Trend Analysis
Research and identify:
- **Macro trends:** Big shifts affecting the market (regulation, tech, demographics)
- **Micro trends:** Emerging patterns within the niche
- **Consumer behavior:** How buyers/users are changing
- **Technology trends:** New tools, platforms, or approaches
- **Pricing trends:** How pricing is evolving

### Step 4: Competitive Landscape Overview
- How many players in this market?
- Who are the top 5-10 by market share?
- Where is consolidation happening?
- What are the barriers to entry?

### Step 5: Opportunity Analysis
- **Underserved segments:** Who's being ignored?
- **Pain points:** What frustrates customers?
- **Gaps:** What's missing from current offerings?
- **Timing:** Why is now the right time?
- **Unfair advantages:** What could give you an edge?

### Step 6: Compile Report

```markdown
# Market Research: [Market/Industry]
> Generated: YYYY-MM-DD | Geography: [scope]

## Executive Summary
[3-5 sentences on the opportunity]

## Market Size
| Metric | Value | Source | Year |
|--------|-------|--------|------|
| TAM | $X | [source] | YYYY |
| SAM | $X | [source] | YYYY |
| Growth Rate | X% | [source] | YYYY |

## Key Trends
1. [Trend + impact]
...

## Competitive Landscape
[Overview + key players table]

## Opportunities
1. [Opportunity + reasoning]
...

## Risks & Challenges
1. [Risk + mitigation]
...

## Recommendation
[What Mike should do with this information]

## Sources
[Numbered list with URLs]
```

### Step 7: Save Report
- Save to `~/.claude/brain/research/market-research-[topic-slug]-YYYY-MM-DD.md`
- Report key findings and file location to the user
