from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_making = CoffeeMaker()
sum_coins = MoneyMachine()
menu = Menu()
drink_ingredients = MenuItem
machine = MoneyMachine()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_making.report()
        sum_coins.report()
    else:
        drink = menu.find_drink(choice)
        if (coffee_making.is_resource_sufficient(drink) and
                sum_coins.make_payment(drink.cost)):
            coffee_making.make_coffee(drink)






