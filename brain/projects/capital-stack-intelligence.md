# Project: Capital Stack Intelligence System

**File:** capital-stack-intelligence.md
**Priority:** 🟡 Medium
**Status:** 🟡 In Progress
**Last Updated:** 2026-03-05

---

## Purpose

Teach the AI system how to structure funding stacks accurately and consistently. This project builds the knowledge base that powers Alex's capital architect model — enabling the AI to analyze any deal, identify the correct capital layers, and match the right lenders without manual lookup every time.

---

## What This Powers

- Accurate deal screening (A/B/C/D scoring)
- Precise lender matching by deal type and borrower profile
- Multi-layer capital stack assembly
- Automated deal routing (future marketplace)
- Faster, more confident deal structuring in every conversation

---

## Knowledge Base Components

### 1 — Lender Criteria Database

Detailed program criteria for every active lender. For each lender:

| Field | Example |
|-------|---------|
| Loan types | Fix and flip, DSCR, bridge |
| LTV / ARV limits | Up to 75% ARV |
| Credit minimum | 660+ |
| Liquidity requirement | 10% of loan amount |
| Active markets | Nationwide except ND, SD, VT |
| Min / max loan | $75k – $5M |
| Close time | 10–14 business days |
| Broker friendly | Yes, up to 2 points |

**Status:** 🟡 In Progress — `brain/lenders/lenders.md` is the current working version. Individual lender profile files to be built using `_LENDER-TEMPLATE.md`.

### 2 — Capital Layers Reference

Rules for when each capital layer is used:

| Layer | When to Use |
|-------|-------------|
| Senior debt | Primary funding — always first |
| Bridge / gap | When senior lender won't cover full need |
| Mezzanine | Large commercial deals needing layered debt |
| 100% financing | When borrower has no equity — Eric Fuller (NC, WV, OH, GA) |
| Transactional | Back-to-back closings only — Mikey |

**Status:** 🟡 Documented in SOPs. Needs dedicated knowledge-base file.

### 3 — Deal Analysis Rules

The logic engine for deal screening:

- Deal spread calculation: `ARV – Purchase – Rehab`
- Leverage check by deal type (65–75% ARV for flips, 70–80% LTV for DSCR)
- Borrower profile scoring (credit, liquidity, experience)
- A/B/C/D scoring criteria
- Decline triggers

**Status:** ✅ Active in `brain/sops/deal-screening.md`

### 4 — Funding Scenarios Library

Real deal examples showing how capital stacks were structured. Over time, this becomes a reference library for structuring similar deals faster.

**Status:** 🔴 Not Started — populate as deals are funded

### 5 — Market Intelligence

Notes on specific markets — which lenders are active, typical ARV ranges, investor activity levels.

**Status:** 🔴 Not Started

---

## Build Plan

| Phase | Action | Status |
|-------|--------|--------|
| Phase 1 | Build out individual lender profile files with full criteria | 🔴 In Progress |
| Phase 2 | Create capital-layers reference file in knowledge-base | 🔴 Not Started |
| Phase 3 | Document first 5 funded deals as scenario examples | 🔴 Not Started |
| Phase 4 | Add market intelligence notes for primary markets | 🔴 Not Started |
| Phase 5 | Feed structured data into marketplace matching engine | 🔴 Future |

---

## Next Actions

- [ ] Build profile files for top 5 lenders using `_LENDER-TEMPLATE.md`
- [ ] Create `brain/knowledge-base/capital-layers.md` reference file
- [ ] Create `brain/knowledge-base/deal-analysis-rules.md` from screening SOP
- [ ] Document first funded deal as a scenario example

---

## Connected Files

- `brain/lenders/lenders.md` — current lender directory
- `brain/lenders/_LENDER-TEMPLATE.md` — lender profile template
- `brain/sops/deal-screening.md` — deal analysis logic
- `brain/sops/capital-stack-structuring.md` — stack assembly process
- `brain/sops/lender-matching.md` — lender matching logic
- `brain/projects/capital-marketplace-platform.md` — platform this intelligence feeds into

---

## AI Notes

- As new lender criteria are learned in conversations, suggest adding them to the lender profile files
- When a deal is successfully structured, suggest logging it as a scenario example
- This project improves AI accuracy over time — treat every deal as a learning opportunity
