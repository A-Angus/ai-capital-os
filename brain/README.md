# Brain — Master Index

> **Purpose:** This is the central nervous system of your AI operating system. Single source of truth for goals, knowledge, processes, people, projects, and daily operations. Claude reads this file to understand the full knowledge base and pull the right context for any task.

**Last Updated:** 2026-03-05

---

## Directory Map

```
brain/
├── README.md                          ← YOU ARE HERE (index & usage guide)
├── goals.md                           ← Vision → yearly → quarterly → weekly priorities
│
├── coordination/                      ← Cross-session coordination layer
│   ├── INBOX_QUEUE.md                 ← Tasks queued for another bot/session to pick up
│   ├── ACTIVE_TASKS.md                ← Tasks currently in progress
│   ├── COMPLETED_ACTIONS.md           ← Log of completed actions across all sessions
│   └── LAST_SYNC.md                   ← Timestamp and summary of last state sync
│
├── knowledge-base/                    ← Domain expertise and business knowledge
│   └── (add files as AI learns your business)
│
├── people/                            ← Contact CRM
│   ├── README.md                      ← Contact index + ecosystem map
│   ├── _TEMPLATE.md                   ← Template for new contacts
│   ├── bryan-marriott.md
│   ├── brian-swinton.md
│   ├── mo-castro.md
│   ├── benny-anand.md
│   ├── sheun-ogunbeku.md
│   ├── kwami-fox.md
│   ├── gheorghe-cucu.md
│   ├── eric-fuller.md
│   └── mikey-transactional.md
│
├── loans.md                           ← Personal loans tracker (money lent to individuals)
│
├── deals/                             ← Deal pipeline and flow
│   ├── deals.md                       ← Active pipeline tracker
│   └── deal-sources.md                ← Deal flow network
│
├── lenders/                           ← Capital provider directory
│   ├── lenders.md                     ← Full lender and capital source database
│   └── _LENDER-TEMPLATE.md            ← Template for new lender profiles
│
├── sops/                              ← Standard Operating Procedures
│   ├── README.md                      ← SOP index
│   ├── _TEMPLATE.md                   ← Template for new SOPs
│   ├── borrower-deal-intake.md        ← ✅ Active
│   ├── deal-screening.md              ← ✅ Active
│   ├── lender-matching.md             ← ✅ Active
│   ├── capital-stack-structuring.md   ← 🔴 Draft
│   ├── deal-funding-coordination.md   ← 🔴 Draft
│   ├── deal-source-outreach.md        ← 🔴 Draft
│   ├── weekly-pipeline-review.md      ← 🔴 Draft
│   ├── borrower-follow-up.md          ← 🔴 Draft
│   ├── lender-relationship-management.md ← 🔴 Draft
│   └── marketplace-deal-routing.md    ← 🔴 Draft
│
├── projects/                          ← Active project tracker
│   ├── README.md                      ← Project dashboard
│   ├── _TEMPLATE.md                   ← Template for new projects
│   ├── lex-website.md                 ← LEX website build (Lovable + Supabase)
│   ├── ghl-crm.md                     ← GoHighLevel CRM setup
│   ├── borrower-intake-portal.md      ← Deal intake portal
│   └── blinq-rebrand.md               ← Digital business card rebrand
│
├── calendar/                          ← Annual planning system
│   └── README.md                      ← Calendar overview
│
└── daily/                             ← Daily logs and weekly reviews
    ├── README.md                      ← Log system overview
    ├── _TEMPLATE.md                   ← Daily log template
    └── YYYY-MM-DD.md                  ← Today's log (load if it exists)
```

---

## How to Use This Brain

### For You (Human)

| I want to... | Do this |
|-------------|---------|
| Add a new goal | Edit `goals.md` |
| Brain dump a thought | Tell AI "add this to the brain" — it files it automatically |
| Document a workflow | Copy `sops/_TEMPLATE.md` → fill in → add to index |
| Add a contact | Copy `people/_TEMPLATE.md` → fill in → add to index |
| Track a new project | Copy `projects/_TEMPLATE.md` → fill in → add to dashboard |
| Log today's work | Create `daily/YYYY-MM-DD.md` |
| Plan next month | Create `calendar/YYYY-MM.md` |
| Check pipeline | Ask AI for a pipeline update — it reads `deals/deals.md` |
| Find someone | Mention their name — AI looks them up automatically |

### For the AI — Session Behavior

**Start of session — always load:**
- `claude.md` — identity, brand rules, decision framework
- `brain/README.md` — this file
- `brain/goals.md` — current priorities and targets

**During session — load on demand:**

| Trigger | File(s) to Load |
|---------|----------------|
| New deal comes in | `deals/deals.md` + `sops/borrower-deal-intake.md` |
| Screening a deal | `sops/deal-screening.md` |
| Matching a deal to a lender | `lenders/lenders.md` + `sops/lender-matching.md` |
| Structuring a capital stack | `sops/capital-stack-structuring.md` |
| Someone mentioned by name | `people/README.md` → find their individual file |
| Deal source or outreach topic | `deals/deal-sources.md` + `sops/deal-source-outreach.md` |
| Pipeline update requested | `deals/deals.md` + `sops/weekly-pipeline-review.md` |
| Follow-up on a borrower | `sops/borrower-follow-up.md` |
| Lender relationship topic | `lenders/lenders.md` + `sops/lender-relationship-management.md` |
| Deal closing or coordination | `sops/deal-funding-coordination.md` |
| Platform or tech build topic | `sops/marketplace-deal-routing.md` + `projects/README.md` |
| Active project status | `projects/README.md` → find specific project file |
| Daily planning or review | `daily/` → today's log if it exists |

**End of session:**
- Log key decisions, updates, or new information to `daily/YYYY-MM-DD.md`

---

## Brain Rules

1. **One source of truth** — If it's in the brain, it's current. If it's not, it doesn't exist.
2. **AI can write** — The AI can add and update files here during sessions.
3. **Human reviews** — Alex approves major changes before they stick.
4. **Templates are law** — Always use `_TEMPLATE.md` files to keep format consistent.
5. **Keep it lean** — If a file hasn't been referenced in 30 days, archive or delete it.
6. **Naming convention** — All files: `kebab-case.md` · All dates: `YYYY-MM-DD`
7. **Load on demand** — Pull specific files when relevant. Don't bulk-read everything.

---

## Decision Framework — Quick Reference

When priorities conflict, follow this order:

1. Revenue-generating activities — borrower conversations and active deals
2. Deals currently in underwriting or structuring
3. Building systems that increase deal flow and automation
4. Strengthening lender relationships and capital sources
5. Content or marketing activities

---

## Active Deal Summary

| Deal | Borrower | Stage | Next Action |
|------|----------|-------|-------------|
| Houston flip | Sheun Ogunbeku | ❌ Dead | — |
| Cheltenham Ct | Kwami Fox | 🟢 Under Review | Follow up on lender inspection |
| Auto shop | Gheorghe Cucu | 🟢 Under Review | Receive financial statements |
| Kennedy Funding Texas Land | Jason Coalson / Coalson Excavation LLC | 🟡 Structuring | Collect parcel details, advance with Kennedy Funding |
| Construction Bridge | Nic Bray / ACJ Built LLC | 🟡 Structuring | Run deal intake checklist, identify lender |

*Always check `brain/deals/deals.md` for the most current status.*

---

## Key People — Quick Reference

| Name | Role | Priority |
|------|------|----------|
| Bryan Marriott | Collaborator / deal source | 🔴 High |
| Brian Swinton | Confidant / deal source | 🔴 High |
| Sheun Ogunbeku | Borrower — Houston flip (dead) | 🟢 Low |
| Kwami Fox | Borrower — Cheltenham Ct | 🔴 High |
| Benny Anand | Lender — Rehab Financial Group | 🟡 Medium |
| Gheorghe Cucu | Borrower — Auto shop | 🟡 Medium |
| Eric Fuller | Capital partner — 100% financing | 🟡 Medium |
| Carrol Walton Grizzle | Private lender — gap capital | 🟡 Medium |

*Always check `brain/people/README.md` for full context on any individual.*

---

## How to Add New Files

### New contact
1. Copy `brain/people/_TEMPLATE.md`
2. Rename: `firstname-lastname.md`
3. Add to `brain/people/README.md` index
4. Add to Key People table above if priority is 🔴 High

### New lender
1. Copy `brain/lenders/_LENDER-TEMPLATE.md`
2. Rename: `lender-name.md`
3. Add a row to the appropriate table in `brain/lenders/lenders.md`

### New deal
1. Add entry to `brain/deals/deals.md`
2. Create or update borrower file in `brain/people/`
3. Note deal source in `brain/deals/deal-sources.md` if applicable

### New project
1. Copy `brain/projects/_TEMPLATE.md`
2. Rename: `project-name.md`
3. Add to `brain/projects/README.md` dashboard
4. Add to directory map above

### New SOP
1. Copy `brain/sops/_TEMPLATE.md`
2. Rename: `sop-name.md`
3. Add to `brain/sops/README.md` index
4. Add to directory map above

### Log today's work
1. Create `brain/daily/YYYY-MM-DD.md` using `daily/_TEMPLATE.md`

### Plan next month
1. Create `brain/calendar/YYYY-MM.md`

---

## System Health Checklist

Run weekly to keep the brain current:

- [ ] `deals/deals.md` — all active deals have a current stage and next step
- [ ] `goals.md` — weekly priorities updated, quarterly status emojis current
- [ ] `people/` — contact files reflect latest deal status and conversation notes
- [ ] `lenders/lenders.md` — new lenders added, criteria current
- [ ] `projects/README.md` — active project statuses updated
- [ ] `daily/` — this week's log exists if using daily logging
- [ ] Any file not referenced in 30+ days — archive or delete

---

## AI Operating Principle

> The brain is only as useful as it is current. If information lives only in Alex's head and not in these files, the AI cannot use it. Every deal, contact, lender, and decision should be captured here.
>
> The more you feed it, the smarter it gets. Start with `goals.md` — everything flows from there.
