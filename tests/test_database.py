import os
import pytest
import aiosqlite
from database import (
    init_db,
    record_posted_question,
    get_posted_ids,
    save_poll_metadata,
    get_poll_metadata,
    register_user,
    record_user_answer,
    get_user_score,
    get_leaderboard,
    get_setting,
    set_setting
)

@pytest.mark.asyncio
async def test_database_operations(tmp_path):
    test_db = str(tmp_path / "test_quiz.sqlite3")
    test_history = str(tmp_path / "test_history.json")

    # 1. Initialize
    await init_db(db_path=test_db)
    assert os.path.exists(test_db)

    # 2. Record posted questions
    await record_posted_question("TG0001", "@test_chat", poll_id="poll_123", db_path=test_db, history_path=test_history)
    posted = await get_posted_ids(db_path=test_db)
    assert "TG0001" in posted

    # 3. Poll metadata
    await save_poll_metadata("poll_123", "TG0001", "@test_chat", correct_option_id=2, db_path=test_db)
    meta = await get_poll_metadata("poll_123", db_path=test_db)
    assert meta is not None
    assert meta["question_id"] == "TG0001"
    assert meta["correct_option_id"] == 2

    # 4. User answer (correct answer)
    is_valid, is_correct, score = await record_user_answer(
        poll_id="poll_123",
        user_id=101,
        selected_option=2,
        username="aspirant1",
        first_name="Raju",
        db_path=test_db
    )
    assert is_valid is True
    assert is_correct is True
    assert score == 10

    # 5. User score check
    user_score = await get_user_score(101, db_path=test_db)
    assert user_score["score"] == 10
    assert user_score["total_attempted"] == 1
    assert user_score["correct_count"] == 1
    assert user_score["accuracy"] == 100.0
    assert user_score["rank"] == 1

    # 6. Leaderboard
    lb = await get_leaderboard(limit=5, db_path=test_db)
    assert len(lb) == 1
    assert lb[0]["user_id"] == 101

    # 7. Settings
    await set_setting("is_paused", "1", db_path=test_db)
    val = await get_setting("is_paused", default="0", db_path=test_db)
    assert val == "1"
