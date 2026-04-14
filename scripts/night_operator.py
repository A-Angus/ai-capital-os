#!/usr/bin/env python3
"""
LEX Night Operator v2 — runs at 2 AM PST
Scans all deals, pipeline, lenders, and inbox.
Identifies stuck deals, missed follow-ups, stalled items.
Generates prioritized action list and executes highest leverage task.
"""
from __future__ import annotations
import datetime as dt
from pathlib import Path
import subprocess
import json

BRAIN = Path("/home/lexbot/brain")
LEX = Path("/home/lexbot/lex-output")

GOALS        = BRAIN / "goals.md"
DEALS        = BRAIN / "deals" / "deals.md"
LENDERS      = BRAIN / "lenders" / "lenders.md"
PIPELINE_DIR = BRAIN / "pipeline"
DAILY_LOG    = BRAIN / "daily-log" / f"{dt.date.today().isoformat()}.md"
PEOPLE_DIR   = BRAIN / "people"

REPORTS_DIR   = LEX / "reports"
FOLLOWUPS_DIR = LEX / "followups"
CONTENT_DIR   = LEX / "content"
RESEARCH_DIR  = LEX / "lender_research"

GMAIL_ACCOUNT = "mr.alexangus@gmail.com"
TODAY         = dt.date.today().isoformat()
NOW           = dt.datetime.now()


def read_text(path: Path) -> str:
    return path.read_text() if path.exists() else ""


def run_gmail_search(query: str) -> str:
    cmd = [
        "bash", "-lc",
        f"export GOG_KEYRING_PASSWORD=openclaw && gog gmail messages search {query!r} --account {GMAIL_ACCOUNT} --max 10"
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=25)
        return (result.stdout or "") + ("\n" + result.stderr if result.stderr else "")
    except Exception as e:
        return f"ERROR: {e}"


# ─── DEAL SCANNER ──────────────────────────────────────────────────────────────

def scan_deals() -> list[dict]:
    """Parse deals.md and return structured deal list with status flags."""
    deals_text = read_text(DEALS)
    deals = []

    active_keywords = ["structuring", "under review", "submitted", "active", "pending", "in progress"]
    stall_keywords  = ["waiting", "stalled", "no response", "follow up needed", "unclear"]
    dead_keywords   = ["dead", "cancelled", "passed", "withdrawn"]

    for line in deals_text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("|--"):
            continue
        lower = line.lower()

        if any(k in lower for k in dead_keywords):
            continue

        deal = {"raw": line, "status": "unknown", "flags": []}

        if any(k in lower for k in active_keywords):
            deal["status"] = "active"
        if any(k in lower for k in stall_keywords):
            deal["flags"].append("stalled")
        if "coalson" in lower:
            deal["name"] = "Coalson Excavation"
            deal["priority"] = "high"
        elif "acj" in lower or "nic bray" in lower:
            deal["name"] = "ACJ Built"
            deal["priority"] = "high"
        elif "nikita" in lower or "baker" in lower:
            deal["name"] = "Nikita Baker"
            deal["priority"] = "high"
        elif "youngs lane" in lower or "nashville" in lower or "tanya" in lower:
            deal["name"] = "Nashville Transactional"
            deal["priority"] = "critical"
            deal["flags"].append("deadline")
        else:
            deal["name"] = line[:40]
            deal["priority"] = "normal"

        deals.append(deal)

    return deals


def scan_pipeline_files() -> list[dict]:
    """Check pipeline folder for recent followup files and flag stale ones."""
    stale = []
    if not PIPELINE_DIR.exists():
        return stale

    cutoff = NOW - dt.timedelta(hours=48)
    for f in sorted(PIPELINE_DIR.glob("*.md")):
        try:
            mtime = dt.datetime.fromtimestamp(f.stat().st_mtime)
            if mtime < cutoff:
                stale.append({"file": f.name, "last_updated": mtime.isoformat(), "hours_ago": round((NOW - mtime).total_seconds() / 3600)})
        except Exception:
            pass
    return stale


def scan_inbox() -> tuple[str | None, str]:
    """Check inbox for deal-related signals."""
    query = (
        "(from:wolfer OR from:bohnker OR from:kennedy OR from:sognare OR from:tanya "
        "OR from:nikita OR from:unitas OR from:jz OR from:zendejas OR from:levinecapital "
        "OR from:cogocapital OR subject:Coalson OR subject:ACJ OR subject:Nikita "
        "OR subject:Youngs OR subject:Nashville) newer_than:2d"
    )
    output = run_gmail_search(query)
    lower = output.lower()

    if "youngs" in lower or "nashville" in lower or "tanya" in lower or "sognare" in lower:
        return "NASHVILLE_URGENT", output
    if "coalson" in lower or "kennedy" in lower or "wolfer" in lower or "bohnker" in lower:
        return "COALSON", output
    if "acj" in lower or "nic bray" in lower or "zendejas" in lower or "jz" in lower:
        return "ACJ", output
    if "nikita" in lower or "baker" in lower or "unitas" in lower:
        return "NIKITA", output
    return None, output


# ─── ACTION GENERATOR ──────────────────────────────────────────────────────────

def build_action_list(deals: list[dict], stale_pipeline: list[dict], inbox_signal: str | None) -> list[dict]:
    """Build prioritized action list from all signals."""
    actions = []

    # Critical deadline first
    if inbox_signal == "NASHVILLE_URGENT" or any(d.get("name") == "Nashville Transactional" for d in deals):
        actions.append({
            "priority": 1,
            "deal": "Nashville Transactional — Youngs Lane LLC",
            "action": "Confirm closing status with Tanya Waymire at Sognare. April 20 deadline.",
            "type": "follow_up",
            "urgency": "CRITICAL — deadline in days"
        })

    # High priority active deals
    if inbox_signal == "COALSON" or any(d.get("name") == "Coalson Excavation" for d in deals):
        actions.append({
            "priority": 2,
            "deal": "Coalson Excavation — $11M Texas land bridge",
            "action": "Follow up with Chase Wolfer and Andrew Bohnker at Kennedy Funding on submission status.",
            "type": "lender_follow_up",
            "urgency": "HIGH — active submission"
        })

    if inbox_signal == "ACJ" or any(d.get("name") == "ACJ Built" for d in deals):
        actions.append({
            "priority": 3,
            "deal": "ACJ Built — construction bridge",
            "action": "Check with Nic Bray on deal intake completion. Confirm lender match status.",
            "type": "borrower_follow_up",
            "urgency": "HIGH — in structuring"
        })

    if inbox_signal == "NIKITA" or any(d.get("name") == "Nikita Baker" for d in deals):
        actions.append({
            "priority": 4,
            "deal": "Nikita Baker — Newport News VA gap funding",
            "action": "Check private lender responses to pitch deck. Follow up with any warm contacts.",
            "type": "lender_follow_up",
            "urgency": "HIGH — gap funding active"
        })

    # Stale pipeline items
    for item in stale_pipeline[:3]:
        actions.append({
            "priority": 5,
            "deal": item["file"].replace(".md", ""),
            "action": f"Pipeline file not updated in {item['hours_ago']} hours. Review and update status.",
            "type": "pipeline_maintenance",
            "urgency": "MEDIUM — stale data"
        })

    # Default content if nothing urgent
    if not actions:
        actions.append({
            "priority": 99,
            "deal": "General",
            "action": "No urgent deal signals tonight. Draft capital placement content or research new lender targets.",
            "type": "content",
            "urgency": "LOW"
        })

    return sorted(actions, key=lambda x: x["priority"])


# ─── OUTPUT WRITERS ─────────────────────────────────────────────────────────────

def write_overnight_report(actions: list[dict], deals: list[dict], stale: list[dict], inbox_signal: str | None) -> Path:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORTS_DIR / f"{TODAY}-overnight-report.md"

    lines = [
        f"# LEX Night Operator Report — {TODAY}",
        f"Generated: {NOW.strftime('%Y-%m-%d %H:%M PST')}",
        "",
        "---",
        "",
        "## Inbox Signal",
        f"Signal detected: {inbox_signal or 'None'}",
        "",
        "## Active Deals Scanned",
    ]

    for d in deals:
        flags = ", ".join(d.get("flags", [])) or "none"
        lines.append(f"- {d.get('name', d['raw'][:40])} — status: {d['status']} — flags: {flags}")

    lines += [
        "",
        f"## Stale Pipeline Files ({len(stale)} found)",
    ]
    for s in stale:
        lines.append(f"- {s['file']} — last updated {s['hours_ago']}h ago")

    lines += [
        "",
        "## Prioritized Action List",
        "",
    ]
    for i, action in enumerate(actions, 1):
        lines += [
            f"### {i}. {action['deal']}",
            f"**Urgency:** {action['urgency']}",
            f"**Action:** {action['action']}",
            f"**Type:** {action['type']}",
            "",
        ]

    lines += [
        "---",
        "",
        "## Recommended First Move for Alex",
        f"{actions[0]['action'] if actions else 'Review pipeline and update deal statuses.'}",
        "",
        "*Generated by LEX Night Operator v2*",
    ]

    report_path.write_text("\n".join(lines))
    return report_path


def write_top_followup(action: dict) -> Path:
    FOLLOWUPS_DIR.mkdir(parents=True, exist_ok=True)
    slug = action["deal"].lower().replace(" ", "-").replace("—", "").replace("$", "").strip("-")[:30]
    out = FOLLOWUPS_DIR / f"{TODAY}-{slug}-followup.md"

    if action["type"] == "lender_follow_up":
        if "coalson" in action["deal"].lower():
            body = """Subject: Follow up — Coalson Excavation bridge request

Hi Chase / Andrew,

Following up on the Coalson Excavation bridge request for the three Texas parcels.

Submitted at roughly 39% LTV. Wanted to check where it stands and whether anything else is needed to move toward a term sheet or formal feedback.

Happy to resend the package or tighten the summary if helpful.

Alex Angus
718-219-9382"""
        elif "nikita" in action["deal"].lower():
            body = """Subject: Follow up — Newport News VA gap funding

Hi,

Following up on the gap funding request for the Newport News VA ground-up project.

ARV is $425K, senior loan through Unitas, $60K gap. Pitch deck was submitted. Wanted to check if you had a chance to review and whether there are any questions.

Alex Angus
718-219-9382"""
        else:
            body = f"""Subject: Follow up — {action["deal"]}

Hi,

Following up on the above deal. Wanted to check on status and whether anything is needed from our side to keep it moving.

Alex Angus
718-219-9382"""

    elif action["type"] == "borrower_follow_up":
        body = f"""Subject: Quick check in — {action["deal"]}

Hi,

Just checking in on your end. Wanted to confirm we have everything needed to move forward and that nothing has changed on the deal.

If there are any updates or new information, send it over and I will keep the file moving.

Alex Angus
718-219-9382"""

    else:
        body = f"Action item: {action['action']}\n\nDeal: {action['deal']}\nUrgency: {action['urgency']}"

    out.write_text(f"# Follow Up Draft — {action['deal']}\n\nGenerated: {TODAY}\n\n---\n\n{body}\n")
    return out


def append_daily_log(report_path: Path, top_action: dict):
    DAILY_LOG.parent.mkdir(parents=True, exist_ok=True)
    if not DAILY_LOG.exists():
        DAILY_LOG.write_text(f"# {TODAY}\n\n")
    stamp = NOW.strftime("%Y-%m-%d %H:%M PST")
    with DAILY_LOG.open("a") as f:
        f.write(
            f"\n---\n\n## Night Operator v2\n\n"
            f"Report: {report_path}\n"
            f"Top action: {top_action['action']}\n"
            f"Generated at: {stamp}\n"
        )


# ─── MAIN ───────────────────────────────────────────────────────────────────────

def main():
    print(f"LEX Night Operator v2 — {TODAY}")
    print("Scanning deals, pipeline, inbox...")

    deals         = scan_deals()
    stale         = scan_pipeline_files()
    signal, _raw  = scan_inbox()
    actions       = build_action_list(deals, stale, signal)

    print(f"Deals found: {len(deals)}")
    print(f"Stale pipeline files: {len(stale)}")
    print(f"Inbox signal: {signal}")
    print(f"Actions generated: {len(actions)}")

    report_path = write_overnight_report(actions, deals, stale, signal)
    followup    = write_top_followup(actions[0])
    append_daily_log(report_path, actions[0])

    print(f"Report: {report_path}")
    print(f"Top followup: {followup}")
    print(f"Top action: {actions[0]['action']}")


if __name__ == "__main__":
    main()
