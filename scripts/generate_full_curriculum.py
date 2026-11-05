#!/usr/bin/env python3
"""
TGPSC Full Curriculum 2,000 Questions Generator
"""

import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from question_manager import validate_question, normalize_text, CATEGORIES

OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "..", "questions", "tgpsc_questions.json")

def make_helper():
    questions = []
    seen_ids = set()
    seen_texts = set()

    def add(cat, q_te, q_en, correct_te, correct_en, d_te, d_en, exp_te, exp_en, slot_idx=None):
        slot = (len(questions) % 4) if slot_idx is None else slot_idx
        opts_te = d_te[:3].copy()
        opts_en = d_en[:3].copy()
        opts_te.insert(slot, correct_te)
        opts_en.insert(slot, correct_en)

        qid = f"TG{len(questions)+1:04d}"
        q_obj = {
            "id": qid,
            "category": cat,
            "question_te": q_te.strip()[:300],
            "question_en": q_en.strip()[:300],
            "options_te": [o.strip()[:100] for o in opts_te],
            "options_en": [o.strip()[:100] for o in opts_en],
            "correct_option_id": slot,
            "explanation_te": exp_te.strip()[:198],
            "explanation_en": exp_en.strip()[:198]
        }
        is_val, msg = validate_question(q_obj, len(questions)+1)
        if not is_val:
            raise ValueError(f"Validation failed for {qid}: {msg}")

        norm = normalize_text(q_te)
        if norm in seen_texts:
            raise ValueError(f"Duplicate text for {qid}: {q_te}")
        seen_texts.add(norm)
        seen_ids.add(qid)
        questions.append(q_obj)

    return add, questions
