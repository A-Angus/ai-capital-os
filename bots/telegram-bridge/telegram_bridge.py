#!/usr/bin/env python3
import os, sys, json, asyncio, logging, shutil, tempfile
from pathlib import Path

CONFIG_FILE = Path.home() / ".claude" / "telegram-bridge-config.json"
CLAUDE_BIN = shutil.which("claude") or "/usr/bin/claude"

CONTEXT_FILES = [
    "SOUL.md",
    "CLAUDE.md",
    "MEMORY.md",
    "IDENTITY.md",
    "brain/goals.md",
    "brain/README.md",
    "brain/deals/deals.md",
    "brain/people/README.md",
]


def load_config():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            return json.load(f)
    return {}


def save_config(config):
    CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)
    print(f"Config saved to {CONFIG_FILE}")


def setup():
    print("\n" + "=" * 50)
    print("  LEX AI OS - Telegram Bridge Setup")
    print("=" * 50)
    token = input("Paste your Telegram Bot Token: ").strip()
    user_id = input("Your Telegram User ID (numbers only): ").strip()
    approved_dir = input(f"Approved directory [{Path.home()}]: ").strip()
    if not approved_dir:
        approved_dir = str(Path.home())
    config = {
        "bot_token": token,
        "allowed_user_id": int(user_id),
        "approved_directory": approved_dir,
        "timeout_seconds": 1800,
    }
    save_config(config)
    print("\nSetup complete. Run this script again to start the bridge.")
    return config


def build_context(approved_dir: str) -> str:
    """Load key brain files and return them as a context block."""
    parts = []
    root = Path(approved_dir)
    # Also check /home/lexbot/brain as fallback for brain/ files
    brain_root = Path("/home/lexbot/brain")
    for rel in CONTEXT_FILES:
        p = root / rel
        if not p.exists() and rel.startswith("brain/"):
            p = brain_root / rel.removeprefix("brain/")
        if p.exists():
            try:
                text = p.read_text().strip()
                if text:
                    parts.append(f"--- {rel} ---\n{text}")
            except Exception:
                pass
    return "\n\n".join(parts)


async def run_claude(message: str, approved_dir: str, timeout: int, context: str) -> str:
    try:
        # Build a full prompt with context prepended
        full_prompt = f"""You are Atlas, Alex's AI assistant. You have access to Alex's full brain and memory system. Use the context below to answer. Be direct, concise, and helpful. No hyphens ever.

{context}

---

Alex's message: {message}"""

        # Write prompt to temp file to avoid shell escaping issues
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write(full_prompt)
            prompt_file = f.name

        cmd = f'cat {prompt_file!r} | {CLAUDE_BIN!r} --print --dangerously-skip-permissions'
        proc = await asyncio.create_subprocess_exec(
            "bash", "-lc", cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            stdin=asyncio.subprocess.DEVNULL,
            cwd=approved_dir,
        )
        try:
            stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout)
            output = stdout.decode().strip()
            if not output and stderr:
                output = f"[Claude error]: {stderr.decode().strip()}"
            return output or "[No response from Claude]"
        except asyncio.TimeoutError:
            proc.kill()
            return f"[Timed out after {timeout}s]"
        finally:
            try:
                os.unlink(prompt_file)
            except Exception:
                pass
    except FileNotFoundError:
        return "[Error: claude command not found]"
    except Exception as e:
        return f"[Error running Claude: {str(e)}]"


def main():
    config = load_config()
    if not config or "--setup" in sys.argv:
        config = setup()
        return

    try:
        from telegram import Update
        from telegram.ext import Application, MessageHandler, filters, ContextTypes
    except ImportError:
        print("\n[Error] python-telegram-bot not installed.")
        sys.exit(1)

    bot_token = config["bot_token"]
    allowed_user_id = config["allowed_user_id"]
    approved_dir = config["approved_directory"]
    timeout = config.get("timeout_seconds", 1800)

    # Pre-load context (refreshed each message)
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
    )
    logger = logging.getLogger(__name__)

    async def handle_message(update: Update, context_obj: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        if user_id != allowed_user_id:
            logger.warning(f"Unauthorized: {user_id}")
            return
        message = update.message.text
        logger.info(f"Received: {message[:80]}")
        await context_obj.bot.send_chat_action(
            chat_id=update.effective_chat.id, action="typing"
        )
        # Rebuild context each time so it picks up changes
        context = build_context(approved_dir)
        response = await run_claude(message, approved_dir, timeout, context)
        if len(response) <= 4096:
            await update.message.reply_text(response)
        else:
            chunks = [response[i : i + 4000] for i in range(0, len(response), 4000)]
            for i, chunk in enumerate(chunks):
                prefix = (
                    f"[Part {i+1}/{len(chunks)}]\n" if len(chunks) > 1 else ""
                )
                await update.message.reply_text(prefix + chunk)

    print("\n" + "=" * 50)
    print("  LEX AI OS - Telegram Bridge Running")
    print("=" * 50)
    print(f"  Authorized user ID : {allowed_user_id}")
    print(f"  Approved directory : {approved_dir}")
    print(f"  Timeout            : {timeout}s")
    print("  Waiting for messages...")
    print("=" * 50 + "\n")

    app = Application.builder().token(bot_token).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
