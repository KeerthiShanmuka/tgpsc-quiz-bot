# 🎯 TGPSC Telegram Quiz Bot (తెలంగాణ పోటీ పరీక్షల క్విజ్ బాట్)

An autonomous, feature-rich Telegram Quiz Bot built with **Python 3.11**, **aiogram 3.x**, **aiosqlite**, and **GitHub Actions**. Tailored specifically for aspirants preparing for **TGPSC Group 1, Group 2, Group 3, Group 4, Police Sub-Inspector (SI), and Constable** examinations.

---

## 🌟 Key Features

1. **2,000 Syllabus-Verified Telangana Questions (`TG0001` - `TG2000`)**
   - Strictly curated across 14 official categories.
   - 4 multiple-choice options with exactly one correct answer.
   - Rich explanations in Telugu adhering to Telegram's 200-character poll explanation limit.
   - Built-in automated duplicate detection (ID and question text normalization).

2. **Native Telegram Quiz Polls & Live Scoring**
   - Posts anonymous native quiz polls to your channel/group.
   - Interactive `/quiz` command allows instant practice in private chat or groups.
   - Automatic `poll_answer` listener records user responses in SQLite.
   - Real-time score tracking (+10 points per correct answer), accuracy percentage calculation, and user ranking.

3. **Autonomous Daily Automation via GitHub Actions**
   - Zero dependence on a local laptop running 24/7.
   - Scheduled daily posting (Default: 10 daily slots across 7:00 AM – 11:30 AM IST).
   - **Persistent Question Posting State**: Synchronizes posted question IDs in `data/posted_history.json` and automatically commits updates back to GitHub.
   - Exponential backoff retry logic on transient Telegram API network failures.

4. **Leaderboard & User Progress**
   - `/leaderboard` displays the top 10 scoring aspirants.
   - `/score` displays personal performance metrics (total attempts, correct answers, accuracy %, rank).

---

## 📚 14 Question Categories (2,000 Questions)

| # | Category (వర్గం) | Question Count | Question ID Range |
|---|-------------------|----------------|-------------------|
| 1 | Telangana History | 143 | TG0001 - TG0143 |
| 2 | Telangana Movement | 143 | TG0144 - TG0286 |
| 3 | Telangana Geography | 143 | TG0287 - TG0429 |
| 4 | Indian Polity | 143 | TG0430 - TG0572 |
| 5 | Indian History | 143 | TG0573 - TG0715 |
| 6 | Indian Geography | 143 | TG0716 - TG0858 |
| 7 | Indian Economy | 143 | TG0859 - TG1001 |
| 8 | General Science | 143 | TG1002 - TG1144 |
| 9 | Biology | 143 | TG1145 - TG1287 |
| 10 | Physics | 143 | TG1288 - TG1430 |
| 11 | Chemistry | 143 | TG1431 - TG1573 |
| 12 | Current Affairs | 143 | TG1574 - TG1716 |
| 13 | Telangana Culture | 142 | TG1717 - TG1858 |
| 14 | Telangana Government Schemes | 142 | TG1859 - TG2000 |
| **Total** | **All 14 Categories** | **2,000 Questions** | **TG0001 - TG2000** |

---

## 🤖 Bot Commands

### User Commands
- `/start` - Welcome message and introduction in Telugu & English.
- `/help` - Comprehensive guide on how to practice quizzes and track scores.
- `/quiz` - Generates an instant interactive quiz question directly in chat.
- `/daily` - View daily schedule timings, posted count, and remaining question bank status.
- `/score` - View your total points, questions attempted, correct answers, accuracy %, and rank.
- `/leaderboard` - Top 10 scorers leaderboard.

### Admin Commands (Restricted to `ADMIN_IDS`)
- `/admin` - Admin control panel with scheduler status, channel info, and metrics.
- `/postquiz` - Manually post the next unposted question to the configured channel immediately.
- `/stats` - Full question bank and posting history summary.
- `/categories` - Detailed question breakdown by category.
- `/pause` - Temporarily pause scheduled postings.
- `/resume` - Resume scheduled postings.

---

## ⚙️ Setup & Local Installation

### Prerequisites
- Python 3.11+
- Git

### 1. Clone & Create Virtual Environment
```bash
git clone https://github.com/KeerthiShanmuka/tgpsc-quiz-bot.git
cd tgpsc-quiz-bot

py -3.11 -m venv .venv
# On Windows PowerShell:
.venv\Scripts\Activate.ps1
# On Linux/macOS:
source .venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
Edit `.env` with your credentials:
```ini
BOT_TOKEN=your_telegram_bot_token_from_botfather
TARGET_CHAT_ID=@your_channel_or_group_id
ADMIN_IDS=123456789,987654321
TIMEZONE=Asia/Kolkata
DB_PATH=quiz_history.sqlite3
QUESTIONS_PATH=questions/tgpsc_questions.json
POSTED_HISTORY_PATH=data/posted_history.json
```

---

## 🧪 Running Tests & Validations

Execute the automated test suite with pytest:
```bash
pytest -v
```

All 2,000 questions are verified for:
- Strict JSON schema conformity
- Unique IDs from `TG0001` to `TG2000`
- Telegram Poll constraints:
  - Question text $\le 300$ characters
  - Option text $\le 100$ characters
  - Explanation $\le 200$ characters
- Zero duplicate normalized questions

---

## 🚀 Autonomous Deployment via GitHub Actions

The bot operates **100% autonomously without keeping your computer on**.

### Required GitHub Repository Secrets
Navigate to your GitHub repository: **Settings > Secrets and variables > Actions > New repository secret**:
1. `BOT_TOKEN`: Your Telegram Bot API token from `@BotFather`.
2. `CHANNEL_ID`: Your target Telegram Channel/Supergroup username (e.g. `@dealstimeknow`) or numeric ID (e.g. `-100xxxxxxxxxx`).

### Automated Workflow
- File: `.github/workflows/daily_quiz.yml`
- Executes on the configured Asia/Kolkata schedule (10 slots daily).
- Supports manual execution via GitHub **Actions > Daily TGPSC Quiz Publisher > Run workflow** (with optional custom question count, category filter, and dry-run flag).
- Preserves question-posting history by committing `data/posted_history.json` back to the repository with `[skip ci]`.

---

## 📁 Project Architecture

```
tgpsc-quiz-bot/
├── .github/
│   └── workflows/
│       ├── daily_quiz.yml         # GitHub Actions scheduled automation
│       └── test.yml               # Automated CI test suite
├── config.py                      # Centralized configuration & environment loader
├── database.py                    # Async SQLite manager (scores, polls, users, history)
├── question_manager.py            # Question loading, validation, and poll payload formatting
├── bot.py                         # Main aiogram 3 bot entrypoint & local APScheduler
├── handlers/
│   ├── __init__.py
│   ├── user_handlers.py           # /start, /help, /quiz, /daily, /score, /leaderboard
│   ├── admin_handlers.py          # /admin, /postquiz, /stats, /categories, /pause, /resume
│   └── poll_handlers.py           # Live PollAnswer scoring and analytics listener
├── scripts/
│   ├── publish_quiz.py            # CLI publisher for GitHub Actions with retry & history sync
│   ├── build_2000_questions.py    # Master compiler for 2,000 syllabus questions
│   └── category_data/             # Modular curriculum data generators
├── data/
│   └── posted_history.json        # Persistent posted question tracking across CI runs
├── questions/
│   └── tgpsc_questions.json       # 2,000 verified TGPSC syllabus questions
├── tests/
│   ├── test_questions.py          # Question validation & schema tests
│   ├── test_database.py           # SQLite score, leaderboard, and history tests
│   └── test_publisher.py          # Dry-run publisher tests
├── requirements.txt
├── pytest.ini
├── .gitignore
├── .env.example
└── README.md
```

---

## 🛡️ Security Best Practices
- Never commit `.env` or hardcode tokens. `.gitignore` is preconfigured to exclude `.env`, `.venv/`, and `*.sqlite3`.
- In GitHub Actions, only repository secrets (`BOT_TOKEN`, `CHANNEL_ID`) are used.
- If a bot token is ever exposed, revoke it immediately via `@BotFather`.
