try:
    age = int(input("How old are you?"))
except ValueError:
    print("you have typed in a invalid number . please try again with a numerical value like 15.")
    age = int(input("How old are you?"))
if age >= 18:
    print(f"You can drive at age {age}.")
