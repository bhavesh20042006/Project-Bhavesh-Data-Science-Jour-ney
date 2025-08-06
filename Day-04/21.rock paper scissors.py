import random
user_choice = int(input("what do you choose? type 0 for rock, 1 for paper and 2 for scissors: "))
choices = ["rock", "paper", "scissors"]
computer_choice = random.randint(0, 2)
print(f"computer choose {choices[computer_choice]}")

if user_choice == 0:
    print("user choose rock")
    if computer_choice == 0:
        print("draw")
    elif computer_choice == 1:
        print("computer wins")
    elif computer_choice == 2:
        print("user wins")

if user_choice == 1:
    print("user choose paper")
    if computer_choice == 0:
        print("user wins")
    elif computer_choice == 1:
        print("draw")
    elif computer_choice == 2:
        print("computer wins")

if user_choice == 2:
    print("user choose scissors")
    if computer_choice == 0:
        print("computer wins")
    elif computer_choice == 1:
        print("user wins")
    elif computer_choice == 2:
        print("draw")

