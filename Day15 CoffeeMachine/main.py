import os
import menu


def order():
    user_order = input("What would you like? (espresso/latte/cappuccino): ")
    if user_order == 'espresso':
        cost = menu.MENU['espresso']['cost']
        coffee = 'espresso'
    elif user_order == 'latte':
        cost = menu.MENU['latte']['cost']
        coffee = 'latte'
    elif user_order == 'cappuccino':
        cost = menu.MENU['cappuccino']['cost']
        coffee = 'cappuccino'
    elif user_order == 'report':
        print(menu.resources)
    elif user_order == 'off':
        return 0
    else:
        print('Invalid input!')
    return cost, coffee


def ingredient_cost(coffee):
    if menu.resources['water'] - menu.MENU[coffee]['ingredients']['water'] >= 0:
        flag = True
        menu.resources['water'] -= menu.MENU[coffee]['ingredients']['water']
    else:
        print(f'Sorry there is not enough water.')
    if menu.resources['milk'] - menu.MENU[coffee]['ingredients']['milk'] >= 0:
        flag = True
        menu.resources['milk'] -= menu.MENU[coffee]['ingredients']['milk']
    else:
        print(f'Sorry there is not enough milk.')
    if menu.resources['coffee'] - menu.MENU[coffee]['ingredients']['coffee'] >= 0:
        flag = True
        menu.resources['coffee'] -= menu.MENU[coffee]['ingredients']['coffee']
    else:
        print(f'Sorry there is not enough milk.')
    return flag


def money():
    print("Please insert coins.")
    money_spent = 0
    quarter = input("how many quarters($0.25)? ")
    money_spent += int(quarter) * 0.25
    dime = input("how many dimes($0.10)? ")
    money_spent += int(dime) * 0.10
    nickle = input("how many nickles($0.05)? ")
    money_spent += int(nickle) * 0.05
    penny = input("how many pennies($0.01)? ")
    money_spent += int(penny) * 0.01
    return money_spent


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def compare_money(total_cost, money, coffee):
    if total_cost > money:
        print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Here is ${money - total_cost} in change.\nHere is your {coffee} ☕️. Enjoy!")


flag = True
while flag:
    result = order()
    total_cost, coffee = result

    money = money()
    compare_money(total_cost, money, coffee)
    flag = ingredient_cost(coffee)
    clear_console()
