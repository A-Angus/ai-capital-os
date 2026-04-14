# SOP: Lender Matching Process

**File:** lender-matching.md
**Category:** Operations
**Status:** ✅ Active
**Last Updated:** 2026-03-05

---

## Purpose

Identify the correct lender or capital source for a screened deal. Match the deal to the right capital layer — senior debt, gap capital, mezz, or transactional — and build the full funding structure.

---

## Trigger

Deal has received a score of A or B from `deal-screening.md`.

---

## Steps

### Step 1 — Identify the Deal Type

Determine the primary loan category needed.

| Deal Type | Examples |
|-----------|---------|
| Fix and flip | Purchase + rehab, short-term exit |
| DSCR rental | Stabilized rental, long-term hold |
| Bridge | Short-term, transitional property |
| Ground-up construction | New build |
| Commercial | Mixed-use, multifamily 5+, commercial CRE |
| Business acquisition | Non-real estate business purchase |

### Step 2 — Cross-Reference Lender Database

Open `brain/lenders/lenders.md` and filter by:

1. **Loan type** — does the lender fund this deal type?
2. **Leverage** — does their LTV/ARV range cover the loan request?
3. **Geography** — are they active in this market?
4. **Borrower requirements** — does the borrower meet minimum credit and liquidity?

**Primary lender matching table:**

| Deal Type | First-Look Lenders |
|-----------|-------------------|
| Fix and flip | Rehab Financial Group, RCN Capital, Cogo Capital, CoreVest, LYNK Capital |
| DSCR rental | Visio Lending, Dominion Commercial, RCN Capital, CoreVest, Lima One |
| Bridge | CoreVest, Socotra Capital, Capital Funding Financial, Gelt Financial |
| Construction | Lima One, Gelt Financial |
| Commercial bridge / mezz | Bloomfield Capital, Avana Capital, Global Capital Partners |
| Business acquisition | National Business Capital, MyInvestorLoan via Vontive |

### Step 3 — Identify Capital Gaps

If the senior lender will not cover the full loan request, check:

| Gap Type | Source |
|----------|--------|
| Down payment / closing costs | Carrol Walton Grizzle, Eric Fuller |
| Full stack (100% financing) | Eric Fuller — Creative Cash Partners (NC, WV, OH, GA only) |
| Short-term bridge to close | Mikey (transactional) |
| Mezzanine above senior | Edgewood Capital Advisors, Farragut Capital Partners |

### Step 4 — Build the Capital Stack

Assemble the full funding structure before presenting to borrower.

**Example structure:**
```
Purchase price:   $200,000
Rehab budget:     $50,000
Total project:    $250,000

Senior loan (70% ARV of $330k):   $231,000
Gap / equity needed:               $19,000

Senior lender:    Rehab Financial Group
Gap source:       Carrol Walton Grizzle or borrower equity
```

### Step 5 — Present Options to Borrower

Communicate the structure clearly. Lead with the solution.

**Example:**
> "Based on your purchase price, rehab budget, and projected ARV, this deal can be structured with a senior fix and flip loan at approximately 70% of ARV. The remaining gap would need to be covered through equity or a secondary capital source. Here's how the stack looks..."

### Step 6 — Submit to Lender

Prepare and send the deal package. Standard package includes:
- [ ] Deal summary (address, purchase price, rehab, ARV, loan request)
- [ ] Borrower profile (credit score, liquidity, experience)
- [ ] Exit strategy
- [ ] Comps supporting ARV (if required)
- [ ] Entity documents (if required)

Update deal stage in `brain/deals/deals.md` to 🟠 Submitted to Lender.

---

## AI Instructions

- Always check lender geographic restrictions before recommending (especially Eric Fuller — NC, WV, OH, GA only)
- Never present a lender to a borrower with their contact details — route all submissions through Liberty Equity Xchange
- If no single lender covers the full stack, identify the combination that works
- Update `brain/deals/deals.md` after every lender submission
- If a lender declines, note the reason and identify the next best match

---

## Automation Target

**Future state:** Screened deal auto-matched to top 3 lenders based on deal type, geography, and borrower profile → deal package generated automatically → Alex reviews and approves submission.
