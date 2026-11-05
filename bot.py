import asyncio
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import PollType
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from config import (
    BOT_TOKEN,
    TARGET_CHAT_ID,
    TZ,
    POST_TIMES
)
from database import (
    init_db,
    get_posted_ids,
    record_posted_question,
    save_poll_metadata,
    get_setting
)
from question_manager import QuestionBank, format_poll_payload
from handlers.user_handlers import router as user_router
from handlers.admin_handlers import router as admin_router
from handlers.poll_handlers import router as poll_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
log = logging.getLogger("tgpsc-quiz")

posting_lock = asyncio.Lock()


async def scheduled_post_quiz(bot: Bot, qb: QuestionBank):
    """Post next scheduled quiz question to the target channel."""
    is_paused = (await get_setting("is_paused", "0")) == "1"
    if is_paused:
        log.info("Scheduled posting is currently paused.")
        return

    async with posting_lock:
        try:
            posted_ids = await get_posted_ids()
            unposted = qb.get_unposted(posted_ids, count=1)

            if not unposted:
                log.warning("Question bank exhausted! No unposted questions remaining.")
                return

            q = unposted[0]
            prompt, options, correct_id, explanation = format_poll_payload(q)

            log.info("Posting scheduled question %s to %s", q["id"], TARGET_CHAT_ID)
            poll_msg = await bot.send_poll(
                chat_id=TARGET_CHAT_ID,
                question=prompt,
                options=options,
                type=PollType.QUIZ,
                correct_option_id=correct_id,
                is_anonymous=True,
                explanation=explanation
            )

            poll_id = poll_msg.poll.id if poll_msg.poll else None
            await record_posted_question(q["id"], str(TARGET_CHAT_ID), poll_id=poll_id)
            if poll_id:
                await save_poll_metadata(poll_id, q["id"], str(TARGET_CHAT_ID), correct_id)

            log.info("Successfully posted question %s (poll_id=%s)", q["id"], poll_id)

        except Exception as e:
            log.exception("Failed to post scheduled quiz: %s", e)


async def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN is not set in environment or .env file.")

    log.info("Initializing database...")
    await init_db()

    log.info("Loading question bank...")
    qb = QuestionBank()
    log.info("Total loaded questions: %d", len(qb.questions))

    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties()
    )

    dp = Dispatcher()
    dp["qb"] = qb

    # Include routers
    dp.include_router(user_router)
    dp.include_router(admin_router)
    dp.include_router(poll_router)

    # Initialize APScheduler for 24/7 background posting
    scheduler = AsyncIOScheduler(timezone=TZ)

    for hour, minute in POST_TIMES:
        scheduler.add_job(
            scheduled_post_quiz,
            CronTrigger(hour=hour, minute=minute, timezone=TZ),
            args=[bot, qb],
            id=f"quiz_{hour}_{minute}",
            replace_existing=True,
            max_instances=1,
            coalesce=True
        )

    scheduler.start()
    log.info("APScheduler running with %d daily slots in %s.", len(POST_TIMES), TZ)
    log.info("Bot started successfully. Listening for updates...")

    try:
        await dp.start_polling(bot)
    finally:
        scheduler.shutdown(wait=False)
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
