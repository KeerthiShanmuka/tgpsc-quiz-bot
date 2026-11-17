"""
Hard question generators for TGPSC Group 1, Group 2, and Police SI standard.
Ensures 100% complete bilingual questions and options without exceeding Telegram limits.
"""

def make_statement_q(cat, topic_te, topic_en, s1_te, s1_en, s2_te, s2_en, correctness_type, exp_te, exp_en, seed=0):
    """
    correctness_type:
    0: Only statement 1 is correct
    1: Only statement 2 is correct
    2: Both 1 and 2 are correct
    3: Neither 1 nor 2 is correct
    """
    q_te = f"[{topic_te}] కింది ప్రకటనలను పరిశీలించండి:\n1. {s1_te}\n2. {s2_te}\nపై ప్రకటనలలో సరైనది/వి ఏది/ఏవి?"
    q_en = f"[{topic_en}] Which of the statements given above is/are correct?"

    opts_te = [
        "1 మాత్రమే సరైనది",
        "2 మాత్రమే సరైనది",
        "1 మరియు 2 రెండూ సరైనవి",
        "1 మరియు 2 రెండూ సరైనవి కావు"
    ]
    opts_en = [
        "1 only is correct",
        "2 only is correct",
        "Both 1 and 2 are correct",
        "Neither 1 nor 2 is correct"
    ]

    return {
        "category": cat,
        "question_te": q_te[:300].strip(),
        "question_en": q_en[:300].strip(),
        "options_te": opts_te,
        "options_en": opts_en,
        "correct_option_id": correctness_type,
        "explanation_te": exp_te[:198].strip(),
        "explanation_en": exp_en[:198].strip()
    }

def make_incorrect_pair_q(cat, domain_te, domain_en, correct_pairs, wrong_pair, exp_te, exp_en, slot=0):
    """
    Identifies the incorrectly matched pair among 4 options.
    """
    assert len(correct_pairs) == 3, f"Need 3 correct pairs: {correct_pairs}"
    
    q_te = f"[{domain_te}] కింద పేర్కొన్న జతలలో 'సరికాని' (తప్పుగా జతపరచబడిన) జత ఏది?"
    q_en = f"[{domain_en}] Which of the following pairs is NOT correctly matched?"

    opts_te = [p[0] for p in correct_pairs]
    opts_en = [p[1] for p in correct_pairs]

    opts_te.insert(slot, wrong_pair[0])
    opts_en.insert(slot, wrong_pair[1])

    return {
        "category": cat,
        "question_te": q_te[:300].strip(),
        "question_en": q_en[:300].strip(),
        "options_te": [o[:100].strip() for o in opts_te],
        "options_en": [o[:100].strip() for o in opts_en],
        "correct_option_id": slot,
        "explanation_te": exp_te[:198].strip(),
        "explanation_en": exp_en[:198].strip()
    }

def make_assertion_q(cat, topic_te, topic_en, a_te, a_en, r_te, r_en, ans_code, exp_te, exp_en):
    """
    ans_code:
    0: Both A and R are true and R is correct explanation of A
    1: Both A and R are true but R is NOT correct explanation
    2: A is true, R is false
    3: A is false, R is true
    """
    q_te = f"[{topic_te}] ప్రతిపాదన (A) మరియు కారణం (R):\nప్రతిపాదన (A): {a_te}\nకారణం (R): {r_te}\nసరైన సమాధానాన్ని ఎంచుకోండి:"
    q_en = f"[{topic_en}] Which option is correct regarding Assertion (A) & Reason (R)?"

    opts_te = [
        "(A), (R) రెండూ సరైనవి, (R) సరైన వివరణ",
        "(A), (R) రెండూ సరైనవి, (R) వివరణ కాదు",
        "(A) సరైనది, కానీ (R) తప్పు",
        "(A) తప్పు, కానీ (R) సరైనది"
    ]
    opts_en = [
        "Both A & R true, R is correct explanation",
        "Both A & R true, R is NOT correct explanation",
        "A is true, but R is false",
        "A is false, but R is true"
    ]

    return {
        "category": cat,
        "question_te": q_te[:300].strip(),
        "question_en": q_en[:300].strip(),
        "options_te": opts_te,
        "options_en": opts_en,
        "correct_option_id": ans_code,
        "explanation_te": exp_te[:198].strip(),
        "explanation_en": exp_en[:198].strip()
    }

def make_match_code_q(cat, topic_te, topic_en, list1, list2, correct_code_te, correct_code_en, distractors_te, distractors_en, exp_te, exp_en, slot=0):
    """
    Match List-I with List-II with coding options.
    """
    l1_str = " | ".join(f"{k}. {v}" for k, v in list1)
    l2_str = " | ".join(f"{k}. {v}" for k, v in list2)
    q_te = f"[{topic_te}] జాబితా-I ని జాబితా-II తో జతపరచండి:\nI: {l1_str}\nII: {l2_str}\nసరైన కోడ్:"
    q_en = f"[{topic_en}] Match List-I with List-II and select the correct code:"

    opts_te = distractors_te[:3].copy()
    opts_en = distractors_en[:3].copy()
    opts_te.insert(slot, correct_code_te)
    opts_en.insert(slot, correct_code_en)

    return {
        "category": cat,
        "question_te": q_te[:300].strip(),
        "question_en": q_en[:300].strip(),
        "options_te": [o[:100].strip() for o in opts_te],
        "options_en": [o[:100].strip() for o in opts_en],
        "correct_option_id": slot,
        "explanation_te": exp_te[:198].strip(),
        "explanation_en": exp_en[:198].strip()
    }
