"""Main entry point for the rock-paper-scissors game."""

from .game import RockPaperScissors


def main() -> None:
    """Main function to start the rock-paper-scissors game."""
    try:
        game = RockPaperScissors()
        game.play()
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Thanks for playing!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        print("Please try again.")


if __name__ == "__main__":
    main()
