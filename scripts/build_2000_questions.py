#!/usr/bin/env python3
"""
Master compiler that generates all 2,000 TGPSC competitive examination questions
and saves them to questions/tgpsc_questions.json with validation.
"""

import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from question_manager import validate_question, normalize_text, CATEGORIES
from scripts.generate_full_curriculum import make_helper
from scripts.category_data.part_telangana import generate_part_telangana
from scripts.category_data.part_india import generate_part_india
from scripts.category_data.part_science import generate_part_science
from scripts.category_data.part_culture_schemes import generate_part_culture_schemes

OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "..", "questions", "tgpsc_questions.json")

def main():
    print("🚀 Starting compilation of 2,000 TGPSC Questions...")
    add_fn, questions = make_helper()

    # Generate all parts
    print("Compiling Part 1 (Telangana History, Movement, Geography)...")
    generate_part_telangana(add_fn)
    print(f"Current total: {len(questions)}")

    print("Compiling Part 2 (Indian Polity, History, Geography, Economy)...")
    generate_part_india(add_fn)
    print(f"Current total: {len(questions)}")

    print("Compiling Part 3 (General Science, Biology, Physics, Chemistry)...")
    generate_part_science(add_fn)
    print(f"Current total: {len(questions)}")

    print("Compiling Part 4 (Current Affairs, Telangana Culture, Telangana Schemes)...")
    generate_part_culture_schemes(add_fn)
    print(f"Current total: {len(questions)}")

    if len(questions) != 2000:
        raise ValueError(f"Expected 2000 questions, got {len(questions)}")

    # Verify ID range
    for idx, q in enumerate(questions, start=1):
        expected_id = f"TG{idx:04d}"
        if q["id"] != expected_id:
            raise ValueError(f"ID mismatch at index {idx}: expected {expected_id}, got {q['id']}")

    # Write to JSON file
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Successfully generated and saved {len(questions)} questions to {OUTPUT_FILE}!")
    print(f"First ID: {questions[0]['id']}, Last ID: {questions[-1]['id']}")

    # Category breakdown
    cat_counts = {}
    for q in questions:
        cat = q["category"]
        cat_counts[cat] = cat_counts.get(cat, 0) + 1

    print("\n📊 Final Category Distribution:")
    for cat in CATEGORIES:
        count = cat_counts.get(cat, 0)
        print(f"  • {cat}: {count} questions")

if __name__ == "__main__":
    main()

