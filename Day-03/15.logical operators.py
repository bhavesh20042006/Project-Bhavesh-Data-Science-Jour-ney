#LOGICAL OPERATORS and , or , not
'''and both needs to be true for true
or both needs to be false to be false
not if gets reversed'''



print("welcome to the roller coaster.")
height = int(input("what is your height in cm?"))
if height >= 120:
    print("you can ride the roller coaster.")
    bill = 0
    age = int(input("what is your age?"))
    if age < 12 :
        bill += 5
        print("youth tickets are 5 dollars")
    elif age <= 18 :
        bill += 7
        print("teenagers tickets are 7 dollars")
    elif age >= 45 and age <=55 :                 #testing logical operators for midlife crises.
        print("everything is going to be fine. have a free ride on us")
    else:
        bill += 12
        print("adults tickets are 12 dollars")
    want_photo = input("do you want to click a phoyo? type y for yes and n for no!")
    if want_photo == "y":
        bill += 3
    print(f"you have to pay {bill} dollars.")
else:
    print("you have to grow taller before you ride.")