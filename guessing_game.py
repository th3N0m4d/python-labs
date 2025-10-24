from random import randint as rand_int

def guessing_game():
    """
    A simple guessing game where the player has 7 attempts to guess a randomly generated number.    
    
    Args:
        None
        
    Returns:
        None        
    """
    print('Welcome to the guessing game! You have seven attempts at guessing the number. Good luck!')
    
    lower_bound = int(input('Please, enter the lower bound: '))
    upper_bound = int(input('Please, enter the upper bound: '))
    
    max_attempts = 0
    num_to_guess = rand_int(lower_bound, upper_bound)
    
    print(f'Now, try guessing a number between {lower_bound} and {upper_bound}.')
    
    while max_attempts < 7:
        
        max_attempts+=1
        
        choice = int(input('What is your guess? '))
        
        if num_to_guess == choice:
            print('Congratulations! You guessed the correct number')
        elif choice < num_to_guess:
            print('Too low! Try a higher number.')
        else:
            print('Too high! Try a lower number.')

    print(f'Game over! You\'ve used all {max_attempts} attempts. The correct number was {num_to_guess}.')

if __name__ == "__main__":
    guessing_game()
