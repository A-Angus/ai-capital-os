---
description: "Full strategic SWOT analysis for any business decision, market, or opportunity — with action items and a go/no-go recommendation."
argument-hint: "[topic or opportunity to analyze]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebSearch, TodoWrite]
---

# SWOT Analysis

The user wants a comprehensive strategic SWOT analysis on a specific topic, opportunity, market, or decision.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract the subject of analysis from $ARGUMENTS
- If no arguments provided, ask: "What do you want me to analyze? A business idea, a market, a partnership, a decision you're weighing?"
- Determine if this is a go/no-go decision, market entry, competitive assessment, or general strategy review

### Step 1: Gather Context from Brain

Read these files for alignment and background:
1. `brain/goals.md` — Does this subject align with stated priorities?
2. `brain/projects/README.md` — Does this relate to or conflict with active projects?
3. Search `brain/research/` — Any existing research on this topic?
4. Search `brain/knowledge-base/` — Any relevant domain expertise?
5. Check if a previous SWOT exists on this topic — if so, offer to update vs. create new

### Step 2: Research (If Web Search Available)

Search for:
- Market size and growth trends for the subject
- Key competitors and their positioning
- Recent industry news, shifts, or disruptions
- Success rates and common failure modes
- Regulatory or legal considerations
- Relevant statistics and benchmarks

If no web search: Work with user context and domain knowledge. Note assumptions.

### Step 3: Build the Four Quadrants

For each quadrant, identify 5-8 specific, evidence-based points:

**Strengths (Internal, Positive):**
- What advantages exist? Unique resources, skills, assets, relationships?
- What's working well that could be leveraged?
- Rate each: High / Medium / Low impact

**Weaknesses (Internal, Negative):**
- What's missing? Gaps in resources, skills, team, capital?
- Where is vulnerability highest?
- Rate each: High / Medium / Low severity

**Opportunities (External, Positive):**
- What market trends favor this? What gaps exist?
- What timing advantages are available?
- Rate each by timeline and probability

**Threats (External, Negative):**
- Competitors, market risks, regulatory risks?
- What's outside the user's control that could cause damage?
- Rate each by severity, probability, and identify early warning signals

### Step 4: Cross-Quadrant Analysis

Analyze the four intersections:
- **SO (Strength + Opportunity):** How to use strengths to capture opportunities
- **ST (Strength + Threat):** How to use strengths to defend against threats
- **WO (Weakness + Opportunity):** What weaknesses to fix to unlock opportunities
- **WT (Weakness + Threat):** What weaknesses to shore up before threats exploit them

### Step 5: Generate Action Items

For each quadrant, create 2-3 specific, time-bound actions:
- **Leverage** strengths (do more of what works)
- **Fix** weaknesses (close the gaps)
- **Capture** opportunities (move before they close)
- **Defend** against threats (build protection)

### Step 6: Risk Matrix

Build a prioritized risk table:
- List top 5 risks
- Rate probability (H/M/L) and impact (H/M/L)
- Assign priority ranking
- Recommend response: Accept / Mitigate / Avoid / Transfer

### Step 7: Strategic Recommendation

Deliver a clear verdict:
- **GO** — Strengths and opportunities outweigh weaknesses and threats. Move forward.
- **NO-GO** — Risks too high, timing wrong, or misaligned with goals. Pass.
- **CONDITIONAL GO** — Proceed only if specific conditions are met. List them.

Support with 2-3 paragraphs of reasoning. Include next steps for GO, conditions for CONDITIONAL, and what would change the answer for NO-GO.

### Step 8: Save the Analysis

Save to: `brain/research/swot-{topic-slug}-{YYYY-MM-DD}.md`

Create `brain/research/` directory if it doesn't exist.

### Step 9: Print Summary

Print to terminal:
- Executive summary (3-5 sentences)
- Verdict with one-line rationale
- Top 3 action items
- Location of full analysis file

Then: "Full SWOT analysis saved. Want me to dig deeper into any quadrant or adjust the recommendation?"