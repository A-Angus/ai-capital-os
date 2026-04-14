# Decision Log — LEX AI OS

> All major architectural changes, dependency additions, and structural pivots are logged here **before** code is written. This is the source of truth for why the system is built the way it is.

**Format:**
```
## [YYYY-MM-DD] — Decision Title
**Decision:** What was decided
**Why:** The reason
**Impact:** What files/systems are affected
**Alternatives considered:** What else was evaluated
```

---

## [2026-03-22] — Workspace Initialization & Quality Infrastructure

**Decision:** Install `ruff` as the primary linter and formatter for the Python codebase. Add technical context sections to CLAUDE.md.

**Why:** The `telegram_bridge.py` script had 4 lint errors (unused imports, multi-line imports, unused variable). No code quality tooling was in place. Adding ruff provides fast, zero-config linting that catches issues before they cause runtime failures in the Telegram bridge.

**Impact:** `telegram_bridge.py`, `CLAUDE.md`, `ruff.toml` (new), `docs/` directory (new)

**Alternatives considered:** `flake8` + `black` (two tools vs one), `mypy` (type checking only — useful addition later), `pylint` (too verbose for this codebase size)

---

## [2026-03-22] — SUPERPOWERS Framework Implementation

**Decision:** Adopt phase-based conversation structure, docs/research/ directory, and Current Phase Status block in CLAUDE.md.

**Why:** Framework improves context retention across sessions by externalizing API docs, making phase status explicit, and enforcing pre-task context loading.

**Impact:** `CLAUDE.md` (new sections added), `docs/research/` directory created.

**Alternatives considered:** Keeping all context inline (rejected — causes token bloat over time). MCP server audit found no active servers to disable.

---

## [2026-03-22] — Full Stack Architecture Initialization

**Decision:** Updated CLAUDE.md with complete VPS service inventory, execution boundaries (Green/Yellow/Red zones), and full architecture layers including Flask orchestrator, OpenClaw, LexCapital Bot, and n8n.

**Why:** Previous CLAUDE.md only documented the local Telegram bridge. The actual production stack runs on DigitalOcean VPS (206.189.71.176) with 5 systemd-managed services. Execution boundaries prevent accidental simultaneous downtime of all bots.

**Impact:** `CLAUDE.md` — System Architecture section rewritten, Execution Boundaries section added, identity section updated with Legends Excel LLC and NBCU W2.

**Alternatives considered:** Keeping VPS details in a separate file — rejected because this is core architecture that every session needs.

---

## [2026-03-22] — Full Stack Architecture Expansion (Webhook Flow + n8n + Lender DB)

**Decision:** Added complete webhook flow (LexCapital Bot → n8n → GHL), GHL custom fields schema, n8n workflow inventory, all 3 webhook endpoints, lender database schema (4 tabs, 23 lenders), lender matching logic, and Layers 3–5 to CLAUDE.md.

**Why:** Previous architecture docs only captured Layers 1–2 and the local Telegram bridge. The n8n-to-GHL pipeline, lender matching rules (geographic filter first), and dead deal archival requirements were undocumented — critical context for building automations correctly.

**Impact:** `CLAUDE.md` — Architecture Layers section expanded, Lender Database Schema section added, Brand Rules updated with primary pitch and visual identity.

**Alternatives considered:** Separate files for n8n and lender DB schema — rejected because this is core operational context that every session needs without additional file reads.

---

## [2026-03-22] — Telegram Bridge Architecture Decision

**Decision:** Keep the bridge as a single-file script (`telegram_bridge.py`) that shells out to `/usr/bin/claude --print`.

**Why:** This architecture avoids the Anthropic SDK dependency and directly uses the installed Claude Code CLI, which already has session context, permissions, and brain file access. Adding the SDK would duplicate functionality and introduce auth complexity.

**Impact:** Deployment is simple — one Python file, one config JSON. No venv required beyond system packages.

**Alternatives considered:** Direct Anthropic SDK (`anthropic` Python package) — rejected because Claude CLI already handles auth and context injection.

---
