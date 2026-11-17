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

from config import BOT_TOKEN, TARGET_CHAT_ID, TZ, CATEGORIES, POST_TIMES
from database import (
    init_db,
    get_posted_ids,
    record_posted_question,
    save_poll_metadata,
    get_posted_subjects_today
)
from question_manager import QuestionBank, format_poll_payload
from datetime import datetime

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
    """Post a single native Telegram Quiz Poll with exponential backoff retry."""
    prompt, options, correct_id, explanation = format_poll_payload(q)
    category = q.get("category", "General Studies")

    if dry_run:
        log.info("[DRY RUN] Would post question %s (%s) to %s", q["id"], category, chat_id)
        log.info("[DRY RUN] Prompt: %s", prompt[:100])
        return True

    delay = 2
    for attempt in range(1, max_retries + 1):
        try:
            log.info("Sending quiz poll for %s [%s] (Attempt %d/%d) to %s...", q["id"], category, attempt, max_retries, chat_id)
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
            message_id = poll_msg.message_id

            await record_posted_question(
                question_id=q["id"],
                chat_id=str(chat_id),
                subject=category,
                poll_id=poll_id,
                message_id=message_id,
                status="success"
            )

            if poll_id:
                await save_poll_metadata(poll_id, q["id"], str(chat_id), correct_id)

            log.info("Successfully posted %s [%s] (msg_id=%s, poll_id=%s)", q["id"], category, message_id, poll_id)
            return True

        except Exception as e:
            log.warning("Attempt %d failed to post question %s: %s", attempt, q["id"], e)
            if attempt < max_retries:
                log.info("Retrying in %d seconds...", delay)
                await asyncio.sleep(delay)
                delay *= 2
            else:
                log.error("All %d attempts failed for question %s.", max_retries, q["id"])
                # Record failure status
                try:
                    await record_posted_question(
                        question_id=q["id"],
                        chat_id=str(chat_id),
                        subject=category,
                        poll_id=None,
                        message_id=None,
                        status="failed"
                    )
                except Exception:
                    pass
                return False

    return False


def determine_auto_slot() -> int:
    """Determine the slot index (0-13) based on current Asia/Kolkata time."""
    now = datetime.now(TZ)
    current_minutes = now.hour * 60 + now.minute

    best_slot = 0
    min_diff = float("inf")

    for i, (h, m) in enumerate(POST_TIMES[:len(CATEGORIES)]):
        diff = abs(current_minutes - (h * 60 + m))
        if diff < min_diff:
            min_diff = diff
            best_slot = i

    return best_slot


async def run_publisher(
    count: int = 1,
    target_chat: Optional[str] = None,
    delay_between_posts: int = 3,
    max_retries: int = 3,
    category: Optional[str] = None,
    slot_index: Optional[int] = None,
    daily_14: bool = False,
    auto_slot: bool = False,
    force: bool = False,
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
    posted_today = await get_posted_subjects_today()

    questions_to_post = []

    if daily_14:
        log.info("Running Daily 14-Subject Rotation...")
        questions_to_post = qb.get_daily_14_batch(posted_ids)
    elif slot_index is not None:
        if 0 <= slot_index < len(CATEGORIES):
            cat = CATEGORIES[slot_index]
            if cat in posted_today and not force:
                log.info("Subject '%s' (Slot %d) already published today. Skipping duplicate.", cat, slot_index)
                return 0
            q = qb.get_next_for_category(cat, posted_ids)
            if q:
                questions_to_post = [q]
            else:
                log.warning("Subject bank exhausted for category: %s", cat)
        else:
            log.error("Invalid slot index: %d. Must be between 0 and %d.", slot_index, len(CATEGORIES) - 1)
            return 1
    elif category:
        q = qb.get_next_for_category(category, posted_ids)
        if q:
            questions_to_post = [q]
        else:
            log.warning("No unposted questions in category '%s'.", category)
    elif auto_slot:
        best_slot = determine_auto_slot()
        cat = CATEGORIES[best_slot]
        log.info("Auto-slot resolved to Slot %d: '%s' based on %s time.", best_slot, cat, TZ)

        # Check if already posted today
        if cat in posted_today and not force:
            log.info("Subject '%s' already published today. Searching for next unpublished subject today...", cat)
            # Find next subject that has not been posted today
            for c in CATEGORIES:
                if c not in posted_today:
                    cat = c
                    log.info("Found unpublished subject for today: '%s'", cat)
                    break
            else:
                log.info("All 14 subjects have already been published today! Nothing to do.")
                return 0

        q = qb.get_next_for_category(cat, posted_ids)
        if q:
            questions_to_post = [q]
        else:
            log.warning("Subject bank exhausted for category: %s", cat)
    else:
        # Fallback to general unposted questions
        questions_to_post = qb.get_unposted(posted_ids, count=count)

    if not questions_to_post:
        log.warning("No questions selected for posting.")
        return 0

    log.info("Selected %d question(s) for publishing to %s.", len(questions_to_post), chat_id)
    for q in questions_to_post:
        log.info("  -> ID: %s | Subject: %s", q["id"], q.get("category"))

    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties()) if not dry_run else None

    success_count = 0
    failure_count = 0

    try:
        for idx, q in enumerate(questions_to_post, start=1):
            success = await post_single_quiz_with_retry(
                bot=bot,
                chat_id=chat_id,
                q=q,
                max_retries=max_retries,
                dry_run=dry_run
            )

            if success:
                success_count += 1
                posted_ids.add(q["id"])
            else:
                failure_count += 1

            if idx < len(questions_to_post):
                await asyncio.sleep(delay_between_posts)

    finally:
        if bot:
            await bot.session.close()

    log.info(
        "Publishing session finished: %d succeeded, %d failed.",
        success_count,
        failure_count
    )

    return 0 if failure_count == 0 else 1


def main():
    parser = argparse.ArgumentParser(description="TGPSC Autonomous Quiz Publisher")
    parser.add_argument("--daily-14", action="store_true", help="Publish 1 question from each of the 14 subjects")
    parser.add_argument("--slot", "--slot-index", dest="slot_index", type=int, default=None, help="Slot index (0 to 13)")
    parser.add_argument("--auto-slot", action="store_true", help="Automatically determine slot by current Asia/Kolkata time")
    parser.add_argument("--category", type=str, default=None, help="Filter by specific subject category")
    parser.add_argument("--count", type=int, default=1, help="Number of questions to post (default: 1)")
    parser.add_argument("--target", type=str, default=None, help="Target channel or chat ID")
    parser.add_argument("--delay", type=int, default=3, help="Delay in seconds between posts")
    parser.add_argument("--retries", type=int, default=3, help="Max retries per post")
    parser.add_argument("--force", action="store_true", help="Force publish even if subject was already posted today")
    parser.add_argument("--dry-run", action="store_true", help="Simulate without posting")

    args = parser.parse_args()

    exit_code = asyncio.run(
        run_publisher(
            count=args.count,
            target_chat=args.target,
            delay_between_posts=args.delay,
            max_retries=args.retries,
            category=args.category,
            slot_index=args.slot_index,
            daily_14=args.daily_14,
            auto_slot=args.auto_slot,
            force=args.force,
            dry_run=args.dry_run
        )
    )
    sys.exit(exit_code)


if __name__ == "__main__":
    main()

