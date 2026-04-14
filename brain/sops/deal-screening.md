# SOP: Deal Screening and Analysis

**File:** deal-screening.md
**Category:** Sales
**Status:** ✅ Active
**Last Updated:** 2026-03-05

---

## Purpose

Quickly determine whether a deal is financeable before spending time on lender matching or structuring. Protects Alex's time and lender relationships by only submitting viable deals.

---

## Trigger

Deal intake checklist is complete (`borrower-deal-intake.md`).

---

## Steps

### Step 1 — Calculate Deal Spread

Run the basic math first.

```
Deal Spread = ARV – Purchase Price – Rehab Budget
```

A viable deal typically leaves enough margin to:
- Support the lender's LTV or ARV requirements
- Cover borrower costs and fees
- Generate a profit for the borrower on exit

### Step 2 — Review Leverage Requirements

Check whether the deal fits typical lending parameters.

| Deal Type | Typical Leverage |
|-----------|----------------|
| Fix and flip | 65–75% of ARV |
| DSCR rental | 70–80% LTV |
| Bridge | 65–75% LTV |
| Construction | 60–70% LTC or ARV |

If the loan request exceeds these ranges, a gap capital or secondary source will be needed. Note it — don't disqualify yet.

### Step 3 — Evaluate Borrower Profile

| Factor | Notes |
|--------|-------|
| Credit score | 660+ preferred; asset-based lenders may go lower |
| Liquidity | Must cover closing costs and reserves at minimum |
| Experience | No prior deals = higher risk; note for lender matching |
| Entity | LLC or Corp preferred by most lenders |

Weak borrower profile does not automatically kill the deal — it shifts the lender category toward asset-based lenders and creative structures.

### Step 4 — Score the Deal

Assign a score based on the full picture.

| Score | Meaning | Criteria |
|-------|---------|----------|
| A | Strong deal | Numbers work, borrower qualified, clean exit |
| B | Financeable with adjustments | Minor gaps in leverage, credit, or structure |
| C | Weak deal | Significant issues but possible path forward |
| D | Not financeable | Deal does not pencil or borrower cannot qualify |

### Step 5 — Determine Next Action

| Score | Action |
|-------|--------|
| A | Proceed immediately to lender matching (`lender-matching.md`) |
| B | Provide structuring advice, then proceed to lender matching |
| C | Request additional information from borrower before proceeding |
| D | Decline deal professionally and move on |

Update deal stage in `brain/deals/deals.md` after scoring.

---

## Declining a Deal (Score D)

Keep it professional and brief.

**Example message:**
> "After reviewing the numbers, this deal doesn't fit the current lending criteria we work with. If the structure changes — purchase price, rehab budget, or ARV — feel free to resubmit and we can take another look."

---

## AI Instructions

- Run this screening logic whenever a deal is presented in conversation
- Always show the math — state the deal spread, leverage percentage, and score explicitly
- A or B deals should move to lender matching immediately
- Never submit a D deal to a lender — it wastes relationship capital
- Update deal score in `brain/deals/deals.md`

---

## Automation Target

**Future state:** Borrower submits deal → platform calculates spread and leverage → auto-scores A/B/C/D → routes A and B deals to lender matching queue → Alex reviews C and D manually.
