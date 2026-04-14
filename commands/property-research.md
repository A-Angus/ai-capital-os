---
description: "Deep dive research on any property address — ownership, tax records, sales history, neighborhood data, and estimated value."
argument-hint: "[property address] [--include comps|neighborhood|schools|crime|all]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch, TodoWrite]
---

# Property Research

The user wants a comprehensive deep dive on a specific property address — everything publicly available about it.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract the full property address
- `--include` — what extra data to pull (default: all)
- If no address provided, ask the user

### Step 1: Property Details
Search for and compile core property information:
- **Address:** Full address with zip
- **Property Type:** SFH, MFH, condo, townhouse, land, commercial
- **Beds / Baths / Sqft:** Interior details
- **Lot Size:** Acreage or sqft
- **Year Built:** Construction year
- **Stories:** Number of levels
- **Garage:** Type and size
- **Features:** Pool, basement, HOA, etc.
- **Condition:** Any available info on current condition

### Step 2: Ownership & Tax Records
Search public records:
- **Current Owner:** Name (public record)
- **Ownership Duration:** How long current owner has held it
- **Purchase Date:** When they bought it
- **Purchase Price:** What they paid
- **Assessed Value:** Current tax assessment (land + improvements)
- **Annual Taxes:** Property tax amount
- **Tax Status:** Current or delinquent
- **Liens:** Any known liens or encumbrances

### Step 3: Sales History
- All recorded sales with dates and prices
- Price appreciation over time
- Days on market for each listing
- Any withdrawn or expired listings

### Step 4: Estimated Value
- Search Zillow Zestimate, Redfin estimate, Realtor.com
- Pull 3-5 recent sales comps (similar properties, sold within 6 months)
- Calculate $/sqft based on comps
- Provide a value range: low, mid, high

```markdown
## Estimated Value

| Source | Estimate |
|--------|----------|
| Zillow Zestimate | $X |
| Redfin Estimate | $X |
| Comp-Based Estimate | $X |
| **Suggested Range** | **$X — $X** |

### Recent Sales Comps
| Address | Beds/Baths | Sqft | Sold Price | $/Sqft | Date |
|---------|-----------|------|-----------|--------|------|
...
```

### Step 5: Neighborhood Data (if --include neighborhood or all)
- **Neighborhood Name:** Community/subdivision
- **Walk Score / Transit Score**
- **Median Home Value:** For the area
- **Median Household Income**
- **Population Density**
- **School Ratings:** Nearby schools and scores
- **Crime Data:** Relative safety rating
- **Major Employers:** Nearby employment centers
- **Commute:** Drive time to nearest city center

### Step 6: Mortgage / Loan Estimate
If this is a potential acquisition:
- Estimate existing mortgage balance (based on purchase price, date, and typical terms)
- Estimate equity position
- Flag SubTo or seller finance potential

### Step 7: Red Flags & Opportunities
- **Red Flags:** Tax delinquency, long DOM, price drops, code violations, flood zone
- **Opportunities:** Equity play, value-add potential, motivated seller signals, below-market pricing

### Step 8: Save Report
- Save to `~/.claude/brain/deal-packages/[address-slug]/property-research.md`
- Create the deal folder if it doesn't exist
- Report key findings and the file location to the user
