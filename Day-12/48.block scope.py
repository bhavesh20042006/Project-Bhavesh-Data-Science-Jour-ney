#there is no block scope in python
game_level = 3
enemies = ["skeletons", "zombies","alien"]

if game_level < 5:
    new_enemy = enemies[0]
#new variables can be created inside variables and will not affect the outer scope
print(new_enemy)


def create_enemy():
    if game_level < 5:
        new_enemy = enemies[1]
#new variables can be created inside functions and cannot be accessed from outside unless called
    print(new_enemy)
