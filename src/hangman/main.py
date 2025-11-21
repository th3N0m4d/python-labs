"""Main entry point for the hangman game."""

from .game import HangmanGame


def main() -> None:
    """Main function to start the hangman game."""
    try:
        game = HangmanGame(max_attempts=6)
        game.play()
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Thanks for playing!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        print("Please try again.")


if __name__ == "__main__":
    main()
