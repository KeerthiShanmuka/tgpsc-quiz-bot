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

# Admin IDs (comma-separated integers)
ADMIN_IDS = {
    int(x.strip())
    for x in os.getenv("ADMIN_IDS", "").split(",")
    if x.strip().isdigit()
}

# Timezone (Default: Asia/Kolkata)
TZ_NAME = os.getenv("TIMEZONE", "Asia/Kolkata")
TZ = ZoneInfo(TZ_NAME)

# Paths
DB_PATH = os.getenv("DB_PATH", "quiz_history.sqlite3")
QUESTIONS_PATH = os.getenv("QUESTIONS_PATH", "questions/tgpsc_questions.json")
POSTED_HISTORY_PATH = os.getenv("POSTED_HISTORY_PATH", "data/posted_history.json")

# Schedule times (Asia/Kolkata)
POST_TIMES = [
    (7, 0), (7, 30),
    (8, 0), (8, 30),
    (9, 0), (9, 30),
    (10, 0), (10, 30),
    (11, 0), (11, 30)
]

def is_admin(user_id: int) -> bool:
    return user_id in ADMIN_IDS
