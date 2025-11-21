"""Tests for the game module."""

import pytest
from src.hangman.game import HangmanGame


class TestHangmanGame:
    """Test the HangmanGame class."""

    def test_init(self):
        """Test game initialization."""
        game = HangmanGame(max_attempts=5)
        assert game.max_attempts == 5
        assert game.wrong_attempts == 0
        assert len(game.correct_guesses) == 0
        assert len(game.wrong_guesses) == 0
        assert not game.game_over
        assert not game.won

    def test_reset_game(self, hangman_game):
        """Test game reset functionality."""
        # Set some game state
        hangman_game.wrong_attempts = 3
        hangman_game.correct_guesses.add("A")
        hangman_game.wrong_guesses.add("X")
        hangman_game.game_over = True

        # Reset and verify
        hangman_game.reset_game()
        assert hangman_game.wrong_attempts == 0
        assert len(hangman_game.correct_guesses) == 0
        assert len(hangman_game.wrong_guesses) == 0
        assert not hangman_game.game_over
        assert not hangman_game.won

    def test_process_guess_correct(self, game_with_word):
        """Test processing a correct guess."""
        result = game_with_word.process_guess("P")
        assert result is True
        assert "P" in game_with_word.correct_guesses
        assert "P" not in game_with_word.wrong_guesses
        assert game_with_word.wrong_attempts == 0

    def test_process_guess_wrong(self, game_with_word):
        """Test processing a wrong guess."""
        result = game_with_word.process_guess("X")
        assert result is False
        assert "X" not in game_with_word.correct_guesses
        assert "X" in game_with_word.wrong_guesses
        assert game_with_word.wrong_attempts == 1

    def test_process_guess_duplicate(self, game_with_word):
        """Test processing a duplicate guess."""
        game_with_word.process_guess("P")
        result = game_with_word.process_guess("P")
        assert result is False
        assert len(game_with_word.correct_guesses) == 1

    def test_get_word_display(self, game_with_word):
        """Test word display generation."""
        # No guesses
        display = game_with_word.get_word_display()
        assert display == "_ _ _ _ _ _"

        # Some correct guesses
        game_with_word.correct_guesses.add("P")
        game_with_word.correct_guesses.add("Y")
        display = game_with_word.get_word_display()
        assert "P" in display
        assert "Y" in display
        assert "_" in display

    def test_check_game_state_win(self, game_with_word):
        """Test win condition detection."""
        # Guess all letters in PYTHON
        for letter in "PYTHON":
            game_with_word.correct_guesses.add(letter)

        game_with_word.check_game_state()
        assert game_with_word.won is True
        assert game_with_word.game_over is True

    def test_check_game_state_lose(self, game_with_word):
        """Test lose condition detection."""
        game_with_word.wrong_attempts = game_with_word.max_attempts

        game_with_word.check_game_state()
        assert game_with_word.won is False
        assert game_with_word.game_over is True

    def test_get_attempts_left(self, game_with_word):
        """Test attempts left calculation."""
        assert game_with_word.get_attempts_left() == 6

        game_with_word.wrong_attempts = 3
        assert game_with_word.get_attempts_left() == 3

    def test_get_score(self, game_with_word):
        """Test score calculation."""
        # Perfect game (no wrong attempts)
        score = game_with_word.get_score()
        assert score > 0

        # Game with wrong attempts
        game_with_word.wrong_attempts = 2
        lower_score = game_with_word.get_score()
        assert lower_score < score

        # Game over (max wrong attempts)
        game_with_word.wrong_attempts = game_with_word.max_attempts
        final_score = game_with_word.get_score()
        assert final_score == 0
