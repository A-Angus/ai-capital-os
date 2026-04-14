# SOP: Borrower Follow Up System

**File:** borrower-follow-up.md
**Category:** Sales
**Status:** 🔴 Draft
**Last Updated:** 2026-03-05

---

## Purpose

Keep deals moving forward through consistent, professional borrower communication. Deals die from silence — not from "no."

---

## Trigger

- New borrower inquiry received
- Deal is awaiting documents or information from borrower
- Deal has been in same stage for 7+ days
- Lender has responded and borrower needs to be updated

---

## Follow Up Timeline

| Timing | Action |
|--------|--------|
| Same day | Confirm receipt of deal inquiry |
| 24–48 hours | Deliver initial deal assessment or request missing info |
| 3–5 days (no response) | First follow-up |
| 7 days (no response) | Second follow-up |
| 14 days (no response) | Final check-in, then mark inactive |

---

## Steps

### Step 1 — Track New Inquiries

Every new borrower inquiry gets logged in `brain/deals/deals.md` immediately with stage 🔵 Intake / Screening.

### Step 2 — Confirm Receipt (Same Day)

**Example:**
> "Hey [Name] — got your deal details. I'll take a look and follow up shortly with what I'm seeing on the funding side."

### Step 3 — Deliver Assessment (24–48 Hours)

After screening, communicate the result clearly.

**If A or B deal:**
> "I've reviewed the numbers on [property address]. This looks like it could work for a [fix and flip / DSCR / bridge] structure. I'm putting together the funding options now — I'll follow up with details shortly."

**If missing information:**
> "I started reviewing your deal but need a few more details before I can determine funding options. Can you send me [specific missing items]?"

**If C deal:**
> "I've reviewed the numbers. There are a few things that need to be addressed before this fits current lending criteria — [specific issue]. Let me know if you want to talk through how to adjust the structure."

### Step 4 — Follow Up on Stalled Borrowers

When a borrower goes quiet after submitting a deal:

**Follow-up 1 (3–5 days):**
> "Hey [Name] — just following up on [property address]. Still working on this one?"

**Follow-up 2 (7 days):**
> "Hey [Name] — checking back in on the [property] deal. Let me know if you still need funding on this or if the situation has changed."

**Final check-in (14 days):**
> "Hey [Name] — last follow-up on this one. If the deal is still alive and you need capital, just reach out and I can pick it back up."

### Step 5 — Schedule Calls When Needed

For complex deals or borrowers who need more hand-holding, offer a call.

> "Want to jump on a quick call to go over the structure? Happy to walk through how the funding would work."

### Step 6 — Record All Communication

After every borrower interaction, update the deal file in `brain/deals/deals.md`:
- Date of contact
- Summary of what was discussed
- Next step and who owns it

### Step 7 — Close the Loop

A deal stays active until one of two outcomes:
- ✅ Deal moves forward to lender submission
- ❌ Deal is declined or borrower goes dark after final follow-up

Mark inactive deals clearly in `brain/deals/deals.md` so the pipeline stays clean.

---

## AI Instructions

- When asked to follow up on a borrower, check `brain/deals/deals.md` for last contact date and current stage
- If a deal has had no activity for 7+ days, draft a follow-up message automatically
- Always match follow-up tone to deal stage — early follow-ups are warmer, later ones are brief and direct
- Never let a deal sit without a clear "next step" recorded
