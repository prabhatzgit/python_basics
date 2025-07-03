from Tools.scripts.pep384_macrocheck import dprint

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"what would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        # 1. Print Report
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        # 2. Check Resources are sufficient
        # Process Coins and check transaction successful
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
