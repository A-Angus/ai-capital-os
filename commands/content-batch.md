---
description: "Generate a batch of social media content (posts, captions, hooks, scripts) for a given topic or business."
argument-hint: "[topic/business] [--platforms ig,tiktok,youtube,x,fb,linkedin] [--count 5] [--tone professional|casual|bold]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch, TodoWrite]
---

# Content Batch

The user wants to generate a batch of ready-to-post social media content for a specific topic, product, or business.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract the topic or business name
- `--platforms` — which platforms to target (default: ig, tiktok, x)
- `--count` — number of pieces per platform (default: 5)
- `--tone` — writing tone (default: bold, direct — matching Mike's brand voice)
- If no topic provided, ask the user

### Step 1: Load Brand Context
- Read `~/.claude/brain/knowledge-base/mike-davis/02-brand-voice-and-philosophy.md` for tone
- Read `~/.claude/brain/knowledge-base/mike-davis/04-content-style-guide.md` for format rules
- If the topic relates to SellFi/TOP Wheels/T.O.P. Method, load relevant knowledge-base files

### Step 2: Research the Topic
- If the topic is broad, run a quick web search for trending angles, hooks, and pain points
- Identify 5-10 content angles that would resonate with the target audience
- Note any trending formats or hashtags

### Step 3: Generate Content by Platform
For each platform, generate the requested count of posts:

**Instagram:**
- Caption (with hook in first line, CTA at end)
- Suggested image/carousel concept
- Hashtag set (15-20 relevant tags)

**TikTok:**
- Hook (first 3 seconds)
- Script outline (15-60 seconds)
- Suggested text overlay / trending sound

**X (Twitter):**
- Tweet text (under 280 chars)
- Thread version if applicable
- Quote-tweet style engagement hooks

**YouTube:**
- Title options (curiosity-driven)
- Thumbnail concept
- Opening hook script (first 30 seconds)

**Facebook / LinkedIn:**
- Long-form post with storytelling angle
- Professional framing for LinkedIn

### Step 4: Package the Output
- Organize all content in a clean markdown format
- Group by platform
- Number each piece for easy reference
- Include a "Best 3" recommendation with reasoning

### Step 5: Save Output
- Save the batch to `~/.claude/brain/research/content-batch-YYYY-MM-DD-[topic-slug].md`
- Report the file location and total pieces generated
