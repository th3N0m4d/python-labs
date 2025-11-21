"""User interface module for hangman game."""

from typing import List


class GameUI:
    """Handles all user interface interactions for the hangman game."""

    @staticmethod
    def display_welcome() -> None:
        """Display welcome message."""
        print("=" * 50)
        print("🎮 Welcome to Hangman! 🎮")
        print("=" * 50)
        print("Guess the word letter by letter!")
        print("You have limited attempts. Good luck!")
        print()

    @staticmethod
    def display_categories(categories: List[str]) -> None:
        """Display available categories.

        Args:
            categories: List of available category names.
        """
        print("📂 Available Categories:")
        for i, category in enumerate(categories, 1):
            emoji = "🍎" if category == "fruit" else "🥕"
            print(f"  [{i}] {emoji} {category.title()}")
        print()

    @staticmethod
    def get_category_choice(categories: List[str]) -> str:
        """Get user's category choice.

        Args:
            categories: List of available categories.

        Returns:
            Selected category name.
        """
        while True:
            try:
                choice = input("Select a category (enter number): ").strip()
                index = int(choice) - 1
                if 0 <= index < len(categories):
                    return categories[index]
                else:
                    print(f"❌ Please enter a number between 1 and {len(categories)}")
            except ValueError:
                print("❌ Please enter a valid number")

    @staticmethod
    def display_game_state(
        word_display: str, wrong_guesses: List[str], attempts_left: int
    ) -> None:
        """Display current game state.

        Args:
            word_display: Current state of the word with revealed letters.
            wrong_guesses: List of incorrect guesses.
            attempts_left: Number of attempts remaining.
        """
        print("\n" + "=" * 40)
        print(f"📝 Word: {word_display}")
        print(
            f"❌ Wrong guesses: {', '.join(wrong_guesses) if wrong_guesses else 'None'}"
        )
        print(f"💪 Attempts left: {attempts_left}")
        print("=" * 40)

    @staticmethod
    def get_letter_guess() -> str:
        """Get a letter guess from the user.

        Returns:
            Single letter guess (uppercase).
        """
        while True:
            guess = input("\n🔤 Enter a letter: ").strip().upper()

            if len(guess) != 1:
                print("❌ Please enter exactly one letter!")
                continue

            if not guess.isalpha():
                print("❌ Please enter a valid letter!")
                continue

            return guess

    @staticmethod
    def display_correct_guess() -> None:
        """Display message for correct guess."""
        print("✅ Great! That letter is in the word!")

    @staticmethod
    def display_wrong_guess() -> None:
        """Display message for wrong guess."""
        print("❌ Sorry! That letter is not in the word.")

    @staticmethod
    def display_already_guessed() -> None:
        """Display message for already guessed letter."""
        print("🔄 You already guessed that letter!")

    @staticmethod
    def display_win(word: str, attempts_used: int) -> None:
        """Display win message.

        Args:
            word: The word that was guessed.
            attempts_used: Number of attempts used.
        """
        print("\n" + "🎉" * 20)
        print(f"🏆 CONGRATULATIONS! 🏆")
        print(f"You guessed '{word}' correctly!")
        print(f"Attempts used: {attempts_used}")
        print("🎉" * 20)

    @staticmethod
    def display_lose(word: str) -> None:
        """Display lose message.

        Args:
            word: The word that should have been guessed.
        """
        print("\n" + "💀" * 20)
        print(f"😞 GAME OVER! 😞")
        print(f"The word was: '{word}'")
        print("Better luck next time!")
        print("💀" * 20)

    @staticmethod
    def ask_play_again() -> bool:
        """Ask if user wants to play again.

        Returns:
            True if user wants to play again, False otherwise.
        """
        while True:
            choice = input("\n🔄 Would you like to play again? (y/n): ").strip().lower()
            if choice in ["y", "yes"]:
                return True
            elif choice in ["n", "no"]:
                return False
            else:
                print("❌ Please enter 'y' for yes or 'n' for no")
