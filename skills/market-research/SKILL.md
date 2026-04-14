---
name: market-research
description: This skill should be used when the user asks to "research a market", "market research", "market size", "TAM SAM SOM", "total addressable market", "industry analysis", "industry research", "market trends", "market opportunity", "competitive landscape", "market growth rate", "industry size", "niche research", "sector analysis", "opportunity analysis", "who are the key players in", "how big is the market for", "is there a market for", "market validation", "industry report", "trend analysis", "market overview", "growth rate for", "market potential", or anything related to researching market size, trends, competitors, and opportunities for any industry, niche, product, or service.
version: 1.0.0
---

# Market Research

## Overview

Conducts comprehensive market research for any industry, niche, product, or service. Uses live web search to pull current data, then synthesizes findings into a structured report covering market size (TAM/SAM/SOM), trends, growth rates, key players, opportunities, and threats. Designed to give the user a clear picture of market dynamics for decision-making.

## When This Skill Applies

- User asks about the size of any market or industry
- User wants TAM/SAM/SOM analysis
- User asks "is there a market for X?"
- User wants to understand trends in an industry
- User asks about competitors or key players in a space
- User wants a market overview before launching a product or service
- User asks about growth rates, projections, or forecasts
- User wants opportunity or gap analysis for a niche
- User mentions market validation or feasibility research

## How It Works

### Step 1: Define the Research Scope

Extract from the user's request:

| Parameter | Description | Example |
|-----------|-------------|---------|
| Industry/Niche | What market to research | "Creative finance for vehicles" |
| Geography | Market boundary | US, Global, specific region |
| Timeframe | Analysis period | Current + 5-year forecast |
| Depth | How deep to go | Quick overview vs. deep dive |
| Specific Questions | Anything particular they want answered | "Is there room for a new platform?" |

### Step 2: Conduct Web Research

Run multiple targeted web searches to gather current data:

**Search queries to run (adapt to the specific market):**

1. `"{industry} market size 2025 2026"` — Current market valuation
2. `"{industry} market growth rate CAGR forecast"` — Growth projections
3. `"{industry} industry trends 2026"` — Current and emerging trends
4. `"{industry} key players companies market share"` — Competitive landscape
5. `"{industry} challenges problems pain points"` — Market gaps and opportunities
6. `"{industry} emerging technology disruption"` — Innovation and disruption vectors
7. `"{industry} consumer behavior demographics"` — Buyer/user analysis
8. `"{industry} regulations policy changes 2026"` — Regulatory environment

Run at least 4-6 searches. More for deep dives.

### Step 3: Synthesize Market Size (TAM/SAM/SOM)

Calculate or estimate using data found:

| Metric | Definition | How to Estimate |
|--------|-----------|-----------------|
| **TAM** (Total Addressable Market) | Total revenue opportunity if 100% market share | Industry-wide revenue or volume |
| **SAM** (Serviceable Addressable Market) | Portion of TAM targetable by the user's specific product/model | Filter by geography, segment, channel |
| **SOM** (Serviceable Obtainable Market) | Realistic share capturable in 1-3 years | SAM filtered by competition, resources, reach |

If exact numbers are not available, use triangulation:
- Top-down: Total industry size, filter down
- Bottom-up: Number of potential customers x average revenue per customer
- Comparable: Similar markets or adjacent industries as proxies

Always note confidence level: **High** (multiple sources agree), **Medium** (extrapolated from partial data), **Low** (estimated from limited info).

### Step 4: Analyze Competitive Landscape

For key players found:

| Competitor | What They Do | Est. Revenue/Size | Strengths | Weaknesses |
|-----------|-------------|-------------------|-----------|------------|
| {name} | {description} | {size} | {strengths} | {gaps} |

Identify:
- Market leaders and their market share
- Emerging challengers
- Recent entrants or exits
- Consolidation trends (M&A activity)
- White space where no one is serving well

### Step 5: Identify Trends and Opportunities

Categorize trends:

| Trend Type | Examples |
|-----------|---------|
| Technology | AI adoption, platform shifts, automation |
| Consumer | Behavior changes, preference shifts, demographics |
| Regulatory | New laws, compliance requirements, deregulation |
| Economic | Interest rates, inflation impact, funding environment |
| Competitive | New entrants, consolidation, pricing pressure |

For each trend, assess: **Impact** (high/medium/low) and **Timeline** (happening now / 1-2 years / 3-5 years).

### Step 6: SWOT for Market Entry

If the user is evaluating whether to enter or expand in a market:

| | Positive | Negative |
|---|---------|----------|
| **Internal** | Strengths: What the user brings | Weaknesses: What they lack |
| **External** | Opportunities: Market gaps | Threats: Risks and barriers |

### Step 7: Compile and Save Report

Save the research report to `brain/research/{topic-slug}-market-research.md`.

If `brain/research/` does not exist, create it.

## Output Format

```markdown
# Market Research: {Industry/Niche}

> **Date:** {YYYY-MM-DD}
> **Scope:** {geography, segment}
> **Depth:** {quick overview / deep dive}
> **Confidence Level:** {high / medium / low}

---

## Executive Summary

{3-5 sentence overview of the market, its size, trajectory, and the key takeaway for the user}

---

## Market Size

| Metric | Value | Confidence |
|--------|-------|------------|
| TAM | ${amount} | {high/medium/low} |
| SAM | ${amount} | {high/medium/low} |
| SOM | ${amount} | {high/medium/low} |
| CAGR | {X%} ({period}) | {high/medium/low} |

**Methodology:** {how the numbers were derived — top-down, bottom-up, comparable}

**Sources:** {list key sources and data points used}

---

## Key Trends

### 1. {Trend Name}
- **Impact:** {High/Medium/Low}
- **Timeline:** {Now / 1-2 years / 3-5 years}
- **Details:** {explanation}

### 2. {Trend Name}
{...}

---

## Competitive Landscape

| Player | Description | Est. Size | Market Position |
|--------|------------|-----------|-----------------|
| {name} | {what they do} | {revenue/users} | {leader/challenger/niche} |

### White Space / Gaps
- {gap 1}
- {gap 2}

---

## Opportunities

1. **{Opportunity}** — {description, why it matters, potential size}
2. **{Opportunity}** — {description}

## Threats & Risks

1. **{Risk}** — {description, likelihood, mitigation}
2. **{Risk}** — {description}

---

## SWOT Analysis

| | Favorable | Unfavorable |
|---|----------|-------------|
| **Internal** | {Strengths} | {Weaknesses} |
| **External** | {Opportunities} | {Threats} |

---

## Recommendations

1. {Actionable recommendation based on findings}
2. {Actionable recommendation}
3. {Actionable recommendation}

---

## Sources

- {Source 1 — URL or publication}
- {Source 2}
- {Source 3}

---

*Research conducted {date}. Market data should be refreshed quarterly.*
```

## Example Usage

**User:** "Research the market for creative finance vehicle platforms in the US"

**AI:** Runs 6-8 web searches, finds market size data for auto finance, alternative lending, and vehicle marketplaces. Builds TAM/SAM/SOM estimates, identifies competitors (Carvana, Vroom, traditional dealers, SubTo community), analyzes trends (dealer-to-consumer shift, AI in lending, rising interest rates pushing creative solutions), identifies opportunities (no dominant creative finance platform for vehicles exists). Saves report.

**User:** "How big is the AI SaaS market?"

**AI:** Conducts quick research, provides current market size, growth rates, key players, and emerging trends. Quick overview depth.

**User:** "I want a deep dive on the online education market for real estate investing"

**AI:** Deep dive with multiple searches, detailed competitive analysis (Kajabi, Teachable, Udemy courses, BiggerPockets, SubTo), pricing analysis, student demographics, conversion rates, and specific opportunities for a new entrant.

**User:** "Is there a market for AI-powered business operating systems?"

**AI:** Researches the AI OS / AI assistant market, finds comparables, estimates market size, identifies what exists (Notion AI, various AI agents), and evaluates the opportunity.

## Error Handling

- **If WebSearch is unavailable or returns errors:** Inform the user: "Web search is not available right now. I can provide a market analysis based on my training knowledge, but it will not include the latest data or statistics. Proceed, or try again later?"
- **If web search returns limited data for a niche market:** Use triangulation methods (top-down from broader industry, bottom-up from comparable niches, or proxy data from adjacent markets). Note the confidence level: "Limited direct data available for this niche. Estimates are derived from {method} with {low/medium} confidence. Cross-reference before making major decisions."
- **If the user does not specify a market or industry:** Ask: "What market or industry do you want me to research? Be as specific as possible — 'creative finance for vehicles in the US' is better than 'finance'."
- **If `brain/research/` directory does not exist:** Create it automatically before saving the research report.
- **If a market research file already exists for this topic:** Ask: "A market research report for '{topic}' already exists (dated {date}). Should I refresh it with current data, or create a separate new report?"
- **If TAM/SAM/SOM calculations rely on limited or conflicting data:** Show the calculation methodology, note the confidence level for each estimate, and present ranges rather than single numbers. Flag: "These are estimates based on available data. For precise market sizing, consider commissioning a formal market study."
- **If the user asks for a geography not well-covered by English-language web search:** Note: "Data for {geography} may be limited in English-language sources. Results are based on what I could find. For deeper local market data, consider local language research or regional industry reports."
- **If sources are outdated (only pre-2024 data available):** Flag: "The most recent data I found for this metric is from {year}. Market conditions may have changed. I've noted the data age in the report."
