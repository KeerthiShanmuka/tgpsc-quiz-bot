import logging
from aiogram import Router
from aiogram.enums import PollType
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from config import SCHEDULED_SLOTS
from database import (
    register_user,
    get_user_score,
    get_leaderboard,
    get_posted_ids,
    save_poll_metadata
)
from question_manager import QuestionBank, format_poll_payload

log = logging.getLogger("tgpsc-quiz.user_handlers")
router = Router()


@router.message(CommandStart())
async def handle_start(message: Message):
    user = message.from_user
    if user:
        await register_user(
            user_id=user.id,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name
        )

    text = (
        "📚 *స్వాగతం! TGPSC డైలీ క్విజ్ బాట్‌కి స్వాగతం.*\n"
        "*Welcome to the TGPSC Daily Quiz Bot!*\n\n"
        "తెలంగాణ పోటీ పరీక్షల (TGPSC Group 1, 2, 3, 4, Police SI & Constable) "
        "అభ్యర్థుల కోసం రూపొందించిన ప్రత్యేక క్విజ్ బాట్.\n\n"
        "📌 *లభ్యమయ్యే ఆదేశాలు / Available Commands:*\n"
        "🔹 `/quiz` - తక్షణమే ఒక క్విజ్ ప్రశ్నను ప్రారంభించండి\n"
        "🔹 `/daily` - నేటి షెడ్యూల్ మరియు డైలీ క్విజ్ సమాచారం\n"
        "🔹 `/score` - మీ ప్రస్తుత స్కోరు, ఖచ్చితత్వం మరియు ర్యాంక్\n"
        "🔹 `/leaderboard` - టాప్ 10 అత్యుత్తమ స్కోరర్ల జాబితా\n"
        "🔹 `/help` - పూర్తి సహాయం మరియు మార్గదర్శకాలు\n\n"
        "ప్రతిరోజూ ఉదయం 10 ముఖ్యమైన ప్రశ్నలు చానల్ లో పోస్ట్ చేయబడతాయి!"
    )
    await message.answer(text, parse_mode="Markdown")


@router.message(Command("help"))
async def handle_help(message: Message):
    text = (
        "📖 *TGPSC Quiz Bot User Guide / సహాయ మార్గదర్శి*\n\n"
        "🔹 `/quiz` - మీ అభ్యాసం కోసం ప్రశ్నను పొందండి.\n"
        "🔹 `/daily` - రోజువారీ క్విజ్ టైమింగ్స్ మరియు వివరాలు చూడండి.\n"
        "🔹 `/score` - మీరు సాధించిన మార్కులు, సరైన సమాధానాలు మరియు ర్యాంక్ చూడండి.\n"
        "🔹 `/leaderboard` - అత్యధిక స్కోరు సాధించిన అగ్రశ్రేణి అభ్యర్థుల వివరాలు.\n\n"
        "💡 *పోల్స్ ఎలా పనిచేస్తాయి:*\n"
        "1. చానల్ లేదా గ్రూప్‌లో వచ్చే క్విజ్ పోల్ లో సరైన సమాధానాన్ని ఎంచుకోండి.\n"
        "2. సరైన సమాధానం ఎంపిక చేసిన వెంటనే +10 పాయింట్లు లభిస్తాయి.\n"
        "3. తప్పు సమాధానం అయితే వివరణ (Explanation) కనిపిస్తుంది.\n"
        "4. `/score` టైప్ చేసి మీ పురోగతిని ఎప్పటికప్పుడు సమీక్షించుకోండి."
    )
    await message.answer(text, parse_mode="Markdown")


@router.message(Command("quiz"))
async def handle_quiz(message: Message, qb: QuestionBank):
    """Serve an interactive quiz question directly in chat."""
    user = message.from_user
    if user:
        await register_user(
            user_id=user.id,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name
        )

    # Get a question from question bank
    import random
    if not qb.questions:
        await message.answer("క్షమించండి, ప్రశ్నల నిధి అందుబాటులో లేదు. దయచేసి తర్వాత ప్రయత్నించండి.")
        return

    # Pick a random question for direct practice
    q = random.choice(qb.questions)
    prompt, options, correct_id, explanation = format_poll_payload(q)

    # Send native Telegram quiz poll
    poll_msg = await message.answer_poll(
        question=prompt,
        options=options,
        type=PollType.QUIZ,
        correct_option_id=correct_id,
        is_anonymous=False,  # non-anonymous allows capturing user vote in DMs/groups for score
        explanation=explanation
    )

    # Save poll metadata for score calculation
    if poll_msg.poll:
        await save_poll_metadata(
            poll_id=poll_msg.poll.id,
            question_id=q["id"],
            chat_id=str(message.chat.id),
            correct_option_id=correct_id
        )


@router.message(Command("score"))
async def handle_score(message: Message):
    """Display user's current score and accuracy."""
    user = message.from_user
    if not user:
        return

    score_info = await get_user_score(user.id)
    if not score_info or score_info["total_attempted"] == 0:
        await message.answer(
            f"నమస్కారం {user.first_name}!\n\n"
            "మీరు ఇంకా ఏ క్విజ్‌లోనూ పాల్గొనలేదు. "
            "వెంటనే `/quiz` ఆదేశాన్ని ఉపయోగించి మీ తొలి క్విజ్ ప్రారంభించండి!"
        )
        return

    text = (
        f"🎯 *{user.first_name} వారి TGPSC స్కోరు కార్డు:*\n\n"
        f"🏆 *మొత్తం స్కోరు (Score):* {score_info['score']} పాయింట్లు\n"
        f"📊 *ప్రయత్నించిన ప్రశ్నలు:* {score_info['total_attempted']}\n"
        f"✅ *సరైన సమాధానాలు:* {score_info['correct_count']}\n"
        f"📈 *ఖచ్చితత్వం (Accuracy):* {score_info['accuracy']}%\n"
        f"🏅 *ప్రస్తుత ర్యాంక్:* #{score_info['rank']}\n\n"
        "మరిన్ని ప్రశ్నల సాధన కోసం `/quiz` క్లిక్ చేయండి!"
    )
    await message.answer(text, parse_mode="Markdown")


@router.message(Command("leaderboard"))
async def handle_leaderboard(message: Message):
    """Display top 10 users."""
    leaders = await get_leaderboard(limit=10)
    if not leaders:
        await message.answer(
            "🏆 *లీడర్‌బోర్డ్ / Leaderboard*\n\n"
            "ప్రస్తుతానికి ఎటువంటి స్కోర్లు నమోదు కాలేదు. "
            "మొదటి స్థానాన్ని కైవసం చేసుకోవడానికి `/quiz` తో ప్రారంభించండి!"
        )
        return

    lines = ["🏆 *TGPSC టాప్ 10 లీడర్‌బోర్డ్ (Leaderboard):*\n"]
    medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

    for idx, user in enumerate(leaders):
        icon = medals[idx] if idx < len(medals) else f"{idx+1}."
        name = user["first_name"] or user["username"] or f"User {user['user_id']}"
        lines.append(f"{icon} *{name}* — {user['score']} pts ({user['correct_count']}/{user['total_attempted']} సరైనవి)")

    lines.append("\nమరింత సాధన చేసి అగ్రస్థానాన్ని చేరండి! 🚀")
    await message.answer("\n".join(lines), parse_mode="Markdown")


@router.message(Command("daily"))
async def handle_daily(message: Message, qb: QuestionBank):
    """Show daily schedule and question bank status."""
    posted_ids = await get_posted_ids()
    stats = qb.stats(posted_ids)

    schedule_lines = []
    for slot in SCHEDULED_SLOTS:
        schedule_lines.append(f"⏰ *{slot['time']}* — {slot['category']}")

    text = (
        "📅 *TGPSC డైలీ 14-సబ్జెక్ట్ క్విజ్ షెడ్యూల్ (Daily Schedule)*\n\n"
        "ప్రతిరోజూ 14 విభిన్న సబ్జెక్టుల నుండి ఖచ్చితంగా 14 ప్రశ్నలు (Asia/Kolkata):\n\n"
        + "\n".join(schedule_lines)
        + f"\n\n📊 *మొత్తం ప్రశ్నల నిధి:* {stats['total_questions']}\n"
        f"📤 *ఇప్పటివరకు పోస్ట్ చేసినవి:* {stats['posted_count']}\n"
        f"📥 *మిగిలి ఉన్న ప్రశ్నలు:* {stats['remaining']}\n\n"
        "📢 రోజూ 14 ప్రశ్నలు చానల్ లో స్వయంచాలకంగా ప్రసారం చేయబడతాయి!"
    )
    await message.answer(text, parse_mode="Markdown")

