import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"The chosen word is: {chosen_word}")
x = len(chosen_word)
placeholder = ""
for i in range(x):
    placeholder += "_"
print(placeholder)
guess = input("Guess a letter: ").lower()
print(f"You guessed: {guess}")
display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)