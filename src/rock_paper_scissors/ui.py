from typing import List


class GameUI:
    """Handles all user interface for the rock, paper, scissors game."""

    @staticmethod
    def display_game_rules() -> None:
        """Display the game rules"""
        print(
            """Winning Rules as follows:
        Rock vs paper -> paper wins
        Rock vs scissor -> Rock wins
        paper vs scissor -> scissor wins."""
        )
        print()

    @staticmethod
    def display_keyboard_commands() -> None:
        """Display keyboard commands for playing the game"""
        print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    @staticmethod
    def display_result(user_wins: bool) -> None:
        if user_wins:
            print("You won! 🥇")
        else:
            print("You lose... Try again! 😔")
