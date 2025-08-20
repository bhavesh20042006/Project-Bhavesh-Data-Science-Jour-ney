# ☕ Simple Coffee Machine

# Menu with drinks, ingredients needed, and cost
MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}

# Available resources in the machine
resources = {"water": 300, "milk": 200, "coffee": 100}
profit = 0  # Total money earned

# Check if there are enough ingredients for the drink
def has_enough_resources(needed):
    for item in needed:
        if needed[item] > resources.get(item, 0):
            print(f"Sorry, not enough {item}.")
            return False
    return True

# Ask user to insert coins and calculate total
def get_payment():
    print("Insert coins:")
    quarters = int(input("Quarters: ")) * 0.25
    dimes = int(input("Dimes: ")) * 0.10
    nickels = int(input("Nickels: ")) * 0.05
    pennies = int(input("Pennies: ")) * 0.01
    return quarters + dimes + nickels + pennies

# Check if payment is enough and update profit
def is_payment_successful(payment, cost):
    global profit
    if payment >= cost:
        change = round(payment - cost, 2)
        print(f"Here is ${change} in change.")
        profit += cost
        return True
    print("Sorry, not enough money. Refunded.")
    return False

# Make the drink and reduce resources
def serve_drink(name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {name} ☕️. Enjoy!")

# Main loop
while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        break

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources.get('milk', 0)}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    elif choice in MENU:
        drink = MENU[choice]
        if has_enough_resources(drink["ingredients"]):
            payment = get_payment()
            if is_payment_successful(payment, drink["cost"]):
                serve_drink(choice, drink["ingredients"])

    else:
        print("Invalid choice. Please select espresso, latte, or cappuccino.")