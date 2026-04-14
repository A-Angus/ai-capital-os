---
description: "Process and prioritize emails/messages — categorize by urgency, draft responses for critical items, create action items."
argument-hint: "[paste emails or describe inbox contents]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebSearch, TodoWrite]
---

# Inbox Triage

The user wants to process their emails or messages and get them sorted by priority with draft responses for urgent items.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- If $ARGUMENTS contains email content (From:, Subject:, body text): Process those emails directly
- If $ARGUMENTS describes the inbox ("I have 15 emails from..."): Work with the description, ask for detail on potentially urgent items
- If $ARGUMENTS is empty: Ask: "Paste your emails or describe what's in your inbox. I'll sort by priority and draft responses for the urgent ones."
- Check for modifiers: "urgent only", "draft all responses", "focus on [person/project]"

### Step 1: Gather Context from Brain

Before triaging, read for context:
1. `brain/people/README.md` — Scan for any senders in the CRM. Read their files if found.
2. `brain/goals.md` — What are current priorities? Emails aligned with goals get priority boost.
3. `brain/projects/README.md` — Are any emails related to active projects?
4. `brain/pipeline/follow-ups.md` — Are any emails responses to tracked follow-ups?

This context is critical. An email from a random name is 🟢. The same email from someone in the CRM tagged 🔴 priority is 🟡 or 🔴.

### Step 2: Parse All Items

For each email or message, extract:
- **Sender** — Who it's from
- **Subject/Topic** — What it's about
- **Key content** — The core ask or information
- **Urgency signals** — Deadlines, money, legal, relationship importance
- **Brain connections** — Is this person/project in the brain?

### Step 3: Categorize Each Item

Apply these rules in priority order:

| Priority | Criteria |
|----------|---------|
| 🔴 URGENT | Revenue at risk, deadline <24h, key relationship, legal/financial, time-sensitive opportunity |
| 🟡 IMPORTANT | Needs response today, active project, client/partner, deadline <1 week |
| 🟢 LOW | Can wait 2-3 days, informational, no response needed, batch-processable |
| 🗑️ IGNORE | Newsletters, spam, marketing, irrelevant notifications |

**Brain-aware boosts:**
- Sender in people/ with 🔴 priority → bump up one category
- Email references active 🔥 Behind project → bump to 🔴
- Email resolves a tracked follow-up → flag it specifically

### Step 4: Draft Responses (URGENT Items)

For every 🔴 item, write a complete, send-ready draft:
- Match sender's tone and formality
- First sentence = the point (no throat-clearing)
- Include clear next step or call to action
- Keep it concise — 3-6 sentences unless complexity demands more
- Use brain context (relationship, project, history) to personalize

### Step 5: Create Action Items (IMPORTANT Items)

For every 🟡 item, specify:
- What action to take
- Who it involves
- Suggested deadline for response
- Whether it should be added to follow-up tracker

### Step 6: Generate Triage Report

Print the full report:

```
================================================================
  INBOX TRIAGE — [Today's Date]
  [X] items | [X] urgent | [X] important | [X] low | [X] ignore
================================================================

🔴 URGENT — Respond Now
═══════════════════════
[For each: sender, subject, why urgent, full draft response, notes]

🟡 IMPORTANT — Respond Today
═════════════════════════════
[For each: sender, subject, specific action, deadline]

🟢 LOW PRIORITY — Batch Later
══════════════════════════════
[For each: sender, subject, brief note on what to do]

🗑️ IGNORE — Delete or Unsubscribe
═══════════════════════════════════
[For each: sender, subject, reason to skip]

────────────────────────────────────
ACTION ITEMS CREATED:
- [ ] [Action items from all categories]

FOLLOW-UPS TO ADD:
- [Items that should be tracked in follow-up system]

PEOPLE TO ADD TO CRM:
- [New contacts worth tracking]
════════════════════════════════════
```

### Step 7: Offer Next Actions

After the triage report:
- "Want me to save these action items to your follow-up tracker?"
- "Want me to adjust any draft responses before you send them?"
- "Should I add any of these people to your CRM (brain/people/)?"
- "Want me to flag any patterns? (e.g., 'You're getting 5 newsletters you never read — want to unsubscribe?')"

### Handling Edge Cases

- **Suspicious emails:** Flag immediately: "This looks like phishing — [reason]. Do not click links or respond."
- **Very large inbox (30+):** Process 🔴 urgent first, then ask if user wants the rest triaged
- **All low priority:** "Nothing urgent. [X] items to batch, [X] to delete. Your inbox is clean."
- **Vague descriptions:** Ask for detail only on potentially urgent items: "The one from the lawyer — what's the subject? That could be urgent."
- **Thread/conversation:** Group related emails together, triage the thread as one item