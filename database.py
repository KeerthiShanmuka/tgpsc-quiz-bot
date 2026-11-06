import json
import logging
import os
from datetime import datetime
from typing import Optional, Set, Tuple, List, Dict, Any
import aiosqlite
from config import DB_PATH, POSTED_HISTORY_PATH, TZ

log = logging.getLogger("tgpsc-quiz.database")

SCHEMA = """
CREATE TABLE IF NOT EXISTS posted_questions (
    question_id TEXT PRIMARY KEY,
    posted_at TEXT NOT NULL,
    chat_id TEXT NOT NULL,
    poll_id TEXT
);

CREATE TABLE IF NOT EXISTS polls (
    poll_id TEXT PRIMARY KEY,
    question_id TEXT NOT NULL,
    chat_id TEXT NOT NULL,
    correct_option_id INTEGER NOT NULL,
    posted_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    first_name TEXT,
    last_name TEXT,
    joined_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS user_scores (
    user_id INTEGER PRIMARY KEY,
    total_attempted INTEGER DEFAULT 0,
    correct_count INTEGER DEFAULT 0,
    score INTEGER DEFAULT 0,
    last_active TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS poll_answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    poll_id TEXT NOT NULL,
    question_id TEXT,
    user_id INTEGER NOT NULL,
    selected_option INTEGER NOT NULL,
    is_correct INTEGER NOT NULL,
    answered_at TEXT NOT NULL,
    UNIQUE(poll_id, user_id)
);

CREATE TABLE IF NOT EXISTS settings (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);
"""


async def init_db(db_path: str = DB_PATH) -> None:
    """Initialize database and schema with auto-migrations."""
    async with aiosqlite.connect(db_path) as db:
        await db.executescript(SCHEMA)
        # Check and migrate columns if necessary
        async with db.execute("PRAGMA table_info(posted_questions)") as cursor:
            cols = [row[1] for row in await cursor.fetchall()]
            if "poll_id" not in cols:
                await db.execute("ALTER TABLE posted_questions ADD COLUMN poll_id TEXT")
        await db.commit()
    log.info("Database initialized successfully at %s", db_path)


async def get_posted_ids(db_path: str = DB_PATH) -> Set[str]:
    """Get all posted question IDs from database and sync with JSON history."""
    posted = set()

    # 1. From database
    if os.path.exists(db_path):
        async with aiosqlite.connect(db_path) as db:
            cur = await db.execute("SELECT question_id FROM posted_questions")
            rows = await cur.fetchall()
            posted.update(row[0] for row in rows)

    # 2. From persistent JSON history file (for GitHub Actions sync)
    if os.path.exists(POSTED_HISTORY_PATH):
        try:
            with open(POSTED_HISTORY_PATH, "r", encoding="utf-8") as f:
                history_data = json.load(f)
                if isinstance(history_data, list):
                    posted.update(history_data)
                elif isinstance(history_data, dict) and "posted_ids" in history_data:
                    posted.update(history_data["posted_ids"])
        except Exception as e:
            log.warning("Could not read posted history file: %s", e)

    return posted


async def record_posted_question(
    question_id: str,
    chat_id: str,
    poll_id: Optional[str] = None,
    db_path: str = DB_PATH,
    history_path: str = POSTED_HISTORY_PATH
) -> None:
    """Record a question as posted in both DB and persistent JSON history."""
    now_iso = datetime.now(TZ).isoformat()

    # Record in SQLite
    async with aiosqlite.connect(db_path) as db:
        await db.execute(
            """
            INSERT OR REPLACE INTO posted_questions (question_id, posted_at, chat_id, poll_id)
            VALUES (?, ?, ?, ?)
            """,
            (question_id, now_iso, str(chat_id), poll_id)
        )
        await db.commit()

    # Record in persistent JSON file
    os.makedirs(os.path.dirname(os.path.abspath(history_path)), exist_ok=True)
    history = []
    if os.path.exists(history_path):
        try:
            with open(history_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    history = data
                elif isinstance(data, dict) and "posted_ids" in data:
                    history = data["posted_ids"]
        except Exception:
            history = []

    if question_id not in history:
        history.append(question_id)
        with open(history_path, "w", encoding="utf-8") as f:
            json.dump({"posted_ids": history, "last_updated": now_iso}, f, indent=2)


async def save_poll_metadata(
    poll_id: str,
    question_id: str,
    chat_id: str,
    correct_option_id: int,
    db_path: str = DB_PATH
) -> None:
    """Save metadata for a posted poll to enable score tracking."""
    now_iso = datetime.now(TZ).isoformat()
    async with aiosqlite.connect(db_path) as db:
        await db.execute(
            """
            INSERT OR REPLACE INTO polls (poll_id, question_id, chat_id, correct_option_id, posted_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (poll_id, question_id, str(chat_id), correct_option_id, now_iso)
        )
        await db.commit()


async def get_poll_metadata(poll_id: str, db_path: str = DB_PATH) -> Optional[Dict[str, Any]]:
    """Retrieve metadata for a poll."""
    async with aiosqlite.connect(db_path) as db:
        db.row_factory = aiosqlite.Row
        cur = await db.execute("SELECT * FROM polls WHERE poll_id = ?", (poll_id,))
        row = await cur.fetchone()
        if row:
            return dict(row)
        return None


async def register_user(
    user_id: int,
    username: Optional[str] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    db_path: str = DB_PATH
) -> None:
    """Register or update user details."""
    now_iso = datetime.now(TZ).isoformat()
    async with aiosqlite.connect(db_path) as db:
        await db.execute(
            """
            INSERT INTO users (user_id, username, first_name, last_name, joined_at)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(user_id) DO UPDATE SET
                username = COALESCE(excluded.username, users.username),
                first_name = COALESCE(excluded.first_name, users.first_name),
                last_name = COALESCE(excluded.last_name, users.last_name)
            """,
            (user_id, username, first_name, last_name, now_iso)
        )
        await db.commit()


async def record_user_answer(
    poll_id: str,
    user_id: int,
    selected_option: int,
    username: Optional[str] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    db_path: str = DB_PATH
) -> Tuple[bool, bool, int]:
    """
    Record an answer to a poll.
    Returns: (is_valid_poll, is_correct, current_total_score)
    """
    poll_meta = await get_poll_metadata(poll_id, db_path=db_path)
    if not poll_meta:
        return False, False, 0

    question_id = poll_meta["question_id"]
    correct_option = poll_meta["correct_option_id"]
    is_correct = int(selected_option == correct_option)
    score_delta = 10 if is_correct else 0
    now_iso = datetime.now(TZ).isoformat()

    await register_user(user_id, username, first_name, last_name, db_path=db_path)

    async with aiosqlite.connect(db_path) as db:
        # Check if user already answered this poll
        cur = await db.execute(
            "SELECT id FROM poll_answers WHERE poll_id = ? AND user_id = ?",
            (poll_id, user_id)
        )
        existing = await cur.fetchone()
        if existing:
            # User already answered, fetch current score
            score_cur = await db.execute(
                "SELECT score FROM user_scores WHERE user_id = ?", (user_id,)
            )
            s_row = await score_cur.fetchone()
            curr_score = s_row[0] if s_row else 0
            return True, bool(is_correct), curr_score

        # Insert answer
        await db.execute(
            """
            INSERT INTO poll_answers (poll_id, question_id, user_id, selected_option, is_correct, answered_at)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (poll_id, question_id, user_id, selected_option, is_correct, now_iso)
        )

        # Update score
        await db.execute(
            """
            INSERT INTO user_scores (user_id, total_attempted, correct_count, score, last_active)
            VALUES (?, 1, ?, ?, ?)
            ON CONFLICT(user_id) DO UPDATE SET
                total_attempted = user_scores.total_attempted + 1,
                correct_count = user_scores.correct_count + ?,
                score = user_scores.score + ?,
                last_active = ?
            """,
            (user_id, is_correct, score_delta, now_iso, is_correct, score_delta, now_iso)
        )
        await db.commit()

        # Get updated score
        cur2 = await db.execute("SELECT score FROM user_scores WHERE user_id = ?", (user_id,))
        row2 = await cur2.fetchone()
        new_score = row2[0] if row2 else score_delta

    return True, bool(is_correct), new_score


async def get_user_score(user_id: int, db_path: str = DB_PATH) -> Optional[Dict[str, Any]]:
    """Retrieve score, attempts, accuracy and rank for a user."""
    async with aiosqlite.connect(db_path) as db:
        db.row_factory = aiosqlite.Row
        cur = await db.execute(
            """
            SELECT u.user_id, u.username, u.first_name, s.total_attempted, s.correct_count, s.score, s.last_active
            FROM users u
            JOIN user_scores s ON u.user_id = s.user_id
            WHERE u.user_id = ?
            """,
            (user_id,)
        )
        row = await cur.fetchone()
        if not row:
            return None

        # Calculate rank
        rank_cur = await db.execute(
            "SELECT COUNT(*) + 1 FROM user_scores WHERE score > ?", (row["score"],)
        )
        rank_row = await rank_cur.fetchone()
        rank = rank_row[0] if rank_row else 1

        result = dict(row)
        result["rank"] = rank
        total = result["total_attempted"]
        correct = result["correct_count"]
        result["accuracy"] = round((correct / total * 100), 1) if total > 0 else 0.0
        return result


async def get_leaderboard(limit: int = 10, db_path: str = DB_PATH) -> List[Dict[str, Any]]:
    """Get top scoring users."""
    async with aiosqlite.connect(db_path) as db:
        db.row_factory = aiosqlite.Row
        cur = await db.execute(
            """
            SELECT u.user_id, u.username, u.first_name, s.total_attempted, s.correct_count, s.score
            FROM user_scores s
            JOIN users u ON s.user_id = u.user_id
            ORDER BY s.score DESC, s.correct_count DESC
            LIMIT ?
            """,
            (limit,)
        )
        rows = await cur.fetchall()
        return [dict(r) for r in rows]


async def get_setting(key: str, default: Optional[str] = None, db_path: str = DB_PATH) -> Optional[str]:
    """Get a persistent setting."""
    async with aiosqlite.connect(db_path) as db:
        cur = await db.execute("SELECT value FROM settings WHERE key = ?", (key,))
        row = await cur.fetchone()
        return row[0] if row else default


async def set_setting(key: str, value: str, db_path: str = DB_PATH) -> None:
    """Set a persistent setting."""
    async with aiosqlite.connect(db_path) as db:
        await db.execute(
            "INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)",
            (key, value)
        )
        await db.commit()

