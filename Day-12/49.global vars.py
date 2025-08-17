# Modifying Global Scope

enemies = 1


def increase_enemies():
    global enemies
    #this shows that we can use outer variables inside a function by declaring the variable as the global variable.
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


#or by

enemies = 1


def increase_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1


enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")

