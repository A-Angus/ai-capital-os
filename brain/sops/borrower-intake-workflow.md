# SOP: Borrower Intake Workflow

**File:** borrower-intake-workflow.md
**Category:** Sales / Operations
**Status:** 🟡 Active
**Last Updated:** 2026-03-05

---

## Purpose

Define the end-to-end process for receiving a borrower deal submission, evaluating it, routing it to the correct capital source, and following up until the deal is funded or closed.

This SOP is the operational manual for the Borrower Intake System (`brain/projects/borrower-intake-system.md`).

---

## Step 1 — When to Send the Intake Form

Send the intake form link anytime a borrower or deal source mentions a deal that may need financing.

**Triggers:**
- Borrower DMs, emails, or calls about a deal
- Deal source (Bryan, Brian, wholesaler, etc.) sends a referral
- LinkedIn or social media connection mentions a project needing capital
- Someone at a networking event or in an investor community asks about funding

**How to send it:**

> "I'd love to take a look at this. The fastest way for me to evaluate your deal is to have you fill out a quick intake form — it takes about 3 minutes and gives me everything I need to assess the funding options. Here's the link: [intake form URL]"

**Rule:** Never do detailed analysis on informal, incomplete information. Always get the form submitted first.

---

## Step 2 — Receive and Review the Submission

When a form is submitted:

1. Deal auto-populates in GHL CRM at stage: **New Submission**
2. Review the submission within **24 hours**
3. Confirm all required fields are complete (see checklist below)

### Intake Completeness Checklist

**Borrower Info**
- [ ] Name
- [ ] Email
- [ ] Phone
- [ ] Entity name (LLC or Corp)

**Property Info**
- [ ] Property address
- [ ] Property type
- [ ] City and state

**Deal Financials**
- [ ] Purchase price
- [ ] ARV or current value
- [ ] Rehab budget (or confirmed no rehab)

**Financing Request**
- [ ] Loan amount requested
- [ ] Loan purpose / deal type

**Borrower Profile**
- [ ] Credit score range
- [ ] Liquidity available
- [ ] Number of prior deals

**Timeline**
- [ ] When funding is needed

If anything is missing, request it immediately before proceeding.

---

## Step 3 — Confirm Receipt with Borrower

Send an acknowledgment within 24 hours of form submission.

**Example message:**
> "Got your deal submission — thanks for sending that over. I'm reviewing the details now and will follow up shortly with my initial thoughts on the funding options."

---

## Step 4 — Evaluate the Submission

Run the deal through the screening process (`brain/sops/deal-screening.md`):

1. Calculate deal spread: `ARV – Purchase Price – Rehab`
2. Check leverage against typical lender parameters
3. Review borrower profile (credit, liquidity, experience)
4. Assign deal score: **A / B / C / D**

Update GHL stage to: **Initial Review**

---

## Step 5 — Categorize the Deal

Tag the deal by type. This determines which lenders to consider.

| Deal Type | Tag | Primary Lender Category |
|-----------|-----|------------------------|
| Fix and flip | `fix_flip` | Asset-based lenders |
| Rental acquisition | `dscr` | DSCR lenders |
| Bridge financing | `bridge` | Bridge lenders |
| Development | `construction` | Construction / bridge |
| Commercial acquisition | `commercial` | Commercial bridge / mezz |
| Refinance | `refi` | DSCR / conventional |

---

## Step 6 — Determine Next Action by Score

| Score | Action | GHL Stage |
|-------|--------|-----------|
| A | Immediately identify lender match, proceed to structuring | Structuring |
| B | Identify adjustments needed, advise borrower, proceed | Structuring |
| C | Request additional info or deal adjustments | Initial Review (hold) |
| D | Decline professionally | Closed (declined) |

---

## Step 7 — Structure the Capital Stack

For A and B deals, build the funding structure before contacting any lender.

Reference: `brain/sops/capital-stack-structuring.md`

**Output:** A clear funding structure showing:
- Senior loan amount and lender
- Gap capital if needed
- Borrower equity required
- Total project cost covered

---

## Step 8 — Route to Lenders

Cross-reference `brain/lenders/lenders.md` and identify 1–3 lenders that match the deal.

Reference: `brain/sops/lender-matching.md`

Prepare submission package:
- [ ] Deal summary (address, purchase, rehab, ARV, loan request)
- [ ] Borrower profile (credit, liquidity, experience)
- [ ] Exit strategy
- [ ] Comps supporting ARV (if required)

Update GHL stage to: **Lender Outreach**

---

## Step 9 — Communicate Structure to Borrower

Before or alongside lender submission, update the borrower on the proposed structure.

**Example:**
> "Based on your numbers, here's how the funding would likely work:
>
> Senior loan (70% of $340k ARV): ~$238k — [Lender type]
> Your equity needed: ~[X]
>
> I'm reaching out to lenders now. I'll follow up once I have initial feedback."

---

## Step 10 — Follow Up Until Resolution

Track every deal until one of two outcomes:
- ✅ Deal funded — update GHL to Closed, record fee
- ❌ Deal declined or dead — update GHL to Closed (declined), note reason

Reference follow-up cadence: `brain/sops/borrower-follow-up.md`

---

## AI Instructions

- When a borrower mentions a deal in conversation, immediately ask if they've completed the intake form — if not, send the link
- Run every submission through the completeness checklist before proceeding to analysis
- Always assign a deal score before routing to lenders
- Update GHL stage after every step — the pipeline is only useful if it's current
- Never let a submitted deal sit without a next action recorded

---

## Automation Target

**Future state:**
1. Borrower submits form → GHL auto-creates deal record
2. AI scores deal automatically (A/B/C/D)
3. Missing fields trigger automated follow-up request to borrower
4. A and B deals auto-matched to top 3 lenders
5. Deal summary auto-generated and queued for Alex to review and send
6. Alex approves routing → deal submitted to lenders automatically
