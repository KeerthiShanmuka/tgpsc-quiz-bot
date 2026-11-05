#!/usr/bin/env python3
"""
Autonomous Telegram Quiz Publisher for GitHub Actions and Scheduled Automation.
Supports single-slot execution or full batch posting with retry logic and persistent history.
"""

import argparse
import asyncio
import logging
import os
import sys
from typing import Optional

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import PollType

from config import BOT_TOKEN, TARGET_CHAT_ID
from database import (
    init_db,
    get_posted_ids,
    record_posted_question,
    save_poll_metadata
)
from question_manager import QuestionBank, format_poll_payload

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
log = logging.getLogger("tgpsc-quiz.publisher")


async def post_single_quiz_with_retry(
    bot: Bot,
    chat_id: str,
    q: dict,
    max_retries: int = 3,
    dry_run: bool = False
) -> bool:
    """Post a single quiz poll with exponential backoff retry."""
    prompt, options, correct_id, explanation = format_poll_payload(q)

    if dry_run:
        log.info("[DRY RUN] Would post question %s (%s) to %s", q["id"], q.get("category"), chat_id)
        log.info("[DRY RUN] Prompt: %s", prompt[:100])
        return True

    delay = 2
    for attempt in range(1, max_retries + 1):
        try:
            log.info("Sending poll for %s (Attempt %d/%d) to %s...", q["id"], attempt, max_retries, chat_id)
            poll_msg = await bot.send_poll(
                chat_id=chat_id,
                question=prompt,
                options=options,
                type=PollType.QUIZ,
                correct_option_id=correct_id,
                is_anonymous=True,
                explanation=explanation
            )

            poll_id = poll_msg.poll.id if poll_msg.poll else None
            await record_posted_question(q["id"], str(chat_id), poll_id=poll_id)
            if poll_id:
                await save_poll_metadata(poll_id, q["id"], str(chat_id), correct_id)

            log.info("Successfully posted question %s (poll_id=%s)", q["id"], poll_id)
            return True

        except Exception as e:
            log.warning("Attempt %d failed to post question %s: %s", attempt, q["id"], e)
            if attempt < max_retries:
                log.info("Retrying in %d seconds...", delay)
                await asyncio.sleep(delay)
                delay *= 2
            else:
                log.error("All %d attempts failed for question %s.", max_retries, q["id"])
                return False

    return False


async def run_publisher(
    count: int = 1,
    target_chat: Optional[str] = None,
    delay_between_posts: int = 3,
    max_retries: int = 3,
    category: Optional[str] = None,
    dry_run: bool = False
) -> int:
    """Main execution loop for publishing quiz batch."""
    chat_id = target_chat or TARGET_CHAT_ID

    if not dry_run and not BOT_TOKEN:
        log.critical("FATAL: BOT_TOKEN is not configured in environment or GitHub secrets.")
        return 1

    if not dry_run and not chat_id:
        log.critical("FATAL: Target chat/channel ID is not configured.")
        return 1

    await init_db()
    qb = QuestionBank()
    posted_ids = await get_posted_ids()

    unposted = qb.get_unposted(posted_ids, count=count, category=category)
    if not unposted:
        log.warning("Question bank exhausted! No unposted questions remaining.")
        return 0

    log.info("Found %d unposted questions. Target: %s", len(unposted), chat_id)

    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties()) if not dry_run else None

    success_count = 0
    failure_count = 0

    try:
        for idx, q in enumerate(unposted, start=1):
            success = await post_single_quiz_with_retry(
                bot=bot,
                chat_id=chat_id,
                q=q,
                max_retries=max_retries,
                dry_run=dry_run
            )

            if success:
                success_count += 1
            else:
                failure_count += 1

            if idx < len(unposted):
                await asyncio.sleep(delay_between_posts)

    finally:
        if bot:
            await bot.session.close()

    log.info(
        "Publishing session completed: %d succeeded, %d failed.",
        success_count,
        failure_count
    )

    return 0 if failure_count == 0 else 1


def main():
    parser = argparse.ArgumentParser(description="TGPSC Autonomous Quiz Publisher")
    parser.add_argument("--count", type=int, default=1, help="Number of questions to post (default: 1)")
    parser.add_argument("--target", type=str, default=None, help="Target channel or chat ID")
    parser.add_argument("--delay", type=int, default=3, help="Delay in seconds between posts")
    parser.add_argument("--retries", type=int, default=3, help="Max retries per post")
    parser.add_argument("--category", type=str, default=None, help="Filter by specific category")
    parser.add_argument("--dry-run", action="store_true", help="Simulate without posting")

    args = parser.parse_args()

    exit_code = asyncio.run(
        run_publisher(
            count=args.count,
            target_chat=args.target,
            delay_between_posts=args.delay,
            max_retries=args.retries,
            category=args.category,
            dry_run=args.dry_run
        )
    )
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
