from .ui import GameUI
from .utils import evaluate_choice, generate_bot_choice


class RockPaperScissors:
    def __init__(self) -> None:
        self.ui = GameUI()

    def play(self) -> None:
        self.ui.display_game_rules()

        while True:
            self.ui.display_keyboard_commands()
            user_choice = int(input(""))
            bot_choice = generate_bot_choice()

            print(f"\nUser chose: {user_choice}\nComputer chose: {bot_choice}")

            result = evaluate_choice(user_choice, bot_choice)

            if result:
                print("User wins")
            else:
                print("Bot wins")

            print("")
            print("-" * 10)
            print("")
