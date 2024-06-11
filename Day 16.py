#This is just a sample.
#This code require all the other modules to run properly.

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_machine = CoffeeMaker()
my_menu = Menu()
my_money_machine = MoneyMachine()

is_on = True

while is_on:
    choice = input(f"What would you like? ({my_menu.get_items()}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        my_machine.report()
        my_money_machine.report()
    else:
        drink = my_menu.find_drink(choice)
        if my_machine.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
                my_machine.make_coffee(drink)