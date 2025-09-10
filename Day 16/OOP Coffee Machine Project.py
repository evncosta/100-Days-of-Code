from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    drink_of_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if drink_of_choice == "off":
        break
    elif drink_of_choice == "report":
        coffee_maker.report()
        money_machine.report()
        continue
    elif drink_of_choice not in ["espresso", "latte", "cappuccino"]:
        print("Invalid input.")
        continue

    drink = menu.find_drink(drink_of_choice)
    if drink is None:
        continue

    if not coffee_maker.is_resource_sufficient(drink):
        continue

    if money_machine.make_payment(drink.cost):
        coffee_maker.make_drink(drink)