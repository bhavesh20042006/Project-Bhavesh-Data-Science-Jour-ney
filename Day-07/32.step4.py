import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"The chosen word is: {chosen_word}")
x = len(chosen_word)
placeholder = ""
for i in range(x):
    placeholder += "_"
print(placeholder)
game_over = False
correct_letters = []
while not game_over:
    guess = input("Guess a letter: ").lower()
    print(f"You guessed: {guess}")
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    if "_" not in display:
        game_over = True
        print("you won")
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            game_over = True
            print("you lost")