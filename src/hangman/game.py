"""Core game logic for hangman game."""

from typing import Dict, Set
from .wordlist import WordList
from .ui import GameUI
from .utils import reveal_letters, is_word_complete, calculate_score


class HangmanGame:
    """Main game class that orchestrates the hangman game."""

    def __init__(self, max_attempts: int = 6):
        """Initialize the hangman game.

        Args:
            max_attempts: Maximum number of wrong attempts allowed.
        """
        self.wordlist = WordList()
        self.ui = GameUI()
        self.max_attempts = max_attempts
        self.reset_game()

    def reset_game(self) -> None:
        """Reset the game state for a new game."""
        self.current_word: Dict[str, str] = {}
        self.correct_guesses: Set[str] = set()
        self.wrong_guesses: Set[str] = set()
        self.wrong_attempts = 0
        self.game_over = False
        self.won = False

    def setup_game(self) -> None:
        """Set up a new game by selecting category and word."""
        categories = self.wordlist.get_categories()
        self.ui.display_categories(categories)

        selected_category = self.ui.get_category_choice(categories)
        self.current_word = self.wordlist.get_random_word(selected_category)

        print(f"\n🎯 Category: {selected_category.title()}")
        print(f"📏 Word length: {len(self.current_word['word'])} letters")

    def process_guess(self, letter: str) -> bool:
        """Process a letter guess.

        Args:
            letter: The guessed letter.

        Returns:
            True if the guess was correct, False otherwise.
        """
        letter_upper = letter.upper()

        # Check if already guessed
        if letter_upper in self.correct_guesses or letter_upper in self.wrong_guesses:
            self.ui.display_already_guessed()
            return False

        # Check if letter is in word
        if letter_upper in self.current_word["word"].upper():
            self.correct_guesses.add(letter_upper)
            self.ui.display_correct_guess()
            return True
        else:
            self.wrong_guesses.add(letter_upper)
            self.wrong_attempts += 1
            self.ui.display_wrong_guess()
            return False

    def check_game_state(self) -> None:
        """Check if the game has ended (won or lost)."""
        word = self.current_word["word"]

        if is_word_complete(word, list(self.correct_guesses)):
            self.won = True
            self.game_over = True
        elif self.wrong_attempts >= self.max_attempts:
            self.won = False
            self.game_over = True

    def get_word_display(self) -> str:
        """Get the current display state of the word.

        Returns:
            String showing revealed and hidden letters.
        """
        return reveal_letters(self.current_word["word"], list(self.correct_guesses))

    def get_attempts_left(self) -> int:
        """Get the number of attempts remaining.

        Returns:
            Number of attempts left.
        """
        return self.max_attempts - self.wrong_attempts

    def get_score(self) -> int:
        """Calculate the current game score.

        Returns:
            Calculated score based on performance.
        """
        word_length = len(self.current_word["word"])
        return calculate_score(word_length, self.wrong_attempts, self.max_attempts)

    def play_round(self) -> None:
        """Play a single round of the game."""
        while not self.game_over:
            # Display current game state
            word_display = self.get_word_display()
            wrong_list = list(self.wrong_guesses)
            attempts_left = self.get_attempts_left()

            self.ui.display_game_state(word_display, wrong_list, attempts_left)

            # Get user guess
            guess = self.ui.get_letter_guess()

            # Process the guess
            self.process_guess(guess)

            # Check if game has ended
            self.check_game_state()

        # Display end game message
        word = self.current_word["word"]
        if self.won:
            total_attempts = len(self.correct_guesses) + self.wrong_attempts
            self.ui.display_win(word, total_attempts)
            score = self.get_score()
            print(f"🎯 Final Score: {score} points")
        else:
            self.ui.display_lose(word)

    def play(self) -> None:
        """Main game loop with option to play multiple rounds."""
        self.ui.display_welcome()

        while True:
            self.reset_game()
            self.setup_game()
            self.play_round()

            if not self.ui.ask_play_again():
                print("\n👋 Thanks for playing! Goodbye!")
                break
