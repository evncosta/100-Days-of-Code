MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def check_resources(drink_name):
    drink = MENU[drink_name]
    ingredients = drink["ingredients"]
    for ingredient, amount_needed in ingredients.items():
        if resources.get(ingredient, 0) < amount_needed:
            print(f"Sorry, there's not enough {ingredient}.")
            return False
    return True


def make_drink(drink_name):
    drink = MENU[drink_name]
    ingredients = drink["ingredients"]
    for ingredient, amount_needed in ingredients.items():
        resources[ingredient] -= amount_needed
    print(f"Here is your {drink_name}! Enjoy! ☕")


while True:
    drink_of_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if drink_of_choice not in ["espresso", "latte", "cappuccino", "report", "off"]:
        print("Invalid input.")
        continue

    if drink_of_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
        continue
    elif drink_of_choice == "off":
        break

    if not check_resources(drink_of_choice):
        continue

    print("Please insert your coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    value_quarter = 0.25
    value_dime = 0.10
    value_nickel = 0.05
    value_penny = 0.01

    total_given = (quarters * value_quarter +
                   dimes * value_dime +
                   nickels * value_nickel +
                   pennies * value_penny)

    drink_cost = MENU[drink_of_choice]["cost"]

    if total_given < drink_cost:
        print("Sorry, that's not enough money. Money refunded.")
    else:
        change = round(total_given - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} in change!")
        money += drink_cost
        make_drink(drink_of_choice)
