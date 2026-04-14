#!/usr/bin/env python3
"""Morning Briefing — runs at 7 AM, reads overnight report and prints summary."""
from __future__ import annotations
import datetime as dt
from pathlib import Path

LEX = Path('/home/lexbot/lex-output')
BRAIN = Path('/home/lexbot/brain')

REPORTS_DIR   = LEX / 'reports'
FOLLOWUPS_DIR = LEX / 'followups'
CONTENT_DIR   = LEX / 'content'
DEALS         = BRAIN / 'deals' / 'deals.md'
BRIEFINGS_DIR = LEX / 'reports'


def read_text(path: Path) -> str:
    return path.read_text() if path.exists() else ''


def find_todays_report() -> str:
    today = dt.date.today().isoformat()
    report_path = REPORTS_DIR / f"{today}-overnight-report.md"
    if report_path.exists():
        return report_path.read_text()
    # Fallback: most recent report
    reports = sorted(REPORTS_DIR.glob('*-overnight-report.md'), reverse=True)
    if reports:
        return f"[Most recent report — {reports[0].name}]\n\n" + reports[0].read_text()
    return "No overnight report found."


def list_pending_outputs() -> list[str]:
    today = dt.date.today().isoformat()
    pending = []
    for d in [FOLLOWUPS_DIR, CONTENT_DIR]:
        if d.exists():
            for f in sorted(d.glob('*.md'), reverse=True)[:3]:
                pending.append(str(f))
    return pending


def main():
    today = dt.date.today().isoformat()
    report_text = find_todays_report()
    pending = list_pending_outputs()

    briefing = f"""
=====================================
  OPENCLAW MORNING BRIEFING — {today}
=====================================

{report_text}

---

PENDING OUTPUTS (review before sending):
"""
    if pending:
        for p in pending:
            briefing += f"  - {p}\n"
    else:
        briefing += "  None found.\n"

    briefing += "\n=====================================\n"

    # Save briefing to reports dir
    out = BRIEFINGS_DIR / f"{today}-morning-briefing.md"
    BRIEFINGS_DIR.mkdir(parents=True, exist_ok=True)
    out.write_text(briefing)

    print(briefing)
    print(f"Briefing saved to: {out}")


if __name__ == '__main__':
    main()
