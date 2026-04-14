# SOP: Marketplace Deal Routing

**File:** marketplace-deal-routing.md
**Category:** Tech
**Status:** 🔴 Draft
**Last Updated:** 2026-03-05

---

## Purpose

Define how deals move through the automated Liberty Equity Xchange marketplace platform. This SOP captures the future-state automated process being built — and guides current manual execution in the same structure so the transition to automation is seamless.

---

## Current State vs. Future State

| Step | Current (Manual) | Future (Automated) |
|------|-----------------|-------------------|
| Deal submission | Borrower contacts Alex directly | Online portal intake form |
| Deal screening | Alex reviews manually | Platform scores A/B/C/D automatically |
| Lender matching | Alex identifies lender by deal type | Platform matches based on criteria database |
| Deal routing | Alex submits to lender | Platform routes deal package to matched lenders |
| Pipeline tracking | `brain/deals/deals.md` | CRM with automated stage updates |
| Follow-up | Manual outreach | Automated follow-up sequences (GHL) |

---

## Marketplace Deal Flow (Target State)

```
Borrower submits deal via intake portal
         │
         ▼
Platform validates intake (all fields complete?)
         │
         ▼
Deal Screening Engine
  → Calculate deal spread
  → Check leverage ratios
  → Score deal: A / B / C / D
         │
    ┌────┴────┐
    A/B      C/D
    │         │
    ▼         ▼
Lender    Flag for
Matching  Manual Review
Engine    or Decline
    │
    ▼
Top 3 lender matches identified
         │
         ▼
Deal package generated automatically
         │
         ▼
Alex reviews and approves routing
         │
         ▼
Deal submitted to lenders
         │
         ▼
Lender responds → conditions tracked in CRM
         │
         ▼
Deal closes → fee recorded → marketplace transaction complete
```

---

## Infrastructure Being Built

| Component | Status | Notes |
|-----------|--------|-------|
| Borrower intake portal | 🔴 In progress | LEX website build (Lovable + Supabase) |
| Deal screening logic | 🔴 Draft | Based on `deal-screening.md` SOP |
| Lender database | 🟡 Active | `brain/lenders/lenders.md` — manual for now |
| CRM pipeline | 🔴 In progress | GoHighLevel (GHL) at app.cyclsales.com |
| Automated follow-up | 🔴 Draft | GHL sequences |
| Lender matching engine | 🔴 Future | Requires lender criteria database |

---

## AI Role in Current Manual Marketplace

Until automation is built, the AI assists by:

1. Running deal screening logic on every new submission
2. Identifying lender matches from `brain/lenders/lenders.md`
3. Generating deal summaries and submission packages
4. Tracking deals in `brain/deals/deals.md`
5. Flagging stalled deals and drafting follow-up messages
6. Maintaining the lender and borrower databases

---

## Key Principle

> Every manual step in this SOP should eventually be replaced by an automated system. Build the manual process correctly first — then automate it.

---

## AI Instructions

- Treat every deal conversation as if it is moving through this marketplace flow
- Always know which stage a deal is in and what the next automated step would be
- When building or discussing platform features, reference this SOP for the intended deal flow
- Flag any step in the current manual process that is a bottleneck — it's the next automation target
