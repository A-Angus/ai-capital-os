# Project: Capital Marketplace Platform

**File:** capital-marketplace-platform.md
**Priority:** 🔴 High
**Status:** 🟡 In Progress
**Last Updated:** 2026-03-05

---

## Purpose

Build the automated system where borrowers submit deals → AI analyzes → lenders matched → Alex oversees complex transactions. This is the long-term infrastructure that transforms Liberty Equity Xchange from a manual brokerage into a scalable capital marketplace.

---

## Vision

A platform where:
- Borrowers submit deals through an online portal
- The system analyzes deal viability and scores A/B/C/D automatically
- Lenders are matched based on deal type, geography, and borrower profile
- Standard deals route automatically
- Alex focuses on complex structuring and capital relationships

---

## Key Components

| Component | Description | Status |
|-----------|-------------|--------|
| Borrower intake portal | Online form capturing full deal and borrower data | 🟡 In Progress |
| Deal analyzer | Logic engine that screens and scores deals | 🔴 Not Started |
| Lender database | Structured criteria database for matching | 🟡 In Progress (manual) |
| Automated routing | System that matches deals to lenders | 🔴 Not Started |
| CRM pipeline | Deal tracking from intake to close | 🟡 In Progress (GHL) |
| Automated follow-up | Borrower and lender communication sequences | 🔴 Not Started |

---

## Build Stages

| Stage | Objective | Status |
|-------|-----------|--------|
| Stage 1 | Manual capital placement with CRM tracking | 🟡 In Progress |
| Stage 2 | Borrower intake portal and automated deal screening | 🟡 In Progress |
| Stage 3 | Lender database and automated matching | 🔴 Not Started |
| Stage 4 | Marketplace platform routing deals to lenders | 🔴 Not Started |
| Stage 5 | Semi-automated marketplace with advisory oversight | 🔴 Not Started |

---

## Tech Stack

| Tool | Role |
|------|------|
| Lovable | Website and portal front-end build |
| Supabase | Backend database (funding requests, contact inquiries) |
| GoHighLevel (GHL) | CRM pipeline and automated follow-up sequences |
| Supabase Edge Function | GHL webhook integration |

**GHL Location:** app.cyclsales.com

---

## Active Work

### LEX Website (Lovable + Supabase)
- 7-page build with dark navy/gold design system
- Supabase schema for funding requests and contact inquiries
- GHL webhook integration via Supabase Edge Function
- Status: 🟡 In Progress — see `brain/projects/lex-website.md`

### GHL CRM Setup
- Deal pipeline stages configured
- Borrower intake workflows
- Status: 🟡 In Progress — see `brain/projects/ghl-crm.md`

### Borrower Intake Portal
- Online deal submission form
- Status: 🟡 In Progress — see `brain/projects/borrower-intake-portal.md`

---

## Next Actions

- [ ] Complete LEX website intake form (Lovable build)
- [ ] Connect Supabase intake form to GHL via webhook
- [ ] Configure GHL pipeline stages for deal flow
- [ ] Begin documenting lender criteria in structured format for matching engine

---

## Success Metrics

| Metric | Target |
|--------|--------|
| Borrower deal submissions | 20–40 per month via portal |
| Deal screening time | Under 5 minutes per deal |
| Lender match accuracy | Right lender on first submission |
| Platform revenue | Placement fees on every funded deal |

---

## Connected Files

- `brain/sops/marketplace-deal-routing.md` — deal flow logic
- `brain/lenders/lenders.md` — lender matching database
- `brain/projects/lex-website.md` — website build
- `brain/projects/ghl-crm.md` — CRM setup
- `brain/projects/borrower-intake-portal.md` — intake portal

---

## AI Notes

- This is the highest-leverage long-term project — every system built should move toward this vision
- When discussing tech builds, reference the stage model above to frame where each piece fits
- Prioritize Stage 1 and Stage 2 completion before building Stage 3 and 4
