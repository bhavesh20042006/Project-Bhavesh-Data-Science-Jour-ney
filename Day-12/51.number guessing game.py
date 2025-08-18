logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

import random

print(logo)

# Choosing a random number between 1 and 100
random_choice = random.randint(1, 100)

# Function to set difficulty
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def game():
    if difficulty == "easy":
        number_of_turns = 10
    elif difficulty == "hard":
        number_of_turns = 5
    else:
        print("Invalid difficulty. Defaulting to easy.")
        number_of_turns = 10

    game_ends = False

    while not game_ends:
        print(f"You have {number_of_turns} attempts remaining to guess the number.")
        try:
            user_input = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_input > random_choice:
            print("Too high.\nGuess again.")
        elif user_input < random_choice:
            print("Too low.\nGuess again.")
        else:
            print(f"You got it! The answer was {random_choice}.")
            game_ends = True
            continue

        number_of_turns -= 1
        if number_of_turns == 0:
            print(f"You've run out of guesses. The number was {random_choice}. Game over.")
            game_ends = True

game()