"""Tests for the wordlist module."""

import pytest
from src.hangman.wordlist import WordList


class TestWordList:
    """Test the WordList class."""

    def test_init(self, sample_wordlist):
        """Test WordList initialization."""
        assert len(sample_wordlist.get_all_words()) > 0

    def test_get_categories(self, sample_wordlist):
        """Test getting categories."""
        categories = sample_wordlist.get_categories()
        assert "fruit" in categories
        assert "vegetable" in categories
        assert len(categories) >= 2

    def test_get_words_by_category(self, sample_wordlist):
        """Test filtering words by category."""
        fruits = sample_wordlist.get_words_by_category("fruit")
        assert len(fruits) > 0
        assert all(word["type"] == "fruit" for word in fruits)

        vegetables = sample_wordlist.get_words_by_category("vegetable")
        assert len(vegetables) > 0
        assert all(word["type"] == "vegetable" for word in vegetables)

    def test_get_words_by_category_case_insensitive(self, sample_wordlist):
        """Test that category filtering is case insensitive."""
        fruits_lower = sample_wordlist.get_words_by_category("fruit")
        fruits_upper = sample_wordlist.get_words_by_category("FRUIT")
        fruits_mixed = sample_wordlist.get_words_by_category("Fruit")

        assert fruits_lower == fruits_upper == fruits_mixed

    def test_get_random_word(self, sample_wordlist):
        """Test getting a random word from category."""
        word = sample_wordlist.get_random_word("fruit")
        assert word["type"] == "fruit"
        assert "word" in word
        assert len(word["word"]) > 0

    def test_get_random_word_invalid_category(self, sample_wordlist):
        """Test getting random word from invalid category raises error."""
        with pytest.raises(ValueError):
            sample_wordlist.get_random_word("invalid_category")

    def test_add_word(self, sample_wordlist):
        """Test adding a new word."""
        initial_count = len(sample_wordlist.get_all_words())
        sample_wordlist.add_word("mango", "fruit")

        assert len(sample_wordlist.get_all_words()) == initial_count + 1
        fruits = sample_wordlist.get_words_by_category("fruit")
        assert any(word["word"] == "Mango" for word in fruits)

    def test_get_all_words_returns_copy(self, sample_wordlist):
        """Test that get_all_words returns a copy, not the original list."""
        words1 = sample_wordlist.get_all_words()
        words2 = sample_wordlist.get_all_words()

        # Modify one list
        words1.append({"word": "Test", "type": "test"})

        # Original should be unchanged
        assert len(words1) != len(words2)
        assert len(sample_wordlist.get_all_words()) == len(words2)
