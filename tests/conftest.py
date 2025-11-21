"""Pytest configuration and shared fixtures."""

import pytest
from src.hangman.wordlist import WordList
from src.hangman.game import HangmanGame


@pytest.fixture
def sample_wordlist():
    """Create a WordList instance for testing."""
    return WordList()


@pytest.fixture
def sample_words():
    """Sample word data for testing."""
    return [
        {"word": "Apple", "type": "fruit"},
        {"word": "Banana", "type": "fruit"},
        {"word": "Carrot", "type": "vegetable"},
        {"word": "Onion", "type": "vegetable"},
    ]


@pytest.fixture
def hangman_game():
    """Create a HangmanGame instance for testing."""
    return HangmanGame(max_attempts=6)


@pytest.fixture
def game_with_word(hangman_game):
    """Create a game instance with a preset word."""
    hangman_game.current_word = {"word": "PYTHON", "type": "programming"}
    return hangman_game
