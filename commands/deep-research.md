---
description: "Deep web research on any topic — aggregates sources, extracts key findings, saves structured report to brain/research/."
argument-hint: "[topic or question] [--depth quick|standard|deep] [--save true|false]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch, TodoWrite]
---

# Deep Research

The user wants thorough research on a topic, compiled into a structured report with sources.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract the research topic or question
- `--depth` — how deep to go (default: standard)
  - `quick` — 3-5 searches, 1-page summary
  - `standard` — 8-12 searches, full report with sections
  - `deep` — 15-20+ searches, exhaustive with competitor/market angles
- `--save` — whether to save to brain/research/ (default: true)
- If no topic provided, ask the user

### Step 1: Define Research Scope
- Break the topic into 5-10 specific sub-questions
- Identify what type of research this is: market, competitive, technical, legal, general
- Create a todo list to track progress through sub-questions

### Step 2: Execute Search Rounds
Run multiple web searches, varying the queries:
- Round 1: Broad overview queries (what, how, overview, guide)
- Round 2: Specific data queries (statistics, market size, pricing, trends)
- Round 3: Expert/opinion queries (analysis, comparison, review, critique)
- Round 4: Recent/news queries (2025-2026 updates, latest, new developments)
- For `deep` depth: Round 5+ with niche, contrarian, and edge-case queries

### Step 3: Fetch and Extract Key Sources
- For the most promising search results, fetch the full page content
- Extract key data points, quotes, statistics, and insights
- Track all source URLs for citation

### Step 4: Synthesize Findings
Compile into a structured report:

```markdown
# Research: [Topic]
> Generated: YYYY-MM-DD | Depth: [level] | Sources: [count]

## Executive Summary
[3-5 sentence overview of key findings]

## Key Findings
1. [Finding with supporting data]
2. [Finding with supporting data]
...

## Detailed Analysis
### [Sub-topic 1]
...
### [Sub-topic 2]
...

## Data & Statistics
| Metric | Value | Source |
|--------|-------|--------|
...

## Opportunities / Implications
- [What this means for Mike's business]

## Sources
1. [Title](URL) — [one-line summary]
...
```

### Step 5: Save Report
- Save to `~/.claude/brain/research/[topic-slug].md`
- If a file with that name exists, append a date suffix
- Report the file location and key takeaways to the user

### Step 6: Connect to Goals
- Check `~/.claude/brain/goals.md` — does this research connect to any active goal?
- If yes, note the connection and suggest next actions
