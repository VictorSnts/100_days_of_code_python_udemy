from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

turn_off = False


def desligar_maquina():
    """Desliga a maquina"""
    print("The machine is shutting down.")
    global turn_off
    turn_off = True
    return


def get_input(coffee_maker, money_machine):
    """Pergunta ao usuario o tipo do cafe e retirna o objeto, caso seja valido"""
    menu = Menu()
    user_input = input(f"What kind of coffee would you like?\n{menu.get_items()} \n").lower()
    type_coffee = Menu()

    if user_input == "off":
        return desligar_maquina()
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif type_coffee.find_drink(user_input):
        return type_coffee.find_drink(user_input)


def coffe_machine():
    coffee = CoffeeMaker()
    money = MoneyMachine()
    while not turn_off:
        coffee_type = get_input(coffee, money)
        if coffee_type:
            if coffee.is_resource_sufficient(coffee_type):
                print(f"The selected coffee costs ${coffee_type.cost}")
                if money.make_payment(coffee_type.cost):
                    coffee.make_coffee(coffee_type)


coffe_machine()
