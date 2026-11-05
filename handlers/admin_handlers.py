import logging
from aiogram import Router, Bot
from aiogram.enums import PollType
from aiogram.filters import Command
from aiogram.types import Message

from config import is_admin, TARGET_CHAT_ID
from database import (
    get_posted_ids,
    record_posted_question,
    save_poll_metadata,
    get_setting,
    set_setting
)
from question_manager import QuestionBank, format_poll_payload

log = logging.getLogger("tgpsc-quiz.admin_handlers")
router = Router()


@router.message(Command("admin"))
async def handle_admin(message: Message, qb: QuestionBank):
    if not message.from_user or not is_admin(message.from_user.id):
        await message.answer("⛔ Access denied. Admin only.")
        return

    posted = await get_posted_ids()
    is_paused = (await get_setting("is_paused", "0")) == "1"
    status_str = "⏸️ PAUSED" if is_paused else "▶️ ACTIVE"

    text = (
        "⚙️ *TGPSC Bot Admin Control Panel*\n\n"
        f"🤖 *Scheduler Status:* {status_str}\n"
        f"🎯 *Target Channel:* `{TARGET_CHAT_ID}`\n"
        f"📚 *Total Questions:* {len(qb.questions)}\n"
        f"📤 *Posted Questions:* {len(posted)}\n"
        f"📥 *Remaining Questions:* {len(qb.questions) - len(posted)}\n\n"
        "🔧 *Available Commands:*\n"
        "• `/postquiz` - Immediately post 1 question to target channel\n"
        "• `/stats` - Full category statistics\n"
        "• `/pause` - Pause scheduled posts\n"
        "• `/resume` - Resume scheduled posts\n"
        "• `/categories` - Breakdown of questions per category"
    )
    await message.answer(text, parse_mode="Markdown")


@router.message(Command("postquiz"))
async def handle_postquiz(message: Message, bot: Bot, qb: QuestionBank):
    if not message.from_user or not is_admin(message.from_user.id):
        await message.answer("⛔ Access denied. Admin only.")
        return

    await message.answer("⏳ Fetching next unposted question and publishing...")

    posted_ids = await get_posted_ids()
    unposted = qb.get_unposted(posted_ids, count=1)

    if not unposted:
        await message.answer("⚠️ Question bank exhausted! No unposted questions remaining.")
        return

    q = unposted[0]
    prompt, options, correct_id, explanation = format_poll_payload(q)

    try:
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

        await message.answer(
            f"✅ Successfully posted question *{q['id']}* to `{TARGET_CHAT_ID}`!\n"
            f"Category: {q.get('category', 'General')}",
            parse_mode="Markdown"
        )
    except Exception as e:
        log.exception("Admin manual post failed")
        await message.answer(f"❌ Failed to post question: {e}")


@router.message(Command("stats"))
async def handle_stats(message: Message, qb: QuestionBank):
    if not message.from_user or not is_admin(message.from_user.id):
        return

    posted_ids = await get_posted_ids()
    s = qb.stats(posted_ids)

    text = (
        "📊 *TGPSC Question Bank & Channel Statistics*\n\n"
        f"📚 *Total Questions in Bank:* {s['total_questions']}\n"
        f"✅ *Already Posted:* {s['posted_count']}\n"
        f"⏳ *Remaining to Post:* {s['remaining']}\n"
        f"🎯 *Days of Coverage (10/day):* {round(s['remaining'] / 10, 1)} days\n\n"
        "Use `/categories` to view the detailed category breakdown."
    )
    await message.answer(text, parse_mode="Markdown")


@router.message(Command("categories"))
async def handle_categories(message: Message, qb: QuestionBank):
    if not message.from_user or not is_admin(message.from_user.id):
        return

    posted_ids = await get_posted_ids()
    s = qb.stats(posted_ids)

    lines = ["📑 *TGPSC Category Breakdown:*\n"]
    for cat, data in s["categories"].items():
        lines.append(f"• *{cat}:* {data['posted']}/{data['total']} posted ({data['remaining']} remaining)")

    await message.answer("\n".join(lines), parse_mode="Markdown")


@router.message(Command("pause"))
async def handle_pause(message: Message):
    if not message.from_user or not is_admin(message.from_user.id):
        return

    await set_setting("is_paused", "1")
    await message.answer("⏸️ Automatic quiz posting has been paused.")


@router.message(Command("resume"))
async def handle_resume(message: Message):
    if not message.from_user or not is_admin(message.from_user.id):
        return

    await set_setting("is_paused", "0")
    await message.answer("▶️ Automatic quiz posting has been resumed.")
