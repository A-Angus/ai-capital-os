---
description: "Generate a content calendar for 1-4 weeks — posts mapped to platforms, dates, topics, and content types."
argument-hint: "[topic/business] [--weeks 1-4] [--platforms ig,tiktok,youtube,x,fb,linkedin] [--posts-per-day 1-10]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch, TodoWrite]
---

# Social Media Calendar

The user wants a structured content calendar with specific posts mapped to dates, platforms, and content types.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract the topic or business focus
- `--weeks` — how many weeks to plan (default: 2)
- `--platforms` — target platforms (default: ig, tiktok, x)
- `--posts-per-day` — posting frequency (default: 3)
- If no topic provided, default to Mike's brand (SellFi, T.O.P. Method, creative finance)

### Step 1: Load Context
- Read `~/.claude/brain/knowledge-base/mike-davis/04-content-style-guide.md` for content rules
- Read `~/.claude/brain/research/youtube-scripts-and-calendar.md` for existing plans
- Check `~/.claude/brain/goals.md` for current marketing goals
- Check for any upcoming events or launches that should be woven into content

### Step 2: Define Content Pillars
Establish 4-6 recurring content themes:
- **Educational:** Teach something (how creative finance works, deal breakdowns)
- **Authority:** Show results, share wins, demonstrate expertise
- **Engagement:** Ask questions, polls, controversial takes
- **Behind the Scenes:** Day-in-the-life, building in public
- **Promotional:** Product/service announcements, CTAs
- **Story/Personal:** Personal journey, lessons, authenticity

### Step 3: Build the Calendar
For each week, create a day-by-day plan:

```markdown
## Week [N]: [Mon Date] - [Sun Date]
**Theme:** [weekly theme or focus]

| Day | Platform | Content Type | Topic/Hook | Pillar | Status |
|-----|----------|-------------|------------|--------|--------|
| Mon | IG Reel | Educational | "Most people don't know you can..." | Education | [ ] |
| Mon | X | Thread | 5 things I learned from [topic] | Authority | [ ] |
| Tue | TikTok | Story | Behind the scenes of [deal/build] | BTS | [ ] |
...
```

### Step 4: Write Hooks and Captions
For each calendar entry, include:
- **Hook:** The first line / opening (attention-grabber)
- **Caption Outline:** 2-3 bullet points of what the post covers
- **CTA:** What the audience should do (comment, follow, DM, link in bio)
- **Hashtags:** Platform-appropriate tags (if applicable)

### Step 5: Add Strategic Notes
- Flag which posts are high-priority (launch tie-ins, trending topics)
- Note any posts that should reference each other (cross-platform threading)
- Suggest best posting times per platform
- Include content batching recommendations (which posts to shoot together)

### Step 6: Save Calendar
- Save to `~/.claude/brain/research/content-calendar-YYYY-MM-DD.md`
- Report the calendar overview and file location to the user
