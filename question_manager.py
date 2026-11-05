import json
import logging
import os
import re
from typing import Dict, List, Optional, Set, Tuple, Any

from config import QUESTIONS_PATH

log = logging.getLogger("tgpsc-quiz.questions")

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


def normalize_text(text: str) -> str:
    """Normalize text for duplicate detection."""
    text = re.sub(r"\s+", " ", text).strip().lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text


def validate_question(q: Dict[str, Any], index: int = 0) -> Tuple[bool, str]:
    """Validate a single question dictionary against syllabus and Telegram constraints."""
    if not isinstance(q, dict):
        return False, f"Question #{index} is not an object."

    qid = q.get("id")
    if not qid or not isinstance(qid, str) or not qid.strip():
        return False, f"Question #{index} has missing or invalid ID."

    # Must contain Telugu content
    if not q.get("question_te") or not isinstance(q["question_te"], str) or not q["question_te"].strip():
        return False, f"Question {qid} is missing 'question_te'."

    # Options Telugu
    opts_te = q.get("options_te")
    if not isinstance(opts_te, list) or len(opts_te) != 4:
        return False, f"Question {qid} must have exactly 4 options in 'options_te'."

    for opt_idx, opt in enumerate(opts_te):
        if not isinstance(opt, str) or not opt.strip():
            return False, f"Question {qid} has invalid option_te at index {opt_idx}."
        if len(opt.strip()) > 100:
            return False, f"Question {qid} option_te #{opt_idx} exceeds 100 chars ({len(opt)})."

    # Correct option id
    try:
        correct_id = int(q.get("correct_option_id"))
    except (ValueError, TypeError):
        return False, f"Question {qid} has non-integer correct_option_id."

    if correct_id < 0 or correct_id > 3:
        return False, f"Question {qid} correct_option_id must be between 0 and 3."

    # Explanation Telugu
    exp_te = q.get("explanation_te")
    if not exp_te or not isinstance(exp_te, str) or not exp_te.strip():
        return False, f"Question {qid} is missing 'explanation_te'."

    # Check Telegram poll limits:
    # Question text max 300 chars
    q_len = len(q["question_te"])
    if q_len > 300:
        return False, f"Question {qid} question_te exceeds Telegram limit of 300 chars ({q_len})."

    # Explanation max 200 chars
    exp_len = len(exp_te)
    if exp_len > 200:
        return False, f"Question {qid} explanation_te exceeds Telegram limit of 200 chars ({exp_len})."

    return True, "Valid"


class QuestionBank:
    def __init__(self, path: str = QUESTIONS_PATH):
        self.path = path
        self.questions: List[Dict[str, Any]] = []
        self.by_id: Dict[str, Dict[str, Any]] = {}
        self.by_category: Dict[str, List[Dict[str, Any]]] = {}
        self.load()

    def load(self) -> int:
        """Load and validate questions from JSON file."""
        if not os.path.exists(self.path):
            log.warning("Questions file not found: %s", self.path)
            self.questions = []
            self.by_id = {}
            self.by_category = {}
            return 0

        with open(self.path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise ValueError("Questions JSON file must contain a list of objects.")

        valid_list = []
        seen_ids = set()
        seen_texts = set()
        by_cat: Dict[str, List[Dict[str, Any]]] = {c: [] for c in CATEGORIES}

        for idx, item in enumerate(data, start=1):
            is_valid, msg = validate_question(item, idx)
            if not is_valid:
                log.warning("Validation issue: %s", msg)
                continue

            qid = item["id"]
            if qid in seen_ids:
                log.warning("Duplicate question ID skipped: %s", qid)
                continue

            norm = normalize_text(item["question_te"])
            if norm in seen_texts:
                log.warning("Duplicate question text skipped: %s (%s)", qid, item["question_te"][:40])
                continue

            seen_ids.add(qid)
            seen_texts.add(norm)
            valid_list.append(item)

            cat = item.get("category", "General Studies")
            if cat not in by_cat:
                by_cat[cat] = []
            by_cat[cat].append(item)

        self.questions = valid_list
        self.by_id = {q["id"]: q for q in valid_list}
        self.by_category = by_cat
        log.info("Loaded %d valid questions from %s", len(self.questions), self.path)
        return len(self.questions)

    def get_by_id(self, qid: str) -> Optional[Dict[str, Any]]:
        return self.by_id.get(qid)

    def get_unposted(self, posted_ids: Set[str], count: int = 1, category: Optional[str] = None) -> List[Dict[str, Any]]:
        """Retrieve the next unposted questions."""
        candidates = self.by_category.get(category, self.questions) if category else self.questions
        unposted = [q for q in candidates if q["id"] not in posted_ids]
        return unposted[:count]

    def stats(self, posted_ids: Set[str]) -> Dict[str, Any]:
        """Generate breakdown statistics."""
        total = len(self.questions)
        posted_count = sum(1 for q in self.questions if q["id"] in posted_ids)
        remaining = total - posted_count

        cat_breakdown = {}
        for cat, q_list in self.by_category.items():
            if q_list:
                cat_posted = sum(1 for q in q_list if q["id"] in posted_ids)
                cat_breakdown[cat] = {
                    "total": len(q_list),
                    "posted": cat_posted,
                    "remaining": len(q_list) - cat_posted
                }

        return {
            "total_questions": total,
            "posted_count": posted_count,
            "remaining": remaining,
            "categories": cat_breakdown
        }


def format_poll_payload(q: Dict[str, Any]) -> Tuple[str, List[str], int, str]:
    """
    Format question into Telegram Poll payload ensuring limits:
    - question <= 300 chars
    - option <= 100 chars
    - explanation <= 200 chars
    """
    # Category tag and Question text
    cat = q.get("category", "")
    prefix = f"[{cat}] " if cat else ""
    q_te = q["question_te"].strip()

    # If bilingual English exists and fits within 300 chars, include it; otherwise use Telugu
    q_en = q.get("question_en", "").strip() if isinstance(q.get("question_en"), str) else ""
    combined = f"{prefix}{q_te}\n\n{q_en}".strip() if q_en else f"{prefix}{q_te}".strip()

    if len(combined) <= 300:
        question_text = combined
    else:
        # Fallback to pure Telugu with prefix
        telugu_only = f"{prefix}{q_te}".strip()
        question_text = telugu_only[:300]

    # Options
    options = []
    opts_te = q["options_te"]
    opts_en = q.get("options_en", [])
    has_en = isinstance(opts_en, list) and len(opts_en) == 4

    for i in range(4):
        te_opt = opts_te[i].strip()
        if has_en and opts_en[i].strip():
            en_opt = opts_en[i].strip()
            combo_opt = f"{te_opt} / {en_opt}"
            if len(combo_opt) <= 100:
                options.append(combo_opt)
            else:
                options.append(te_opt[:100])
        else:
            options.append(te_opt[:100])

    answer_idx = int(q["correct_option_id"])

    # Explanation - must be <= 200 chars for Telegram Poll
    exp_te = q.get("explanation_te", "").strip()
    explanation_text = f"వివరణ: {exp_te}"
    if len(explanation_text) > 200:
        explanation_text = explanation_text[:197] + "..."

    return question_text, options, answer_idx, explanation_text
