---
description: "Generate a professional invoice (HTML + markdown) for services rendered — auto-numbered, browser-printable, multi-currency."
argument-hint: "[client name] [amount or line items] [--type connection|tc|consulting|custom] [--description service details] [--due-days 30] [--tax-rate 0] [--currency USD|EUR|GBP|CAD|AUD|MXN] [--notes text]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, TodoWrite]
---

# Invoice Generator

The user wants to generate a professional, formatted invoice for a client. The output is both a markdown file and a print-ready HTML file.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract client name (required — ask if missing)
- Extract amount (total or individual line items — required)
- `--type` — invoice type: connection fee, TC fee, consulting, custom (auto-generates description)
- `--description` — service description (overrides auto-generated)
- `--due-days` — payment terms in days (default: 30)
- `--tax-rate` — tax percentage (default: 0)
- `--currency` — currency code (default: USD). Supported: USD, EUR, GBP, CAD, AUD, MXN
- `--notes` — additional notes for the invoice
- If missing client name or amount, ask the user before proceeding

### Step 1: Load Business Configuration
- Check for `brain/invoices/config.md`
  - If it exists, read business name, address, phone, email, payment methods, default terms
  - If it does NOT exist, ask the user for their business info:
    - Business name (and DBA if any)
    - Address
    - Phone and email
    - Payment methods (Zelle, wire, check, etc.)
    - Default payment terms
  - Save their answers to `brain/invoices/config.md` for future invoices

### Step 2: Look Up Client Info
- Check `brain/people/` for a file matching the client name
- If found, auto-populate: client company, address, email
- If not found, use whatever the user provided. Suggest creating a contact entry.

### Step 3: Generate Invoice Number
- Format: `INV-{YYYYMMDD}-{NNN}` (e.g., INV-20260302-001)
- Read `brain/invoices/config.md` for last used number
- Also scan `brain/invoices/` directories for existing invoice files to prevent conflicts
- Increment to the next available number
- Update config.md with the new last number

### Step 4: Calculate Totals
- For each line item: quantity x unit price = line total
- Subtotal: sum of all line totals
- Tax: subtotal x tax rate (default 0%)
- Discount: if specified by user
- **Total Due = Subtotal + Tax - Discount**
- Format all amounts according to the specified currency

### Step 5: Generate the Invoice Files
Create both formats:

1. **Markdown version:** `brain/invoices/{client-slug}/INV-{YYYYMMDD}-{NNN}.md`
   - Clean, readable markdown with all invoice details
   - Follows the template in the SKILL.md

2. **HTML version:** `brain/invoices/{client-slug}/INV-{YYYYMMDD}-{NNN}.html`
   - Professional, print-ready HTML with embedded CSS
   - Can be opened in any browser and printed or saved as PDF
   - Includes status badge (Unpaid/Paid)
   - Follows the HTML template in the SKILL.md

Create the `brain/invoices/` and `brain/invoices/{client-slug}/` directories if they do not exist.

### Step 6: Update Invoice Log
- Check for `brain/invoices/log.md`
- If it does not exist, create it with the header template
- Append the new invoice to the log table:

```markdown
| Invoice # | Date | Client | Amount | Currency | Status | Due Date |
|-----------|------|--------|--------|----------|--------|----------|
| INV-20260302-001 | 2026-03-02 | ABC Motors | $5,000.00 | USD | Sent | 2026-04-01 |
```

### Step 7: Report
- Display the invoice to the user (show the markdown version inline)
- Report both file locations (markdown and HTML)
- Tell them: "Open the HTML file in your browser to print or save as PDF."
- Show the invoice total and due date prominently
- Suggest next steps: send to client, track payment, add client to contacts if new
