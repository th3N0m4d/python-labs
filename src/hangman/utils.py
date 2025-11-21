"""Utility functions for hangman game."""

from typing import List


def reveal_letters(word: str, guessed_letters: List[str]) -> str:
    """Reveal guessed letters in the word.

    Args:
        word: The target word.
        guessed_letters: List of correctly guessed letters.

    Returns:
        String showing revealed letters and underscores for hidden letters.
    """
    display = []
    for char in word.upper():
        if char.upper() in [letter.upper() for letter in guessed_letters]:
            display.append(char)
        else:
            display.append("_")
    return " ".join(display)


def is_word_complete(word: str, guessed_letters: List[str]) -> bool:
    """Check if the word has been completely guessed.

    Args:
        word: The target word.
        guessed_letters: List of correctly guessed letters.

    Returns:
        True if all letters in the word have been guessed.
    """
    word_upper = word.upper()
    guessed_upper = [letter.upper() for letter in guessed_letters]

    for char in word_upper:
        if char.isalpha() and char not in guessed_upper:
            return False
    return True


def validate_input(input_str: str) -> bool:
    """Validate user input for letter guesses.

    Args:
        input_str: The input string to validate.

    Returns:
        True if input is a single alphabetic character.
    """
    return len(input_str) == 1 and input_str.isalpha()


def format_guess_list(guesses: List[str]) -> str:
    """Format a list of guesses for display.

    Args:
        guesses: List of letter guesses.

    Returns:
        Formatted string of guesses.
    """
    if not guesses:
        return "None"
    return ", ".join(sorted(guesses, key=str.upper))


def calculate_score(word_length: int, wrong_attempts: int, max_attempts: int) -> int:
    """Calculate game score based on performance.

    Args:
        word_length: Length of the guessed word.
        wrong_attempts: Number of wrong attempts made.
        max_attempts: Maximum allowed attempts.

    Returns:
        Calculated score (higher is better).
    """
    if wrong_attempts >= max_attempts:
        return 0

    # Base score based on word length
    base_score = word_length * 10

    # Bonus for fewer wrong attempts
    accuracy_bonus = (max_attempts - wrong_attempts) * 5

    return base_score + accuracy_bonus
