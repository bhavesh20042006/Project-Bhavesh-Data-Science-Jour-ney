print("welcome to the python pizza deleveries.")
size = input("what size pizza do you want?S,M or L: ")
pepperoni = input("do you want pepperoni on your pizza?Y or N: ")
extra_cheese = input("do you want extra cheese? Y or N: ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("you typed wrong inputs.")



if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3


if extra_cheese == "Y":
    bill += 1




print(f"you have to pay {bill} dollars.")


