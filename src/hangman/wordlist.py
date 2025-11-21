"""Word list management for hangman game."""

import random
from typing import List, Dict


class WordList:
    """Manages the word list for the hangman game."""

    def __init__(self):
        """Initialize the word list with default words."""
        self._words = [
            {"word": "Apple", "type": "fruit"},
            {"word": "Banana", "type": "fruit"},
            {"word": "Orange", "type": "fruit"},
            {"word": "Grape", "type": "fruit"},
            {"word": "Carrot", "type": "vegetable"},
            {"word": "Onion", "type": "vegetable"},
            {"word": "Potato", "type": "vegetable"},
            {"word": "Tomato", "type": "vegetable"},
        ]

    def get_categories(self) -> List[str]:
        """Get all available categories.

        Returns:
            List of unique category names.
        """
        return list(set(word["type"] for word in self._words))

    def get_words_by_category(self, category: str) -> List[Dict[str, str]]:
        """Get words filtered by category.

        Args:
            category: The category to filter by.

        Returns:
            List of word dictionaries matching the category.
        """
        return [
            word for word in self._words if word["type"].lower() == category.lower()
        ]

    def get_random_word(self, category: str) -> Dict[str, str]:
        """Get a random word from the specified category.

        Args:
            category: The category to select from.

        Returns:
            Random word dictionary from the category.

        Raises:
            ValueError: If category has no words.
        """
        words = self.get_words_by_category(category)
        if not words:
            raise ValueError(f"No words found for category: {category}")
        return random.choice(words)

    def add_word(self, word: str, category: str) -> None:
        """Add a new word to the word list.

        Args:
            word: The word to add.
            category: The category for the word.
        """
        self._words.append({"word": word.capitalize(), "type": category.lower()})

    def get_all_words(self) -> List[Dict[str, str]]:
        """Get all words in the list.

        Returns:
            Complete list of word dictionaries.
        """
        return self._words.copy()
