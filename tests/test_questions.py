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

def test_daily_14_batch_selection_and_order():
    qb = QuestionBank()
    batch = qb.get_daily_14_batch(set())
    assert len(batch) == 14
    for idx, (expected_cat, q) in enumerate(zip(CATEGORIES, batch)):
        assert q["category"] == expected_cat, f"Slot {idx} category mismatch: expected {expected_cat}, got {q['category']}"

def test_daily_14_rotation_and_no_repeats():
    qb = QuestionBank()
    day1_batch = qb.get_daily_14_batch(set())
    posted = {q["id"] for q in day1_batch}
    assert len(posted) == 14

    day2_batch = qb.get_daily_14_batch(posted)
    assert len(day2_batch) == 14
    day2_ids = {q["id"] for q in day2_batch}

    # No duplicate questions across days
    assert posted.isdisjoint(day2_ids)

    # Each subject progressed by 1
    for q1, q2 in zip(day1_batch, day2_batch):
        assert q1["category"] == q2["category"]
        id1_num = int(q1["id"][2:])
        id2_num = int(q2["id"][2:])
        assert id2_num == id1_num + 1

