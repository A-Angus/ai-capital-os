---
description: "Rental market analysis for a property or area — comp rents, vacancy rates, demand drivers, and rental pricing recommendation."
argument-hint: "[address or area] [--beds 1-5] [--type sfh|mfh|condo|apartment] [--radius 1-10mi]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch, TodoWrite]
---

# Rental Analysis

The user wants a rental market analysis for a specific property or geographic area — what it could rent for, market conditions, and demand dynamics.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract the address or area (city, zip, neighborhood)
- `--beds` — bedroom count for comp filtering
- `--type` — property type (single family, multi-family, condo, apartment)
- `--radius` — search radius for comps (default: 3 miles)
- If no location provided, ask the user

### Step 1: Research Rental Comps
Search for comparable rental listings and recently rented properties:
- Search Zillow, Rentometer, Apartments.com for active listings
- Search for recently rented comps (last 3-6 months)
- Filter by similar: beds, baths, sqft, property type, condition
- Collect at least 5-10 comps

### Step 2: Compile Comp Data

```markdown
## Rental Comps

| # | Address | Beds/Baths | Sqft | Rent | $/Sqft | Status | Days on Market |
|---|---------|-----------|------|------|--------|--------|---------------|
| 1 | [address] | 3/2 | 1,400 | $1,800 | $1.29 | Active | 12 |
...

### Comp Summary
- **Low:** $X/mo
- **Median:** $X/mo
- **High:** $X/mo
- **Average:** $X/mo
- **Recommended Rent:** $X/mo
- **Price Per Sqft Range:** $X — $X
```

### Step 3: Market Conditions
Research and report:
- **Vacancy Rate:** Area vacancy rate and trend
- **Absorption Rate:** How fast rentals are filling
- **Rent Trends:** YoY rent growth for this area
- **Supply Pipeline:** New construction or units coming online
- **Demand Drivers:** Major employers, universities, military bases, hospitals
- **Seasonality:** Best/worst months to list in this market

### Step 4: Tenant Pool Analysis
- **Income demographics:** Median household income in the area
- **Affordability ratio:** Recommended rent vs. area median income (30% rule)
- **Renter population:** % of renters vs. owners in the area
- **Target tenant profile:** Who would rent this property?

### Step 5: Revenue Projections

```markdown
## Annual Revenue Projections

| Scenario | Monthly Rent | Vacancy | Gross Annual | Net Annual |
|----------|-------------|---------|-------------|------------|
| Conservative | $X | 10% | $X | $X |
| Base Case | $X | 7% | $X | $X |
| Optimistic | $X | 4% | $X | $X |

### Rent Growth Projections (5-Year)
| Year | Projected Rent | Annual Growth |
|------|---------------|---------------|
| Year 1 | $X | — |
| Year 2 | $X | X% |
| Year 3 | $X | X% |
| Year 4 | $X | X% |
| Year 5 | $X | X% |
```

### Step 6: Rental Pricing Recommendation
- Recommended listing price with reasoning
- Suggested lease terms (12-month, month-to-month, etc.)
- Any value-add opportunities to increase rent (pet policy, furnished, utilities included)
- Marketing suggestions (best platforms to list on for this market)

### Step 7: Save Report
- Save to `~/.claude/brain/research/rental-analysis-[location-slug]-YYYY-MM-DD.md`
- Report key findings and recommended rent to the user
