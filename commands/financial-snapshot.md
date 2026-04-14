---
description: "Generate an executive financial summary — revenue by stream, expenses, profit margins, cash flow projection, burn rate, runway, and 3 actionable recommendations."
argument-hint: "[business-or-period] [--revenue amount] [--expenses amount] [--cash amount] [--businesses biz1,biz2]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebSearch, TodoWrite]
---

# Financial Snapshot

The user wants an executive-level financial summary with actionable recommendations.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Determine the business or time period for the snapshot
- `--revenue` — total monthly revenue (can also be broken out by stream in conversation)
- `--expenses` — total monthly expenses
- `--cash` — current cash on hand
- `--businesses` — multiple business entities to track separately
- If no financial data provided, ask for: (1) monthly revenue, (2) monthly expenses, (3) cash in the bank
- Check `~/.claude/brain/research/` for prior financial snapshots

### Step 1: Load Context
- Check `~/.claude/brain/goals.md` for financial goals and targets
- Check `~/.claude/brain/projects/` for active businesses or revenue-generating projects
- Check `~/.claude/brain/research/` for previous financial data or snapshots
- If prior snapshots exist, use them for trend comparison

### Step 2: Revenue Analysis
- Break down revenue by stream (each source of income)
- Calculate percentage of total for each stream
- Assess revenue concentration risk (>50% from one stream = high risk)
- Evaluate revenue quality: recurring vs. one-time, predictability, average deal size

### Step 3: Expense Analysis
- Categorize expenses (payroll, software, marketing, rent, insurance, travel, subscriptions, etc.)
- Calculate expense-to-revenue ratio
- Flag non-essential expenses
- Identify potential savings (subscription audit, contract renegotiation, automation opportunities)

### Step 4: Profitability
- Build P&L summary: revenue - COGS = gross profit - operating expenses = net income - taxes = net profit
- Calculate gross margin, operating margin, net margin
- Assess margins against industry benchmarks
- If multiple businesses: individual P&L per entity + consolidated view

### Step 5: Cash Flow Projection
- Current cash position (bank balances, receivables, payables)
- 90-day forecast: month-by-month cash in, cash out, ending balance
- Scenario analysis: best case, base case, worst case
- Cash conversion cycle (how long from work to cash received)

### Step 6: Burn Rate & Runway
- Monthly fixed costs + average variable costs = total burn
- Daily burn rate
- Runway at zero revenue
- Runway at 50% revenue drop
- Runway at current pace
- Compare to recommended 3-6 month reserve

### Step 7: Generate 3 Recommendations
Exactly 3 high-impact, specific, actionable recommendations:
- Each includes: the problem, the fix, implementation steps, timeline, difficulty, dollar impact
- Categories to consider: revenue increase, cost reduction, cash flow optimization, risk reduction, tax optimization
- Calculate combined monthly and annual impact

### Step 8: Save and Report
- Save to `~/.claude/brain/research/financial-snapshot-{YYYY-MM-DD}.md`
- Create brain/research/ if it does not exist
- Present: financial health verdict, monthly net profit/loss and margin, runway, #1 recommendation
- Include disclaimer: not tax/legal/accounting advice — consult a CPA
- Offer to dig deeper into any section or schedule monthly re-runs