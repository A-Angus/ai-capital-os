# Project: Borrower Intake System

**File:** borrower-intake-system.md
**Category:** Tech / Operations
**Priority:** 🔴 Critical
**Status:** 🟡 Active
**Last Updated:** 2026-03-05

---

## Purpose

Create a centralized system where borrowers submit deal information that can be evaluated, structured, and matched with capital sources. This system becomes the front door of the Liberty Equity Xchange capital marketplace.

---

## Objective

Build a standardized intake process that collects complete deal information and feeds it into the LEX capital placement workflow.

**Goal:** Convert conversations and referrals into structured deal submissions that can be quickly evaluated and routed to lenders.

---

## Why This Project Matters

Most deal opportunities fail because information is incomplete or scattered across messages, emails, and calls.

A structured intake system ensures:
- All required deal data is collected upfront
- Deals can be screened quickly and consistently
- Lender matching becomes efficient and accurate
- AI systems can analyze deals automatically

Without this system: deal conversations remain informal and difficult to manage.
With this system: deal flow becomes structured, scalable, and automatable.

---

## Entry Points

Borrowers enter the system through multiple channels:

| Channel | Method |
|---------|--------|
| Direct link | Primary method — borrowers submit deals through the online form |
| Messenger / DM | If a deal appears in conversation, send the intake form link |
| LinkedIn | When a connection mentions a deal, request they complete the intake form |
| Referrals | Partners send borrowers directly to the intake portal |
| Website | libertyequityx.com intake form (primary inbound channel) |

---

## Intake Form Structure

The form collects enough information to determine if a deal can be financed.

### Borrower Information
- Name
- Email
- Phone
- Company name or LLC

### Property Information
- Property address
- City and state
- Property type (single family / duplex / multifamily / development / commercial)

### Deal Overview
- Purchase price
- Estimated ARV or current value
- Rehab budget (if no rehab, mark as rental or acquisition)

### Financing Request
- Loan amount requested
- Loan purpose (fix and flip / bridge / DSCR rental / construction / development)

### Borrower Profile
- Credit score range
- Liquidity available
- Number of completed projects (experience determines lender fit)

### Timeline
- When funding is needed (under contract / closing soon / planning stage)

---

## Intake Processing Workflow

```
Borrower submits form
        ↓
Deal appears in CRM pipeline (GHL)
        ↓
AI reviews deal data
        ↓
Deal categorized by type
        ↓
Potential capital structures identified
        ↓
Deal routed to lenders or capital partners
```

*Full process detail in `brain/sops/borrower-intake-workflow.md`*

---

## Deal Categories

The system tags deals automatically by type. Categories determine the correct lender set.

| Category | Lender Type |
|----------|-------------|
| Fix and flip | Asset-based lenders |
| Rental acquisition | DSCR lenders |
| Bridge financing | Bridge lenders |
| Development | Construction / bridge lenders |
| Commercial acquisition | Commercial bridge / mezz lenders |
| Refinance | DSCR / conventional lenders |

---

## CRM Pipeline Stages

| Stage | Description |
|-------|-------------|
| New Submission | Intake received |
| Initial Review | Deal being evaluated |
| Structuring | Capital stack being built |
| Lender Outreach | Sent to lenders |
| Underwriting | Lender reviewing |
| Approved | Loan terms issued |
| Closed | Deal funded |

**CRM:** GoHighLevel at app.cyclsales.com
**Connected project:** `brain/projects/ghl-crm.md`

---

## Tech Stack

| Tool | Role |
|------|------|
| libertyequityx.com | Public-facing intake form |
| Supabase | Backend — stores form submissions |
| GoHighLevel (GHL) | CRM — deal pipeline tracking and follow-up sequences |
| Supabase Edge Function | Webhook to push intake data into GHL automatically |

---

## Automation Vision

Future automation allows the system to:
- Screen deals automatically using intake data
- Suggest lenders based on deal type and borrower criteria
- Identify missing information and request it from borrowers
- Prepare deal summaries for lender submission

Alex intervenes primarily during structuring, negotiation, and complex deal oversight.

---

## Success Metrics

| Metric | Current | Target |
|--------|---------|--------|
| Monthly deal submissions | 0 consistent | 20+ |
| Qualified deals (A or B score) | 0 | 10+ |
| Deals sent to lenders | 0 | 5+ |
| Deals funded | 0 | 2–4 |

---

## Next Actions

- [ ] Finalize intake form fields on LEX website (Lovable build)
- [ ] Connect Supabase form submission to GHL via webhook
- [ ] Configure GHL pipeline with all 7 stages above
- [ ] Set up automated acknowledgment message when form is submitted
- [ ] Create `brain/sops/borrower-intake-workflow.md` (next step)
- [ ] Test full workflow: submit test deal → confirm it appears in GHL

---

## Connected Files

- `brain/sops/borrower-intake-workflow.md` — step-by-step intake SOP *(to be created)*
- `brain/sops/borrower-deal-intake.md` — current manual intake process
- `brain/sops/deal-screening.md` — deal evaluation after intake
- `brain/projects/capital-marketplace-platform.md` — platform this feeds into
- `brain/projects/ghl-crm.md` — CRM configuration
- `brain/projects/lex-website.md` — intake form front-end
- `brain/deals/deals.md` — where submitted deals are tracked

---

## AI Notes

- When a borrower shares deal details in conversation, treat it as an informal intake submission — run through the intake form structure to identify what's missing
- Always send the intake form link before doing detailed analysis — structured data is better than scattered conversation notes
- When the intake system is live, every deal conversation should end with a form submission, not just a verbal exchange
