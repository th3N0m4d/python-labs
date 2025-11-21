"""Tests for utility functions."""

import pytest
from src.hangman.utils import (
    reveal_letters,
    is_word_complete,
    validate_input,
    format_guess_list,
    calculate_score,
)


class TestUtilityFunctions:
    """Test utility functions."""

    def test_reveal_letters_no_guesses(self):
        """Test reveal_letters with no guesses."""
        result = reveal_letters("PYTHON", [])
        assert result == "_ _ _ _ _ _"

    def test_reveal_letters_some_guesses(self):
        """Test reveal_letters with some correct guesses."""
        result = reveal_letters("PYTHON", ["P", "Y"])
        assert result == "P Y _ _ _ _"

    def test_reveal_letters_all_guesses(self):
        """Test reveal_letters with all letters guessed."""
        result = reveal_letters("PYTHON", ["P", "Y", "T", "H", "O", "N"])
        assert result == "P Y T H O N"

    def test_reveal_letters_case_insensitive(self):
        """Test that reveal_letters is case insensitive."""
        result1 = reveal_letters("Python", ["p", "y"])
        result2 = reveal_letters("PYTHON", ["P", "Y"])
        assert result1 == result2

    def test_is_word_complete_false(self):
        """Test is_word_complete when word is not complete."""
        assert is_word_complete("PYTHON", ["P", "Y"]) is False
        assert is_word_complete("PYTHON", []) is False

    def test_is_word_complete_true(self):
        """Test is_word_complete when word is complete."""
        assert is_word_complete("PYTHON", ["P", "Y", "T", "H", "O", "N"]) is True

    def test_is_word_complete_case_insensitive(self):
        """Test that is_word_complete is case insensitive."""
        result1 = is_word_complete("Python", ["p", "y", "t", "h", "o", "n"])
        result2 = is_word_complete("PYTHON", ["P", "Y", "T", "H", "O", "N"])
        assert result1 == result2 == True

    def test_validate_input_valid(self):
        """Test validate_input with valid inputs."""
        assert validate_input("A") is True
        assert validate_input("z") is True

    def test_validate_input_invalid(self):
        """Test validate_input with invalid inputs."""
        assert validate_input("") is False
        assert validate_input("AB") is False
        assert validate_input("1") is False
        assert validate_input("!") is False
        assert validate_input(" ") is False

    def test_format_guess_list_empty(self):
        """Test format_guess_list with empty list."""
        assert format_guess_list([]) == "None"

    def test_format_guess_list_with_guesses(self):
        """Test format_guess_list with guesses."""
        result = format_guess_list(["Z", "A", "X"])
        assert result == "A, X, Z"  # Should be sorted

    def test_calculate_score_perfect_game(self):
        """Test score calculation for perfect game."""
        score = calculate_score(word_length=6, wrong_attempts=0, max_attempts=6)
        assert score == 90  # 6*10 + (6-0)*5

    def test_calculate_score_with_mistakes(self):
        """Test score calculation with some mistakes."""
        score = calculate_score(word_length=6, wrong_attempts=2, max_attempts=6)
        assert score == 80  # 6*10 + (6-2)*5

    def test_calculate_score_game_over(self):
        """Test score calculation for lost game."""
        score = calculate_score(word_length=6, wrong_attempts=6, max_attempts=6)
        assert score == 0

    @pytest.mark.parametrize(
        "word,guesses,expected",
        [
            ("CAT", [], "_ _ _"),
            ("CAT", ["C"], "C _ _"),
            ("CAT", ["C", "A"], "C A _"),
            ("CAT", ["C", "A", "T"], "C A T"),
            ("HELLO", ["L"], "_ _ L L _"),
        ],
    )
    def test_reveal_letters_parametrized(self, word, guesses, expected):
        """Test reveal_letters with various inputs."""
        assert reveal_letters(word, guesses) == expected
