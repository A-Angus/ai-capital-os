---
description: "Take one piece of content and generate 10+ derivative pieces for every platform — Twitter/X thread, LinkedIn, Instagram, TikTok, email, Facebook, YouTube Short, blog summary, quote graphics, and a repurposing calendar."
argument-hint: "[source-content-or-path] [--voice casual|professional|bold|educational] [--platforms all|twitter,linkedin,instagram]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch, TodoWrite]
---

# Content Repurposer

The user wants to take a single piece of content and generate multiple derivative pieces optimized for different platforms.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Determine the source content:
  - If text is provided inline, use it directly
  - If a file path is provided, read the file
  - If a URL is provided, fetch and extract the content
  - If a reference ("that blog post about X"), search brain/drafts/, brain/daily/, brain/research/
- `--voice` — tone override: casual, professional, bold, educational (default: match source content voice)
- `--platforms` — which platforms to generate for (default: all)
- If no source content can be identified, ask: "What content do you want me to repurpose? Paste it, give me a file path, or tell me what to find in the brain."

### Step 1: Analyze Source Content
Extract from the source:
- **Core message** — the single most important takeaway
- **Key points** — 3-7 supporting arguments or ideas
- **Quotable lines** — phrases that stand alone as powerful statements
- **Data/statistics** — any numbers or proof points
- **Stories/examples** — narrative elements
- **Emotional hook** — what feeling does this trigger?
- Check `~/.claude/brain/knowledge-base/` for brand voice settings

### Step 2: Generate Platform Content
Produce each piece adapted to platform norms:

1. **Twitter/X Thread** (5-12 tweets) — Hook tweet + thread body + closer. Under 280 chars per tweet. No hashtags except final tweet.
2. **LinkedIn Post** (1200-1500 chars) — Pattern-interrupt opener, short paragraphs, personal angle, question CTA, 3-5 hashtags.
3. **Instagram Caption** (150-300 words) — Hook in first 125 chars, storytelling format, CTA, dot-separated hashtags (15-25), visual suggestion.
4. **TikTok Script** (30-60s) — 3-second hook, timestamped script, caption, sound suggestion.
5. **Email Newsletter Snippet** (150-250 words) — 3 subject line options, preview text, conversational body, single CTA.
6. **Facebook Post** (100-300 words) — Question opener, shareable format, minimal hashtags.
7. **YouTube Short Script** (30-60s) — Keyword-rich title, timestamped script, description, tags.
8. **Blog Summary** (200-400 words) — SEO headline, meta description, key takeaways.
9. **Quote Graphics Text** (5-8 quotes) — Under 20 words each, design notes.
10. **Repurposing Calendar** — 2-week day-by-day distribution plan with platform, content piece, and timing notes.

### Step 3: Voice Calibration
- If brand voice file exists in brain/knowledge-base/, match it across all pieces
- If not, match the tone of the source content
- Adapt tone per platform (Twitter = punchy, LinkedIn = professional-personal, TikTok = fast/direct, Email = intimate)

### Step 4: Save and Report
- Save to `~/.claude/brain/drafts/repurposed-{slug}-{YYYY-MM-DD}.md`
- Create brain/drafts/ if it does not exist
- Report: total pieces generated, the Twitter hook tweet, the 2-week calendar, file location
- Offer to adjust voice, add more pieces, or customize for specific platforms