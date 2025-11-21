import random


def generate_bot_choice() -> int:
    return random.choice([1, 2, 3])


def is_rock(choice: int) -> bool:
    return choice == 1


def is_paper(choice: int) -> bool:
    return choice == 2


def is_scissors(choice: int) -> bool:
    return choice == 3


def rock_wins(choice_one: int, choice_two: int) -> bool:
    return is_rock(choice_one) and is_scissors(choice_two)


def paper_wins(choice_one: int, choice_two: int) -> bool:
    return is_rock(choice_one) and is_paper(choice_two)


def scissors_wins(choice_one: int, choice_two: int) -> bool:
    return is_paper(choice_one) and is_scissors(choice_two)


def evaluate_choice(human_choice: int, bot_choice: int) -> bool:
    if rock_wins(human_choice, bot_choice):
        return True

    if paper_wins(human_choice, bot_choice):
        return True

    if scissors_wins(human_choice, bot_choice):
        return True

    return False
