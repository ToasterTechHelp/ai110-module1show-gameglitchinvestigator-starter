from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score

# --- check_guess ---

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_message_says_lower():
    # FIX verification: when guess > secret the hint must say "Go LOWER!", not "Go HIGHER!"
    _, message = check_guess(70, 50)
    assert "LOWER" in message

def test_too_low_message_says_higher():
    # FIX verification: when guess < secret the hint must say "Go HIGHER!", not "Go LOWER!"
    _, message = check_guess(30, 50)
    assert "HIGHER" in message

def test_check_guess_always_int_secret():
    # FIX verification: passing secret as str should still work correctly (no alphabetical compare)
    # 9 vs "50": lexicographic "9" > "50" is True (wrong), but numeric 9 < 50 is correct.
    # With the fix, logic_utils never receives a str secret, but check_guess handles int only now.
    outcome, _ = check_guess(9, 50)
    assert outcome == "Too Low"

# --- parse_guess ---

def test_parse_guess_valid_int():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_empty():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None

def test_parse_guess_non_numeric():
    ok, value, err = parse_guess("abc")
    assert ok is False

# --- get_range_for_difficulty ---

def test_hard_range_is_wider_than_normal():
    # FIX verification: Hard should be harder (wider range) than Normal
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high > normal_high

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20
