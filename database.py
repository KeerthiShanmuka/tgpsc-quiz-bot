import json
import logging
import os
import re
from datetime import datetime
from typing import Optional, Set, Tuple, List, Dict, Any
import aiosqlite
from config import DB_PATH, POSTED_HISTORY_PATH, TZ, CATEGORIES

log = logging.getLogger("tgpsc-quiz.database")

SCHEMA = """
CREATE TABLE IF NOT EXISTS posted_questions (
    question_id TEXT PRIMARY KEY,
    subject TEXT,
    posted_at TEXT NOT NULL,
    chat_id TEXT NOT NULL,
    poll_id TEXT,
    message_id INTEGER,
    status TEXT DEFAULT 'success'
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


def infer_subject_from_id(qid: str) -> str:
    """Infer the 14-subject category from the question ID range."""
    try:
        num = int(re.sub(r"\D", "", qid))
        if 1 <= num <= 143:
            return "Telangana History"
        elif 144 <= num <= 286:
            return "Telangana Movement"
        elif 287 <= num <= 429:
            return "Telangana Geography"
        elif 430 <= num <= 572:
            return "Indian Polity"
        elif 573 <= num <= 715:
            return "Indian History"
        elif 716 <= num <= 858:
            return "Indian Geography"
        elif 859 <= num <= 1001:
            return "Indian Economy"
        elif 1002 <= num <= 1144:
            return "General Science"
        elif 1145 <= num <= 1287:
            return "Biology"
        elif 1288 <= num <= 1430:
            return "Physics"
        elif 1431 <= num <= 1573:
            return "Chemistry"
        elif 1574 <= num <= 1716:
            return "Current Affairs"
        elif 1717 <= num <= 1858:
            return "Telangana Culture"
        elif 1859 <= num <= 2000:
            return "Telangana Government Schemes"
    except Exception:
        pass
    return "General Studies"


async def init_db(db_path: str = DB_PATH) -> None:
    """Initialize database and schema with auto-migrations."""
    async with aiosqlite.connect(db_path) as db:
        await db.executescript(SCHEMA)
        # Check and migrate columns if necessary
        async with db.execute("PRAGMA table_info(posted_questions)") as cursor:
            cols = [row[1] for row in await cursor.fetchall()]
            if "poll_id" not in cols:
                await db.execute("ALTER TABLE posted_questions ADD COLUMN poll_id TEXT")
            if "subject" not in cols:
                await db.execute("ALTER TABLE posted_questions ADD COLUMN subject TEXT")
            if "message_id" not in cols:
                await db.execute("ALTER TABLE posted_questions ADD COLUMN message_id INTEGER")
            if "status" not in cols:
                await db.execute("ALTER TABLE posted_questions ADD COLUMN status TEXT DEFAULT 'success'")
        await db.commit()
    log.info("Database initialized successfully at %s", db_path)


async def get_posted_ids(db_path: str = DB_PATH) -> Set[str]:
    """Get all posted question IDs from database and sync with JSON history."""
    posted = set()

    # 1. From database
    if os.path.exists(db_path):
        try:
            async with aiosqlite.connect(db_path) as db:
                cur = await db.execute("SELECT question_id FROM posted_questions")
                rows = await cur.fetchall()
                posted.update(row[0] for row in rows)
        except Exception as e:
            log.warning("Could not read posted IDs from DB: %s", e)

    # 2. From persistent JSON history file (for GitHub Actions sync)
    if os.path.exists(POSTED_HISTORY_PATH):
        try:
            with open(POSTED_HISTORY_PATH, "r", encoding="utf-8") as f:
                history_data = json.load(f)
                if isinstance(history_data, list):
                    posted.update(history_data)
                elif isinstance(history_data, dict):
                    if "posted_ids" in history_data:
                        posted.update(history_data["posted_ids"])
                    if "history" in history_data:
                        for entry in history_data["history"]:
                            if isinstance(entry, dict) and "question_id" in entry:
                                posted.add(entry["question_id"])
        except Exception as e:
            log.warning("Could not read posted history file: %s", e)

    return posted


async def get_posted_subjects_today(today_str: Optional[str] = None) -> Set[str]:
    """Return set of subject names posted today (Asia/Kolkata date YYYY-MM-DD)."""
    if not today_str:
        today_str = datetime.now(TZ).strftime("%Y-%m-%d")
    posted_subjects = set()

    if os.path.exists(DB_PATH):
        try:
            async with aiosqlite.connect(DB_PATH) as db:
                cur = await db.execute(
                    "SELECT subject FROM posted_questions WHERE posted_at LIKE ? AND status = 'success'",
                    (f"{today_str}%",)
                )
                rows = await cur.fetchall()
                for r in rows:
                    if r[0]:
                        posted_subjects.add(r[0])
        except Exception as e:
            log.warning("Could not check today's posted subjects in SQLite: %s", e)

    if os.path.exists(POSTED_HISTORY_PATH):
        try:
            with open(POSTED_HISTORY_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                history = data.get("history", []) if isinstance(data, dict) else []
                for entry in history:
                    if (
                        isinstance(entry, dict)
                        and entry.get("publication_date", "").startswith(today_str)
                        and entry.get("publication_status") == "success"
                    ):
                        subj = entry.get("subject")
                        if subj:
                            posted_subjects.add(subj)
        except Exception as e:
            log.warning("Could not check today's posted subjects in JSON: %s", e)

    return posted_subjects


async def record_posted_question(
    question_id: str,
    chat_id: str,
    subject: Optional[str] = None,
    poll_id: Optional[str] = None,
    message_id: Optional[int] = None,
    status: str = "success",
    db_path: str = DB_PATH,
    history_path: str = POSTED_HISTORY_PATH
) -> None:
    """
    Record a question as posted in both SQLite DB and persistent JSON history.
    Tracks: Question ID, Subject, Publication date, Telegram message ID, Publication status.
    """
    now_iso = datetime.now(TZ).isoformat()
    resolved_subject = subject or infer_subject_from_id(question_id)

    # 1. Record in SQLite
    async with aiosqlite.connect(db_path) as db:
        await db.execute(
            """
            INSERT OR REPLACE INTO posted_questions (
                question_id, subject, posted_at, chat_id, poll_id, message_id, status
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (question_id, resolved_subject, now_iso, str(chat_id), poll_id, message_id, status)
        )
        await db.commit()

    # 2. Record in persistent JSON file
    os.makedirs(os.path.dirname(os.path.abspath(history_path)), exist_ok=True)
    posted_ids_list: List[str] = []
    detailed_history: List[Dict[str, Any]] = []
    by_subject: Dict[str, List[str]] = {c: [] for c in CATEGORIES}

    if os.path.exists(history_path):
        try:
            with open(history_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    posted_ids_list = data
                elif isinstance(data, dict):
                    posted_ids_list = list(data.get("posted_ids", []))
                    detailed_history = list(data.get("history", []))
                    raw_by_sub = data.get("by_subject", {})
                    if isinstance(raw_by_sub, dict):
                        for k, v in raw_by_sub.items():
                            by_subject[k] = list(v)
        except Exception as e:
            log.warning("Could not parse history file: %s", e)

    # Reconcile existing legacy posted_ids into detailed_history & by_subject
    existing_ids_in_hist = {h.get("question_id") for h in detailed_history if isinstance(h, dict)}
    for old_id in posted_ids_list:
        if old_id not in existing_ids_in_hist:
            inferred = infer_subject_from_id(old_id)
            detailed_history.append({
                "question_id": old_id,
                "subject": inferred,
                "publication_date": now_iso,
                "telegram_message_id": None,
                "poll_id": None,
                "publication_status": "success"
            })
            if old_id not in by_subject.setdefault(inferred, []):
                by_subject[inferred].append(old_id)

    if question_id not in posted_ids_list:
        posted_ids_list.append(question_id)

    # Insert or update detailed entry
    new_entry = {
        "question_id": question_id,
        "subject": resolved_subject,
        "publication_date": now_iso,
        "telegram_message_id": message_id,
        "poll_id": poll_id,
        "publication_status": status
    }
    found_idx = next((i for i, h in enumerate(detailed_history) if h.get("question_id") == question_id), -1)
    if found_idx >= 0:
        detailed_history[found_idx] = new_entry
    else:
        detailed_history.append(new_entry)

    if resolved_subject not in by_subject:
        by_subject[resolved_subject] = []
    if question_id not in by_subject[resolved_subject]:
        by_subject[resolved_subject].append(question_id)

    payload = {
        "posted_ids": posted_ids_list,
        "history": detailed_history,
        "by_subject": by_subject,
        "last_updated": now_iso
    }
    with open(history_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)


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

