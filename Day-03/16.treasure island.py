print("welcome to the treasure island")
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Your mission is to find the treasure.")

choice_1 = input('You are at a crossroad. Where do you want to go? Type "left" or "right": ').lower()
if choice_1 == "left":
    choice_2 = input('You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat or "swim" to swim across: ').lower()
    if choice_2 == "wait":
        choice_3 = input('You have arrived on the island safely. There is a house with three doors: "red", "yellow", and "blue". Which gate will you enter? ').lower()
        if choice_3 == "red":
            print("Game over. You were burned by fire.")
        elif choice_3 == "blue":
            print("Game over. You were eaten by beasts.")
        elif choice_3 == "yellow":
            print("Congratulations, you found the treasure! You win!")
        else:
            print("Please enter a valid choice.")
    else:
        print("Game over. You were attacked by a trout.")
else:
    print("Game over. You fell into a hole.")