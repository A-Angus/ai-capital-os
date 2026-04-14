---
description: "Review any contract or legal document — executive summary, key terms, financial obligations, risk flags, and negotiation leverage points."
argument-hint: "[file-path] [--compare file-path-2] [--focus risks|financials|termination|negotiation] [--brief]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebSearch, TodoWrite]
---

# Contract Review

The user wants a contract or legal document reviewed — summarized in plain English with key terms, financial obligations, risk flags, and negotiation points identified.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract file path (if provided) — supports `.txt`, `.md`, `.pdf`
- `--compare` — second file path for side-by-side version comparison
- `--focus` — narrow the review to a specific area: risks, financials, termination, or negotiation
- `--brief` — short-form review (executive summary + risk flags only, skip the deep dive)
- If no arguments and no pasted text, ask for the contract

### Step 1: Get the Contract Text
- **File path provided:** Read the file (use PDF reading for .pdf files)
- **Text pasted in message:** Use the pasted text directly
- **Both file and paste:** Use the file, treat pasted text as context/notes
- If the file does not exist, report the error and ask for the correct path
- If the document is very short (< 100 words), flag it as potentially incomplete

### Step 2: Classify the Document
Identify:
- Document type (NDA, MSA, SOW, lease, operating agreement, LOI, employment, vendor, licensing, partnership, etc.)
- Parties involved
- Effective date and term
- Governing jurisdiction
- Complexity level (Simple / Moderate / Complex)

### Step 3: Generate the Review

**Full review (default):**

```markdown
# Contract Review: {Type} — {Parties}
> **Reviewed:** {date}
> **Type:** {type} | **Complexity:** {level}
> **Parties:** {A} and {B}

## DISCLAIMER
AI-generated analysis. Not legal advice. Have a licensed attorney review before signing.

## Executive Summary
{One paragraph: what this contract does, who does what, how much money, how long, how to exit.}

## Key Terms
| Term | Details | Section |
|------|---------|---------|
| {term} | {details} | {ref} |

## Financial Obligations
### What You Pay
| Obligation | Amount | Frequency | Conditions | Section |
|-----------|--------|-----------|-----------|---------|

### Total Exposure
- Year 1 cost: ${X}
- Full term cost: ${X}
- Maximum liability: ${X}
- Exit cost: ${X}

## Termination & Exit
| Method | Notice | Penalty | Conditions | Section |
|--------|--------|---------|-----------|---------|
- Auto-renew: {Yes/No}
- Opt-out window: {X days before renewal}
- Post-termination obligations: {list}

## Risk Flags
| # | Risk | Severity | Section | Impact |
|---|------|----------|---------|--------|
| 1 | {risk} | HIGH/MED/LOW | {ref} | {real-world impact} |

## Negotiation Leverage
### Must-Change
1. **{clause}** — Current: {X} → Recommend: {Y}
   **Suggested language:** "{redline text}"

### Should-Change
1. **{clause}** — Current: {X} → Recommend: {Y}

## Questions to Ask Before Signing
1. {question raised by a risk or ambiguity}

## Verdict
**Assessment:** {FAVORABLE / MOSTLY FAIR / NEEDS NEGOTIATION / UNFAVORABLE / DO NOT SIGN}
**Risk Level:** {LOW / MODERATE / HIGH / CRITICAL}
**Next Step:** {sign / negotiate X items / attorney review Section Y / walk away}
```

**Brief review (--brief):**
- Executive Summary only
- Risk Flags only
- Verdict only

**Focused review (--focus):**
- Executive Summary (always included)
- Only the requested section (risks, financials, termination, or negotiation)
- Verdict

**Comparison review (--compare):**
- Side-by-side diff of every changed term
- Which changes favor which party
- Recommendation on which version to sign

### Step 4: Save the Review
- Save to `brain/research/contract-review-{type-or-counterparty-slug}-{YYYY-MM-DD}.md`
- If `brain/research/` does not exist, create it
- Report the file location to the user
- Append a one-line entry to today's daily log: "Contract reviewed: {type} with {counterparty} — Verdict: {verdict}"
