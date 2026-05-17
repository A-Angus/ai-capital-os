# Retrieval — Semantic Vault Search

**Tool:** `lex-retrieve` (CLI on this VPS as user `lexbot`).

**What it does:** embeds a natural-language query via the mini's Ollama (`nomic-embed-text`, 768-dim) over Tailscale, then runs cosine similarity against `public.vault_chunks` in the LEX Capital Engine Supabase project. Returns top-k chunks ranked by similarity.

**Two indexed roots:**
1. `~/Documents/LEX/CentralBrain/` on the mini — Obsidian vault (curated lender/deal/borrower/people/SOP notes, system plans)
2. `~/Documents/ai-workspace/ai-capital-os/brain/` on the mini (mirror of this VPS's `~/brain/` synced nightly) — pipeline logs, daily activity, identity, tracker

A 15-min launchd job on the mini re-indexes anything modified.

## Usage

```bash
# Basic
lex-retrieve "what's the status of the coalson deal"

# Filter by frontmatter type
lex-retrieve "fix and flip lender georgia" --type lender --top 5
lex-retrieve "who is benny anand" --type person

# Filter by source root (e.g. only curated vault)
lex-retrieve "deal sources" --root /Users/alex/Documents/LEX/CentralBrain

# Machine-readable
lex-retrieve "..." --json
```

## When to use

- Before drafting outreach: confirm what we already know about the borrower, lender, or deal.
- When a name surfaces in an email/Telegram message: pull every prior context.
- When a deal stalls: ask "what was the last lender note on X" to surface relevant follow-ups.
- For lender matching: `lex-retrieve "lender 100% financing GA fix and flip" --type lender`.

## When NOT to use

- Real-time deal status — use `~/brain/coordination/ACTIVE_TASKS.md` and `~/brain/tracker.md` directly.
- Structured pipeline queries (counts, sums, filters by status) — use Supabase pipeline tables (`deals`, `lenders`, `interactions`) directly via SQL or the Supabase MCP.
- New facts not yet in the vault — retrieval is only as fresh as the latest indexer run (worst case 15 min behind file changes).

## Env

`~/.config/lex/retrieve.env` holds `SUPABASE_DB_URL` (Session Pooler IPv4 URL), `OLLAMA_HOST=http://100.107.60.111:11434` (mini Tailscale), `EMBED_MODEL=nomic-embed-text`. The wrapper at `~/bin/lex-retrieve` sources it automatically.

## Hard requirement

Mini's Ollama must be reachable on Tailscale (`100.107.60.111:11434`). If the mini is offline, `lex-retrieve` fails fast with a clear error.
