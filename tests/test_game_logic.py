from logic_utils import check_guess

# FIXME : Check for correct Guess
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# Tests targeting the backward-hint bug:
# check_guess returns (outcome, message). The bug caused the direction
# in the message to be the opposite of what it should be.

def test_too_high_message_says_lower():
    # Guess is above the secret — player must go LOWER, not higher
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in message, got: {message}"
    assert "HIGHER" not in message, f"Message should not say 'HIGHER' when guess is too high"

def test_too_low_message_says_higher():
    # Guess is below the secret — player must go HIGHER, not lower
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in message, got: {message}"
    assert "LOWER" not in message, f"Message should not say 'LOWER' when guess is too low"

def test_correct_guess_message():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message
