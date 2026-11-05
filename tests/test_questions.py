import pytest
from question_manager import QuestionBank, CATEGORIES, validate_question, normalize_text, format_poll_payload

def test_question_count_and_ids():
    qb = QuestionBank()
    assert len(qb.questions) == 2000, f"Expected 2000 questions, got {len(qb.questions)}"
    for idx, q in enumerate(qb.questions, start=1):
        expected_id = f"TG{idx:04d}"
        assert q["id"] == expected_id, f"Question at index {idx} has ID {q['id']}"

def test_all_14_categories_present():
    qb = QuestionBank()
    cats_found = set(q["category"] for q in qb.questions)
    for cat in CATEGORIES:
        assert cat in cats_found, f"Category {cat} missing in loaded questions"
        count = sum(1 for q in qb.questions if q["category"] == cat)
        assert count >= 140, f"Category {cat} has only {count} questions, expected >= 140"

def test_question_validation_and_telegram_limits():
    qb = QuestionBank()
    for idx, q in enumerate(qb.questions, start=1):
        is_valid, msg = validate_question(q, idx)
        assert is_valid, f"Validation failed for {q.get('id')}: {msg}"
        assert len(q["question_te"]) <= 300, f"Question text too long in {q['id']}"
        assert len(q["options_te"]) == 4, f"Must have 4 Telugu options in {q['id']}"
        for opt in q["options_te"]:
            assert len(opt) <= 100, f"Option too long in {q['id']}: {opt}"
        assert 0 <= q["correct_option_id"] <= 3, f"Invalid correct_option_id in {q['id']}"
        assert len(q["explanation_te"]) <= 200, f"Explanation too long in {q['id']}"

def test_no_duplicate_ids_or_texts():
    qb = QuestionBank()
    ids = set()
    texts = set()
    for q in qb.questions:
        assert q["id"] not in ids, f"Duplicate ID found: {q['id']}"
        ids.add(q["id"])
        norm = normalize_text(q["question_te"])
        assert norm not in texts, f"Duplicate question text found: {q['id']}"
        texts.add(norm)

def test_format_poll_payload():
    qb = QuestionBank()
    q = qb.questions[0]
    prompt, options, correct_idx, explanation = format_poll_payload(q)
    assert len(prompt) <= 300
    assert len(options) == 4
    for opt in options:
        assert len(opt) <= 100
    assert correct_idx == q["correct_option_id"]
    assert len(explanation) <= 200
