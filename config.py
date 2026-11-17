import os
from zoneinfo import ZoneInfo
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot Configuration
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
# Accepts CHANNEL_ID or TARGET_CHAT_ID for compatibility with GitHub secrets & local env
TARGET_CHAT_ID = (
    os.getenv("TARGET_CHAT_ID")
    or os.getenv("CHANNEL_ID")
    or "@dealstimeknow"
).strip()

import re

# Admin IDs (comma-separated integers, handles prefixes like PA)
ADMIN_IDS = set()
for item in os.getenv("ADMIN_IDS", "").split(","):
    digits = re.sub(r"\D", "", item.strip())
    if digits:
        ADMIN_IDS.add(int(digits))

# Timezone (Default: Asia/Kolkata)
TZ_NAME = os.getenv("TIMEZONE", "Asia/Kolkata")
TZ = ZoneInfo(TZ_NAME)

# Paths
DB_PATH = os.getenv("DB_PATH", "quiz_history.sqlite3")
QUESTIONS_PATH = os.getenv("QUESTIONS_PATH", "questions/tgpsc_questions.json")
POSTED_HISTORY_PATH = os.getenv("POSTED_HISTORY_PATH", "data/posted_history.json")

# 14 Official TGPSC Subjects in exact syllabus order
CATEGORIES = [
    "Telangana History",
    "Telangana Movement",
    "Telangana Geography",
    "Indian Polity",
    "Indian History",
    "Indian Geography",
    "Indian Economy",
    "General Science",
    "Biology",
    "Physics",
    "Chemistry",
    "Current Affairs",
    "Telangana Culture",
    "Telangana Government Schemes"
]

# 14 Daily Posting Times (Asia/Kolkata)
# Default: 14 hourly slots from 07:00 to 20:00 IST (1 per subject)
DEFAULT_POST_TIMES = [
    (7, 0),   # 07:00 IST - Telangana History
    (8, 0),   # 08:00 IST - Telangana Movement
    (9, 0),   # 09:00 IST - Telangana Geography
    (10, 0),  # 10:00 IST - Indian Polity
    (11, 0),  # 11:00 IST - Indian History
    (12, 0),  # 12:00 IST - Indian Geography
    (13, 0),  # 13:00 IST - Indian Economy
    (14, 0),  # 14:00 IST - General Science
    (15, 0),  # 15:00 IST - Biology
    (16, 0),  # 16:00 IST - Physics
    (17, 0),  # 17:00 IST - Chemistry
    (18, 0),  # 18:00 IST - Current Affairs
    (19, 0),  # 19:00 IST - Telangana Culture
    (20, 0),  # 20:00 IST - Telangana Government Schemes
]

def _parse_post_times():
    raw = os.getenv("POST_TIMES", "").strip()
    if not raw:
        return DEFAULT_POST_TIMES
    times = []
    for part in raw.split(","):
        part = part.strip()
        if ":" in part:
            try:
                h, m = part.split(":", 1)
                times.append((int(h), int(m)))
            except ValueError:
                pass
    return times if len(times) == len(CATEGORIES) else DEFAULT_POST_TIMES

POST_TIMES = _parse_post_times()

SCHEDULED_SLOTS = [
    {
        "slot": i,
        "hour": POST_TIMES[i][0],
        "minute": POST_TIMES[i][1],
        "time": f"{POST_TIMES[i][0]:02d}:{POST_TIMES[i][1]:02d}",
        "category": CATEGORIES[i]
    }
    for i in range(min(len(POST_TIMES), len(CATEGORIES)))
]

def is_admin(user_id: int) -> bool:
    return user_id in ADMIN_IDS

