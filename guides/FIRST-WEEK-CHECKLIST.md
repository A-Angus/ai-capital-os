# Your First Week with AI OS Blueprint

> **Purpose:** This is your guided 7-day onboarding. Each day takes 15-30 minutes and unlocks a new layer of your AI Operating System. By Day 7, you'll have a fully customized AI that knows your business, tracks your goals, and works the way you think.
>
> **The rule:** Don't skip days. Each one builds on the last. The investment you make this week pays dividends for months.

---

## Day 1: Install and Identity

**Time:** 20 minutes
**Goal:** Get installed and teach your AI who you are.

- [ ] **Run the Magic Install** -- Open the Claude desktop app, click the **Code** tab, then open `MAGIC-INSTALL.md`, copy the prompt, paste into Claude Code. Wait for the success report.
- [ ] **Open ~/CLAUDE.md** in any text editor (VS Code, TextEdit, Notepad, whatever you use)
- [ ] **Fill in "Who You Are"** -- Your name, business name, industry, and role. Be specific. "Real estate investor" is okay. "Fix-and-flip investor specializing in off-market distressed properties in the Dallas-Fort Worth metro" is better.
- [ ] **Fill in "Your Brand Rules"** -- How is your company name written? What's your website? What tone should your AI use? What should it never say?
- [ ] **Fill in "Decision Framework"** -- When two things compete for your time, which wins? Revenue work? Client deadlines? Building? List your priorities in order.
- [ ] **Test it:** Open a new Claude Code session and ask: *"Who am I and what are my priorities?"*

**What you should see:** Claude responds with YOUR name, YOUR business, YOUR priorities -- not generic answers. If it does, Day 1 is done. Your AI knows you.

**Troubleshooting:**
- If Claude gives generic answers, make sure ~/CLAUDE.md exists and has content
- If Claude can't find your files, make sure the Magic Install completed successfully
- Try starting a new Claude Code session -- it reads CLAUDE.md fresh on startup

---

## Day 2: Goals and Vision

**Time:** 30 minutes
**Goal:** Give your AI a map of where you're going and what matters right now.

- [ ] **Open ~/.claude/brain/goals.md** in your text editor
- [ ] **Fill in "Long-Term Vision"** -- Where do you want to be in 3-5 years? Business, wealth, lifestyle, legacy. Even rough answers are valuable. You can refine later.
- [ ] **Fill in "1-Year Goals"** -- What are 3-5 things you want to accomplish this year? Add real metrics: "Launch product by June" or "Hit $50K/month revenue."
- [ ] **Fill in "This Quarter"** -- What are the top 3 objectives for this quarter? These should connect to your 1-year goals.
- [ ] **Fill in "Monthly Focus"** -- What's this month's theme? What are the top 3 priorities?
- [ ] **Fill in "Weekly Priorities"** -- What are the 3 most important things for THIS week?
- [ ] **Fill in "Decision Framework"** -- This tells your AI how to prioritize when you have conflicting tasks
- [ ] **Test it:** Run `/project-pulse` in Claude Code

**What you should see:** Claude references your goals, flags what's on track vs. behind, and gives you a status dashboard. It might say "No projects found yet" -- that's fine, you'll add them tomorrow.

**Troubleshooting:**
- If `/project-pulse` doesn't work, make sure ~/.claude/commands/project-pulse.md exists
- If Claude doesn't reference your goals, double-check that ~/.claude/brain/goals.md has content

**Pro tip:** Spend the most time on the Decision Framework. This single section determines how your AI triages every request you make. Get it right and your AI makes better calls about what to prioritize.

---

## Day 3: Projects and People

**Time:** 25 minutes
**Goal:** Load your AI with what you're actively working on and who matters in your business.

### Add Your Projects

- [ ] **Open ~/.claude/brain/projects/README.md**
- [ ] **Add your 3 most important active projects** to the Dashboard table. For each project, fill in: name, category, status, priority, and next action.
- [ ] **(Optional) For complex projects:** Copy `~/.claude/brain/projects/_TEMPLATE.md` to a new file like `my-project-name.md` and fill in the details

### Add Your Key Contacts

- [ ] **Copy the people template** for each of your 5 most important contacts:
  - Copy `~/.claude/brain/people/_TEMPLATE.md` to `~/.claude/brain/people/firstname-lastname.md`
  - Fill in their name, role, contact info, and relationship context
  - Repeat for each person
- [ ] **Update the index** at `~/.claude/brain/people/README.md` -- add each person to the table
- [ ] **Test it:** Ask Claude: *"What am I working on?"*

**What you should see:** Claude lists your active projects with their status and next actions. If you mention a contact by name, Claude should know who they are.

**Troubleshooting:**
- Make sure you updated the README.md dashboard, not just created individual files
- File names must be kebab-case: `john-smith.md`, not `John Smith.md`

**Pro tip:** You don't need to add everyone right now. Just add the people you'll mention most often. You can always say "Add Sarah to my contacts" later and your AI will create the file.

---

## Day 4: Try 5 Power Commands

**Time:** 20 minutes
**Goal:** Experience what your AI can actually do. These are the commands you'll use most.

- [ ] **Run `/brain-dump`** -- Type: `/brain-dump Remember that [something relevant to your business]`
  - *What happens:* Claude files this information in the right brain location automatically. You just captured knowledge that your AI will remember forever.

- [ ] **Run `/deep-research`** -- Type: `/deep-research [a topic relevant to your industry]`
  - *What happens:* Claude researches the topic across the web and generates a structured report. Gets saved to your brain's research folder.

- [ ] **Run `/content-batch`** -- Type: `/content-batch Create 10 social media posts about [your business topic]`
  - *What happens:* Claude generates 10+ ready-to-post social media updates tailored to your brand voice (from CLAUDE.md).

- [ ] **Run `/email-drafter`** -- Type: `/email-drafter Draft a follow-up email to [contact] about [topic]`
  - *What happens:* Claude drafts a professional email in your brand voice. If the contact is in your people/ directory, it uses their context.

- [ ] **Run `/project-pulse`** -- Type: `/project-pulse`
  - *What happens:* Claude checks all active projects, compares against your goals, and gives you a health dashboard.

**What you should see:** Each command produces real, usable output -- not generic filler. The content matches your brand voice, references your goals, and uses context from your brain files.

**Troubleshooting:**
- If a command isn't recognized, check that the .md file exists in ~/.claude/commands/
- If output is generic, make sure CLAUDE.md and goals.md are filled in -- these are what make output personalized
- Try starting a fresh Claude Code session if commands seem stale

**Pro tip:** These 5 commands alone can save you 5-10 hours per week. Brain-dump captures ideas instantly. Deep-research replaces hours of Googling. Content-batch gives you a week of posts in 2 minutes.

---

## Day 5: Build Your First SOP

**Time:** 20 minutes
**Goal:** Document one repeatable process so your AI can run it (or help you run it) forever.

- [ ] **Pick one repeatable process** in your business. Examples:
  - How you onboard a new client
  - How you respond to an inbound lead
  - How you prepare for a weekly meeting
  - How you process an invoice
  - How you create content for social media

- [ ] **Run `/sop-builder`** -- Type: `/sop-builder [describe your process in plain English]`
  - Example: `/sop-builder When a new lead comes in, I check their info, send a welcome email, add them to my CRM, and schedule a discovery call within 48 hours`

- [ ] **Review the SOP** -- Claude generates a structured SOP with steps, triggers, and expected outcomes
- [ ] **Edit if needed** -- The SOP lives in `~/.claude/brain/sops/`. Open the file and tweak anything that doesn't match how you actually do it.
- [ ] **Verify it's indexed** -- Check that `~/.claude/brain/sops/README.md` lists your new SOP

**What you should see:** A clean, step-by-step SOP saved to your brain. Next time you (or your AI) need to run this process, the SOP is right there.

**Troubleshooting:**
- If the SOP output is too generic, give more detail in your description
- You can always edit the .md file directly -- it's just a text file

**Pro tip:** The SOPs you write this week become the playbooks your AI follows autonomously. The more specific you are, the less you have to supervise. Write them like you're training a sharp new employee who takes notes on everything.

---

## Day 6: Go Deeper

**Time:** 30 minutes
**Goal:** Explore the skills that match your specific industry and start customizing.

### For Everyone

- [ ] **Run `/market-research [your industry or niche]`** -- Get market size, trends, and opportunities
- [ ] **Run `/competitor-analysis [competitor name or niche]`** -- Research competitive landscape
- [ ] **Run `/weekly-review`** -- Even if it's not the end of the week, see what it generates. This is the command you'll run every Friday.

### For Real Estate Investors (Bonus Skills)

- [ ] **Run `/deal-analyzer [property address or deal details]`** -- Analyze cash flow, ROI, cap rate
- [ ] **Run `/property-research [address]`** -- Deep dive on any property
- [ ] **Run `/rental-analysis [address or area]`** -- Rental market analysis
- [ ] **Run `/investment-calculator`** -- BRRRR, flip, buy-and-hold, or seller finance calculations
- [ ] **Run `/deal-marketing-package [deal details]`** -- Generate marketing materials for a deal
- [ ] **Run `/seller-outreach-drafter [seller situation]`** -- Personalized seller outreach letters

### Build Your First Custom Skill (Optional, Advanced)

- [ ] **Read `~/.claude/HOW-TO-ADD-SKILLS.md`** -- This is the complete guide to extending your AI OS
- [ ] **Think of something you do repeatedly** that isn't covered by the existing skills
- [ ] **Create a new skill folder** at `~/.claude/skills/your-skill-name/SKILL.md`
- [ ] **Use the template** from HOW-TO-ADD-SKILLS.md to structure it

**Pro tip:** You don't need to build custom skills right away. The 35 built-in skills cover most business operations. But knowing HOW to build them means your AI OS grows with you.

---

## Day 7: Your First Weekly Review

**Time:** 15 minutes
**Goal:** Close the loop. See how your AI summarizes your week and plan the next one.

- [ ] **Run `/weekly-review`**
  - *What happens:* Claude reads your goals, projects, and any daily logs to generate a complete week-in-review. It flags what's on track, what slipped, and suggests priorities for next week.

- [ ] **Review the output** -- Does it match reality? Is anything missing?
  - If things are missing, it means you haven't been logging them. That's fine -- just start using `/brain-dump` more often and your weekly reviews will get richer over time.

- [ ] **Update your weekly priorities** -- Open `~/.claude/brain/goals.md` and update the "Weekly Priorities" section for next week

- [ ] **Reflect on the week:**
  - Which commands did you find most useful?
  - What felt like it should exist but doesn't? (That's your next custom skill.)
  - Is your Decision Framework accurate, or did you discover new priorities?

**What you should see:** A structured summary of your week that actually reflects your work, connected to your goals and projects. This is your AI operating system working as designed.

---

## What Happens After Day 7

You now have a fully operational AI OS. Here's how to keep it sharp:

**Daily habits (2 minutes each):**
- Use `/brain-dump` to capture ideas, notes, and learnings as they happen
- Ask Claude questions about your business -- it has context now

**Weekly habits (15 minutes):**
- Run `/weekly-review` every Friday
- Update `goals.md` weekly priorities section
- Add new contacts, projects, and SOPs as they come up

**Monthly habits (30 minutes):**
- Review goals.md -- are quarterly objectives still right?
- Create a monthly calendar file in `brain/calendar/`
- Archive completed projects and outdated SOPs

**The compound effect:** Your AI OS gets smarter every day you use it. Every brain-dump, every SOP, every contact you add -- it all compounds. In 30 days, your AI will know your business better than any human assistant could learn in 6 months. In 90 days, it's indispensable.

---

## Quick Reference -- All 35 Commands

| Command | What It Does |
|---------|-------------|
| `/morning-briefing` | CEO-level daily briefing: priorities, fires, deadlines |
| `/negotiation-prep` | Full negotiation strategy: research, BATNA, objection scripts |
| `/swot-analysis` | Strategic SWOT analysis with GO/NO-GO verdict |
| `/follow-up` | Track commitments, deadlines, promises |
| `/inbox-triage` | 4-tier email categorization + draft responses |
| `/meeting-prep` | Pre-meeting intelligence brief |
| `/meeting-to-actions` | Parse meeting notes into action items |
| `/project-pulse` | Status dashboard for all projects |
| `/weekly-review` | Weekly summary + next week planning |
| `/content-batch` | Generate batch social media content |
| `/content-repurpose` | One piece of content → 10+ platform versions |
| `/social-media-calendar` | Plan content across platforms |
| `/email-drafter` | Draft professional emails |
| `/hiring-screener` | Full hiring package: job post, screening, scorecard |
| `/personal-brand-audit` | Comprehensive brand analysis + 30-day plan |
| `/seller-outreach-drafter` | Personalized seller outreach |
| `/deep-research` | Deep dive research report on any topic |
| `/competitor-analysis` | Competitive landscape analysis |
| `/market-research` | Market size, trends, opportunities |
| `/financial-snapshot` | Executive financial summary: P&L, cash flow |
| `/kpi-dashboard` | Track KPIs with trend analysis |
| `/pipeline-sync` | Pipeline intelligence + revenue forecast |
| `/brain-dump` | Capture any thought -- AI files it automatically |
| `/sop-builder` | Create SOPs from descriptions |
| `/client-onboarding` | New client setup workflow |
| `/contract-review` | Review contracts: risks, leverage, redlines |
| `/travel-plan` | Full trip logistics: flights, hotels, itinerary |
| `/networking-intel` | Pre-event intelligence + follow-up templates |
| `/invoice-generator` | Generate professional invoices |
| `/deal-analyzer` | Analyze RE deals (cash flow, ROI, cap rate) |
| `/rental-analysis` | Rental market analysis |
| `/property-research` | Deep dive on any property |
| `/deal-marketing-package` | Marketing materials for a deal |
| `/lead-tracker` | Track leads through pipeline stages |
| `/investment-calculator` | BRRRR, flip, hold, seller finance calculations |

---

*You bought this system because you want your AI to actually know your business. This first week is how that happens. Don't rush it, don't skip days, and don't overthink it. Fill in the files, run the commands, and let the system do its job.*
