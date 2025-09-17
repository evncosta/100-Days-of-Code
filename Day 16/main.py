# OOP Coffee Machine - Main interface for coffee ordering system
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Initialize system components
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# Main program loop
while True:
    drink_of_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # Handle system commands
    if drink_of_choice == "off":
        break
    elif drink_of_choice == "report":
        # Display resource and revenue reports
        coffee_maker.report()
        money_machine.report()
        continue
    elif drink_of_choice not in ["espresso", "latte", "cappuccino"]:
        print("Invalid input.")
        continue

    # Find drink object from menu
    drink = menu.find_drink(drink_of_choice)
    if drink is None:
        continue

    # Check if resources are sufficient
    if not coffee_maker.is_resource_sufficient(drink):
        continue

    # Process payment and make drink if successful
    if money_machine.make_payment(drink.cost):
        coffee_maker.make_drink(drink)
