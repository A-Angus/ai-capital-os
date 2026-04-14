---
description: "Plan full trip logistics — flights, hotels, transportation, daily itinerary, restaurants, packing list, and pre-trip preparation timeline."
argument-hint: "[destination] [dates] [purpose] [--budget low|mid|high] [--focus flights|hotels|food|packing|itinerary] [--travelers number]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch, TodoWrite]
---

# Travel Plan

The user wants to plan a trip — full logistics from flights to packing to daily itinerary.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract destination (required — ask if missing)
- Extract dates (required — ask if missing; accept "next week", "March 4-8", "3 nights", etc.)
- Extract purpose (ask if not obvious: business, conference, vacation, property visit, etc.)
- `--budget` — low (hostel/budget), mid (standard business), high (luxury/no constraint)
- `--focus` — narrow the plan to a specific section: flights, hotels, food, packing, or itinerary
- `--travelers` — number of people traveling (default: 1)
- If the user mentions a specific event or conference, search for its venue and schedule

### Step 1: Load Context
- Read user profile from `brain/identity/` or CLAUDE.md for preferences and home city
- Check `brain/calendar/` for any existing events during the travel dates
- Check `brain/people/` for contacts in the destination city (potential meetings)
- If departure city is unknown, ask: "Where are you flying from?"

### Step 2: Research the Destination
Use WebSearch to gather:
- Weather for the destination during the travel dates
- Best neighborhoods to stay (relevant to trip purpose)
- Airport and ground transportation options
- Event/conference details (if applicable)
- Restaurant recommendations near key locations
- Any travel advisories or major events that could affect the trip

### Step 3: Generate the Trip Brief

**Full plan (default):**

```markdown
# Trip Brief: {Destination} — {Dates}
> **Purpose:** {purpose}
> **Created:** {date}

## Flight Search
| Parameter | Recommendation |
|-----------|---------------|
| Route | {origin} → {destination} |
| Outbound | {date} — depart {time recommendation} |
| Return | {date} — depart {time recommendation} |
| Airlines | {top options for this route} |
| Book on | Google Flights, Kayak, airline direct |

## Hotel Recommendations
### Option 1: {Best Overall}
- **Why:** {reason} | **Price:** ${X}/night | **Area:** {neighborhood}
### Option 2: {Best Value}
### Option 3: {Best Location}

## Ground Transportation
| Option | Cost | Time | Best For |
|--------|------|------|---------|
| Rideshare | ${X} | {X} min | Convenience |
| Rental car | ${X}/day | | Multiple stops |
| Public transit | ${X} | {X} min | Budget |
**Recommended:** {option and why}

## Daily Itinerary
### Day 1 — {Date} — Travel
| Time | Activity | Location | Notes |
|------|----------|----------|-------|
### Day 2 — {Date} — {Theme}
| Time | Activity | Location | Notes |
|------|----------|----------|-------|
(continue for each day)

## Restaurants
### Near Hotel
| Name | Cuisine | Price | Best For |
|------|---------|-------|---------|
### Near Venue/Meetings
| Name | Cuisine | Price | Best For |
|------|---------|-------|---------|
### Client Dinner / Special
| Name | Cuisine | Price | Why |
|------|---------|-------|-----|

## Packing Checklist
### Essentials
- [ ] ID / passport
- [ ] Phone + charger
- [ ] Laptop (if business)
### Clothing ({weather summary})
- [ ] {items based on weather and purpose}
### Business
- [ ] Business cards
- [ ] Presentation materials

## Pre-Trip Timeline
### 1 Week Before
- [ ] Book flights + hotel
- [ ] Confirm meetings
### 3 Days Before
- [ ] Check flight status
- [ ] Download offline maps
### Day Before
- [ ] Pack
- [ ] Set alarm

## Emergency Info
- Hotel: {name, address, phone}
- Nearest hospital: {name}
- Local emergency: {number}
```

**Focused plan (--focus):**
- Only generate the requested section plus a brief executive summary
- For `--focus flights`: flight search + tips only
- For `--focus hotels`: hotel recommendations + neighborhood guide only
- For `--focus food`: restaurant suggestions organized by meal and location
- For `--focus packing`: weather-aware packing checklist only
- For `--focus itinerary`: day-by-day schedule only

### Step 4: Save and Report
- Display the full trip brief in terminal
- Save to `brain/research/travel-{destination-slug}-{YYYY-MM-DD}.md`
- If `brain/research/` does not exist, create it
- Add the trip dates to `brain/calendar/` if a calendar file exists for that month
- Report the file location so the user can reference it later
