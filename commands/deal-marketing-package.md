---
description: "Generate marketing materials for a deal — one-pager, social posts, listing copy, email blast, and buyer outreach."
argument-hint: "[property address or deal description] [--price amount] [--type vehicle|property|business] [--audience buyers|investors|agents]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch, TodoWrite]
---

# Deal Marketing Package

The user wants to create a full set of marketing materials for a specific deal — property, vehicle, or business opportunity.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract the deal details (address, description, key numbers)
- `--price` — asking price or terms
- `--type` — what's being marketed (vehicle, property, business)
- `--audience` — primary target audience
- If missing key details, ask for: what's being sold, price/terms, key selling points

### Step 1: Load Brand and Deal Context
- Read `~/.claude/brain/knowledge-base/mike-davis/02-brand-voice-and-philosophy.md`
- Read `~/.claude/brain/knowledge-base/mike-davis/04-content-style-guide.md`
- Check `~/.claude/brain/deal-packages/` for existing deal info
- If vehicle deal, load `~/.claude/brain/knowledge-base/sellfi-ecosystem/02-top-wheels-execution-arm.md`

### Step 2: Research (if needed)
- If property: pull property details, photos reference, neighborhood highlights
- If vehicle: pull market value, comparable listings, key specs
- Identify the strongest selling points and unique angles

### Step 3: Generate One-Pager

```markdown
# [Property/Vehicle/Deal] — [Address/Title]

## Highlights
- [Key selling point 1]
- [Key selling point 2]
- [Key selling point 3]

## The Numbers
| Detail | Value |
|--------|-------|
| Asking Price | $X |
| Estimated Value | $X |
| Monthly Payment | $X |
| Cash Flow | $X/mo |
| Terms | [seller finance / SubTo / cash] |

## Property/Vehicle Details
[Beds/baths/sqft OR year/make/model/miles]

## Location / Context
[Neighborhood highlights, school district, commute, or vehicle history]

## Why This Deal
[2-3 sentences on why this is a compelling opportunity]

## Contact
Mike Davis — TOP Wheels / SellFi
[contact method]
```

### Step 4: Generate Social Media Posts
Create platform-ready posts:

**Instagram/Facebook Post:**
- Eye-catching hook headline
- Key details in caption
- Call to action (DM, comment, link)
- Hashtag set

**Facebook Marketplace Listing:**
- Title, price, description optimized for marketplace

**Craigslist/Classified Ad:**
- Formatted for classified listing

**X (Twitter) Post:**
- Under 280 chars, punchy, CTA

### Step 5: Generate Email Blast Copy
- Subject line options (3 variations)
- Email body: hook, deal details, urgency/scarcity, CTA
- Keep under 200 words
- Mobile-friendly formatting

### Step 6: Generate Buyer Outreach Script
- Text message template (under 160 chars)
- DM template for social media
- Phone script outline (30-second pitch)

### Step 7: Package Everything
Save all materials to `~/.claude/brain/deal-packages/[deal-slug]/`:
- `one-pager.md`
- `social-posts.md`
- `email-blast.md`
- `outreach-scripts.md`

### Step 8: Report
- Display the one-pager
- List all files created
- Suggest distribution plan (which platforms, what order, timing)
