import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"The chosen word is: {chosen_word}")
guess = input("Guess a letter: ").lower()
print(f"You guessed: {guess}")
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
