# ops_safety.md — Live Infrastructure Rules

Any action that affects live infrastructure must:

1. Be explicitly confirmed by Alex before execution. No assumed authorization. No "I'll just do it since it's small."
2. Include rollback awareness. Before the action, state how to undo it. If you can't state the rollback, you can't take the action.
3. Show a backup or snapshot path for anything destructive. Touching configs, restarting services, killing processes, editing crontabs, modifying systemd units, rotating tokens, dropping tables, removing files — all require this.
4. Default to dry-run when ambiguous. If the request could be interpreted as "show me what would happen" vs "make it happen," show first, ask second.

Scope: this applies to /opt/, /etc/, /home/lexbot/.claude/, systemd, cron, running processes, network configs, GHL/Telegram/Google API tokens, the orchestrator, and any production database. It does NOT apply to /home/lexbot/brain/ content edits (those are content, not infrastructure) or to /home/claude/ scratch work.

Precedence: ops_safety.md overrides any "act on intent" guidance in CLAUDE.md or agent prompts when the action touches live infrastructure.
