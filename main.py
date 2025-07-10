import random
from art1 import logo

NUMBER_EASY_GUESSES = 10
NUMBER_HARD_GUESSES = 5

def check_guess(user_guess, guess_this_number, turns):
    """Checks the user guess against the number to be guessed
    reduces the number of turns by 1 if the guess is incorrect
    tells the user if their guess is too high or too low to the numbre to be guessed
    """
    if user_guess < guess_this_number:
        print("Your guess was too low. Guess again.")
        return turns - 1
    elif user_guess > guess_this_number:
        print("Your guess was too high. Guess again.")
        return turns - 1
    else:
        print(f"Your guess was right. The number was {guess_this_number}.")

def set_level():
    """This function sets the difficulty level of the game"""
    user_difficulty = input("Select your difficulty. Select 'easy' for easy and 'hard' for hard.")
    if user_difficulty == "easy":
        # print(f"You have {NUMBER_EASY_GUESSES} chances remaining to guess the number.")
        return NUMBER_EASY_GUESSES
    elif user_difficulty == "hard":
        # print(f"You have {NUMBER_HARD_GUESSES} chances remaining to guess the number.")
        return NUMBER_HARD_GUESSES
    else:
        print("Enter the correct difficulty to proceed.")


def game():
    print(logo)
    print("Welcome to the Guess My Number game!")

    # Choose a random number between 1 and 100
    print("I'm thinking of a number between 1 and 100. Guess the number")
    guess_this_number = random.randint(1, 100)

    #Sets the number of turns or guesses based on the level the user selects
    turns = set_level()

    #tracks the number of turns the user has remaining and reduce it by 1 for each incorrect guess

    #repeat the guessing game until they get it right or they run of guesses if they got it wrong
    user_guess = 0
    while user_guess != guess_this_number:
        print(f"You have {turns} chances remaining to guess the number.")

        # Let the user guess the number
        user_guess = int(input("Enter your guess"))

        #Track the number of turns remaining to get the guess right
        turns = check_guess(user_guess, guess_this_number, turns)
        if turns == 0:
            print("You've run out of guesses. You lose.")
            print(f"The answer was {guess_this_number}")
            return
        # elif user_guess != guess_this_number:
        print("Guess again")

game()