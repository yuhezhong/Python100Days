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


def money():
    print("Please insert coins.")
    money_spent = 0
    quarter = input("how many quarters? ")
    money_spent += int(quarter) * 0.25
    dime = input("how many dimes? ")
    money_spent += int(dime) * 0.10
    nickle = input("how many nickles? ")
    money_spent += int(nickle) * 0.05
    penny = input("how many pennies? ")
    money_spent += int(penny) * 0.01
    return money_spent


def compare_money(total_cost, money, coffee):
    if total_cost > money:
        print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Here is ${money - total_cost} in change.\nHere is your {coffee} ☕️. Enjoy!")


result = order()
total_cost, coffee = result

money = money()
compare_money(total_cost, money, coffee)
