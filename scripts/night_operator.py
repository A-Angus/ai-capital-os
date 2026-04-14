#!/usr/bin/env python3
"""Night Operator — runs at 2 AM, picks the highest-leverage task and executes it.
Outputs go to /home/lexbot/.local/share/lex/* as defined in goals.md.
"""
from __future__ import annotations
import datetime as dt
from pathlib import Path
import subprocess

BRAIN = Path('/home/lexbot/brain')
LEX = Path('/home/lexbot/lex-output')

GOALS = BRAIN / 'goals.md'
DAILY_LOG = BRAIN / 'daily' / f"{dt.date.today().isoformat()}.md"
OPEN_LOOPS = BRAIN / 'daily-log' / 'OPEN_LOOPS.md'
ACTIVE = BRAIN / 'daily-log' / 'ACTIVE_PROJECTS.md'
DEALS = BRAIN / 'deals' / 'deals.md'

# Output dirs per goals.md
REPORTS_DIR   = LEX / 'reports'
FOLLOWUPS_DIR = LEX / 'followups'
CONTENT_DIR   = LEX / 'content'
RESEARCH_DIR  = LEX / 'lender_research'
RESOURCES_DIR = LEX / 'resources'

GMAIL_ACCOUNT = 'mr.alexangus@gmail.com'


def read_text(path: Path) -> str:
    return path.read_text() if path.exists() else ''


def run_gmail_search(query: str) -> str:
    cmd = [
        'bash', '-lc',
        f'export GOG_KEYRING_PASSWORD=openclaw && gog gmail messages search {query!r} --account {GMAIL_ACCOUNT} --max 10'
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=25)
        return (result.stdout or '') + ('\n' + result.stderr if result.stderr else '')
    except Exception as e:
        return f'ERROR: {e}'


def inbox_signal() -> tuple[str | None, str]:
    query = (
        '(from:rodoentre@gmail.com OR from:lbogner@cogocapital.com '
        'OR from:giancarloyacarine@gmail.com OR from:jamonewoodley@yahoo.com '
        'OR from:scbinnovativesolutions@gmail.com OR from:easystreetcap.com '
        'OR subject:Cheltenham OR subject:Sherbourne OR subject:Mehl '
        'OR subject:"Conley Downs") newer_than:2d'
    )
    output = run_gmail_search(query)
    lower = output.lower()
    if 'rodoentre@gmail.com' in lower:
        return 'RODOLFO_DSCR', output
    if 'cogocapital.com' in lower or 'cheltenham' in lower:
        return 'CHELTENHAM', output
    if 'giancarloyacarine@gmail.com' in lower or 'sherbourne' in lower:
        return 'HOUSTON_SHEUN', output
    if 'jamonewoodley@yahoo.com' in lower or 'scbinnovativesolutions@gmail.com' in lower or 'conley downs' in lower:
        return 'CONLEY_DOWNS', output
    return None, output


def parse_live_deal_priority() -> str | None:
    deals = read_text(DEALS)
    if 'Jason Coalson' in deals and ('Structuring' in deals or 'Under Review' in deals):
        return 'COALSON_LAND'
    if 'Nic Bray' in deals and 'Structuring' in deals:
        return 'NIC_BRAY'
    if 'Kwami Fox' in deals and 'Under Review' in deals:
        return 'CHELTENHAM'
    return None


def choose_task() -> tuple[str, str, Path, str]:
    open_loops = read_text(OPEN_LOOPS)
    active = read_text(ACTIVE)
    deals = read_text(DEALS)
    signal, inbox_debug = inbox_signal()
    live_priority = parse_live_deal_priority()
    today = dt.date.today().isoformat()

    if signal == 'RODOLFO_DSCR':
        out = FOLLOWUPS_DIR / f'{today}-rodolfo-followup.md'
        content = f"""# Follow Up — Rodolfo DSCR

[PROJECT: RODOLFO_DSCR]

Suggested message:

Got it. Before I ask for a corrected quote, I need to verify your exact payoff. Please send the latest mortgage statement or payoff letter when you can so I can tighten the numbers.

Why this won tonight:
- there is recent borrower inbox activity
- quote inputs appear inconsistent
- correcting payoff is the fastest path to movement

Inbox signal used:
```text
{inbox_debug.strip()[:2000]}
```
"""
        return 'Borrower follow-up', 'Inbox first logic found Rodolfo activity — payoff clarification is highest leverage.', out, content

    if signal == 'CHELTENHAM' or live_priority == 'CHELTENHAM':
        out = FOLLOWUPS_DIR / f'{today}-cheltenham-followup.md'
        content = f"""# Follow Up — Cheltenham

[PROJECT: CHELTENHAM]

Suggested message:

Hi Leah,

Following up on Cheltenham. Wanted to check whether there is any update on underwriting, inspection handling, or anything still needed from our side to keep the file moving.

If there is an issue blocking progress, send me the exact item and I will work it.

Alex

Why this won tonight:
- inbox showed Cheltenham related lender activity
- deals file marks it under review
- lender movement beats passive waiting
"""
        return 'Lender follow-up', 'Inbox and live deal file both point to Cheltenham as active and worth pushing.', out, content

    if 'COALSON_LAND' in open_loops or 'COALSON_LAND' in active or live_priority == 'COALSON_LAND':
        out = FOLLOWUPS_DIR / f'{today}-coalson-lender-followup.md'
        content = f"""# Follow Up — Coalson Land

[PROJECT: COALSON_LAND]

Subject: Quick follow up on Coalson Excavation bridge request

Hi,

Wanted to follow up on the Coalson Excavation bridge request for the three Texas parcels.

This one came in at roughly 39% LTV, so I wanted to see where it stands on your side and whether anything else is needed to move it toward a term sheet or formal feedback.

If helpful, I can resend the package or tighten the summary.

Alex

Why this won tonight:
- live deal file still shows active structuring work
- direct lender movement is the fastest route to revenue progress
"""
        return 'Lender follow-up', 'Live deal file points to Coalson as the best remaining leverage move.', out, content

    if 'Nic Bray' in deals or live_priority == 'NIC_BRAY':
        out = FOLLOWUPS_DIR / f'{today}-nic-bray-checklist.md'
        content = f"""# Structuring Checklist — Nic Bray

[PROJECT: NIC_BRAY]

Priority items to request or confirm:
- full property address
- project scope
- total loan request
- budget and timeline
- construction lender fit

Why this won tonight:
- the live deals file still shows structuring work in progress
- better packaging improves lender match speed
"""
        return 'Structuring task', 'Live deals file shows Nic Bray still needs a cleaner package.', out, content

    # Default: content draft
    out = CONTENT_DIR / f'{today}-capital-post.md'
    content = f"""# Content Draft — {today}

Topic: Why most borrowers wait too long to fix deal structure

Strong deals do not just need capital. They need timing, structure, and clean information.

A lot of deals die before they ever get a real look because the borrower waits too long to clarify payoff, docs, exit, or entity structure.

The earlier you tighten the file, the more options you have.

---

Hook options:
1. "Most deals don't die because of the property. They die because of the paperwork."
2. "Capital is available. Clean deals get it. Here's what that means."
3. "I've seen $2M deals fall apart in week 3 of underwriting. Here's the pattern."
"""
    return 'Content draft', 'No live deal blocker tonight — educational content asset is highest remaining leverage.', out, content


def write_report(task_name: str, reason: str, output_path: Path) -> Path:
    today = dt.date.today().isoformat()
    report = REPORTS_DIR / f"{today}-overnight-report.md"
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report.write_text(
        f"OPENCLAW OVERNIGHT REPORT — {today}\n\n"
        f"Task completed: {task_name}\n\n"
        f"Output saved to: {output_path}\n\n"
        f"Key finding or result: {reason}\n\n"
        f"Recommended next action for Alex: Review the output and act on it if tied to a live deal.\n"
    )
    return report


def append_daily_log(task_name: str, output_path: Path):
    stamp = dt.datetime.now(dt.UTC).strftime('%Y-%m-%d %H:%M UTC')
    DAILY_LOG.parent.mkdir(parents=True, exist_ok=True)
    if not DAILY_LOG.exists():
        DAILY_LOG.write_text(f"# {dt.date.today().isoformat()}\n\n")
    with DAILY_LOG.open('a') as f:
        f.write(
            f"\n---\n\n## Night Operator\n\n"
            f"Task completed: {task_name}\n"
            f"Output saved to: {output_path}\n"
            f"Generated at: {stamp}\n"
        )


def main():
    task_name, reason, output_path, content = choose_task()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content)
    report = write_report(task_name, reason, output_path)
    append_daily_log(task_name, output_path)
    print('TASK:', task_name)
    print('OUTPUT:', output_path)
    print('REPORT:', report)
    print('REASON:', reason)


if __name__ == '__main__':
    main()
