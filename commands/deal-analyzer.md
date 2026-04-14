---
description: "Analyze a real estate deal — cash flow projections, ROI, cap rate, cash-on-cash return, and multiple exit scenarios."
argument-hint: "[property address or description] [--price amount] [--rent amount] [--down amount] [--type subto|seller-finance|flip|rental|brrrr] [--terms details]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch, TodoWrite]
---

# Deal Analyzer

The user wants to analyze a real estate deal with detailed financial projections and multiple scenarios.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract property address or description
- `--price` — purchase price
- `--rent` — expected monthly rent (or current rent)
- `--down` — down payment or money in
- `--type` — deal structure (SubTo, seller finance, flip, rental, BRRRR)
- `--terms` — deal-specific terms (interest rate, term length, balloon, etc.)
- If missing critical numbers (price, rent), ask or research

### Step 1: Load T.O.P. Method Framework
- Read `~/.claude/brain/knowledge-base/top-method/03-underwriting-how-deals-get-scored.md`
- Read `~/.claude/brain/knowledge-base/top-method/05-the-vqi-scoring-system.md`
- Read `~/.claude/brain/knowledge-base/top-method/02-deal-types-explained.md`
- Apply the T.O.P. Method underwriting framework to the analysis

### Step 2: Research Property Data (if address provided)
- Search for property details: beds, baths, sqft, lot size, year built
- Search for recent sales comps in the area
- Search for rental comps in the area
- Search for neighborhood data (schools, crime, employment)

### Step 3: Run the Numbers

**Core Metrics:**
| Metric | Value |
|--------|-------|
| Purchase Price | $X |
| Down Payment / Money In | $X |
| Estimated Market Value (ARV) | $X |
| Monthly Rent (Gross) | $X |
| Monthly Expenses | $X |
| Monthly Cash Flow (Net) | $X |
| Annual Cash Flow | $X |
| Cap Rate | X% |
| Cash-on-Cash Return | X% |
| Gross Rent Multiplier | X |
| Debt Service Coverage Ratio | X |

**Monthly Expense Breakdown:**
| Expense | Amount | Notes |
|---------|--------|-------|
| Mortgage/Note Payment | $X | [terms] |
| Property Taxes | $X | [annual / 12] |
| Insurance | $X | |
| Vacancy (8%) | $X | |
| Maintenance (5%) | $X | |
| Property Management (10%) | $X | |
| Utilities (if applicable) | $X | |
| HOA (if applicable) | $X | |
| **Total Expenses** | **$X** | |

### Step 4: Scenario Analysis
Run 3 scenarios:

**Conservative:**
- Higher vacancy (12%), lower rent (-5%), higher expenses
- Worst-case cash flow and returns

**Base Case:**
- Standard assumptions (8% vacancy, market rent, typical expenses)
- Expected cash flow and returns

**Optimistic:**
- Lower vacancy (5%), rent increase (+5%), value-add upside
- Best-case cash flow and returns

### Step 5: Deal-Type Specific Analysis

**SubTo:**
- Existing mortgage details and payment
- Equity position
- Risk assessment (due-on-sale clause, insurance, escrow)

**Seller Finance:**
- Note terms (rate, term, balloon, amortization)
- Payment schedule
- Comparison to conventional financing

**Flip:**
- Rehab budget estimate
- ARV analysis
- Profit margin and timeline
- Holding costs

**BRRRR:**
- Buy, rehab, rent, refinance, repeat projections
- Cash left in deal after refinance

### Step 6: VQI Score (if applicable)
Apply the T.O.P. Method VQI scoring system to rate the deal.

### Step 7: Generate Report

```markdown
# Deal Analysis: [Address/Description]
> Generated: YYYY-MM-DD | Type: [deal type]

## Deal Summary
[2-3 sentence overview — is this a good deal?]

## The Numbers
[Core metrics table from Step 3]

## Expense Breakdown
[Monthly expenses table]

## Scenario Analysis
[Three scenarios with key numbers]

## VQI Score: [X/100]
[Scoring breakdown]

## Verdict
- **Buy?** [Yes / No / Conditional]
- **Best exit strategy:** [hold/flip/refinance/wholesale]
- **Key risks:** [top 3 risks]
- **Key upside:** [top 3 opportunities]
```

### Step 8: Save Report
- Save to `~/.claude/brain/deal-packages/[address-slug]/deal-analysis.md`
- Create the deal folder if it doesn't exist
- Report findings and file location to the user
