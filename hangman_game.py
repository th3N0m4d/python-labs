import random


def get_category_name(category_type):
    if category_type.upper() == "F":
        return "fruit"

    return "vegetable"


def filter_by_type(words, category_type):
    category = get_category_name(category_type)
    return [item for item in words if item["type"] == category]


def reveal_character(word, correct_guesses):
    word_display = ""
    for char in word.lower():
        if char in correct_guesses:
            word_display += char.upper()
        else:
            word_display += "_ "

    return word_display


def play():
    words = [
        {"word": "Apple", "type": "fruit"},
        {"word": "Banana", "type": "fruit"},
        {"word": "Carrot", "type": "vegetable"},
        {"word": "Onion", "type": "vegetable"},
    ]

    valid_category = False
    category_type = None
    num_of_attempts = 0

    print("===========Welcome to hangman!===============")
    print("Please, select a category\n\n")

    while valid_category is False:
        category_type = input("Press [F] for Fruits 🍉 or [V] for Veggies 🥦\n")

        if category_type in ["F", "V"]:
            valid_category = True
        else:
            print("Invalid option! Try again!\n")

    word_to_guess = random.choice(filter_by_type(words, category_type))

    word_length = len(word_to_guess["word"])
    guessed_letters = []

    print("Guess the word!")
    print(word_length * "_ ")

    while num_of_attempts < 10:
        guessed_letter = input("Enter a letter to guess: ")
        letter_found = guessed_letter.lower() in word_to_guess["word"].lower()

        if len(guessed_letter) != 1 or not guessed_letter.isalpha():
            print("Please enter a single letter!")
            continue

        if guessed_letter.lower() in guessed_letters:
            print("You already guessed that letter!")
            continue

        if letter_found:
            guessed_letters.append(guessed_letter.lower())
            display = reveal_character(word_to_guess["word"], guessed_letters)
            print(f"✅ Good guess! '{guessed_letter.upper()}' is in the word.")
            print(display)

            if "_" not in display:
                print(
                    f"\n🎉 Congratulations! You guessed '{word_to_guess['word'].upper()}' correctly!"
                )
                break
        else:
            num_of_attempts += 1
            print(f"❌ Sorry, '{guessed_letter.upper()}' is not in the word.")
            print(f"Attempts remaining: {10 - num_of_attempts}")

            if num_of_attempts >= 10:
                print(f"\n💀 Game Over! The word was '{word_to_guess['word'].upper()}'")
                break


if __name__ == "__main__":
    play()
