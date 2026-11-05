import logging
from aiogram import Router
from aiogram.types import PollAnswer

from database import record_user_answer

log = logging.getLogger("tgpsc-quiz.poll_handlers")
router = Router()


@router.poll_answer()
async def handle_poll_answer(poll_answer: PollAnswer):
    """
    Handle live user answers to Telegram quiz polls.
    Tracks answers, awards points (+10 for correct), updates leaderboard.
    """
    try:
        user = poll_answer.user
        poll_id = poll_answer.poll_id

        if not poll_answer.option_ids:
            # User retracted vote (if enabled)
            return

        selected_option = poll_answer.option_ids[0]

        is_valid_poll, is_correct, current_score = await record_user_answer(
            poll_id=poll_id,
            user_id=user.id,
            selected_option=selected_option,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name
        )

        if is_valid_poll:
            log.info(
                "Recorded answer for user %s (%s): poll=%s, option=%s, correct=%s, total_score=%s",
                user.id,
                user.first_name,
                poll_id,
                selected_option,
                is_correct,
                current_score
            )
        else:
            log.debug("Poll %s not tracked in bot database.", poll_id)

    except Exception as e:
        log.exception("Error processing poll answer: %s", e)

