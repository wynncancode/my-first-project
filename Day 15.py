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


# TODO: 1. Print report of all coffee machine resources


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


# TODO: 2. Ask customer for order, user for input


def ask_order():
    cus_order = input("What would you like? (espresso/latte/capppucino): ")
    return cus_order


# TODO: 3. Check resources


def check_resources(drink):
    if resources["water"] < MENU[drink]["ingredients"]["water"]:
        print("Sorry, there is not enough water.")
    elif drink != "espresso" and resources["milk"] < MENU[drink]["ingredients"]["milk"]:
        print("Sorry, there is not enough milk.")
    elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        print("Sorry, there is not enough coffee.")
    else:
        return True


# TODO: 4. Ask customer to insert coins


def ask_payment():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total


# TODO: 5. Check payment is sufficient.


def check_payment(order, payment):
    if payment < MENU[order]["cost"]:
        print("Sorry, that's not enough. Money refunded.")
        return False
    elif payment > MENU[order]["cost"]:
        change = round(payment - MENU[order]["cost"],2)
        print(f"Here is ${change} in change.")
        return True
    else:
        return True


# TODO: 6. Keep track of sales and resources left


def update_report(order):

    resources["water"] = resources["water"] - MENU[order]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - MENU[order]["ingredients"]["coffee"]
    if order != "espresso":
        resources["milk"] = resources["milk"] - MENU[order]["ingredients"]["milk"]


# TODO 7: Launch coffee machine.

order = ""
money = 0.0

while order != "off":
    order = ask_order()
    if order == "off":
        break
    elif order == "report":
        print_report()
    else:
        if check_resources(order):
            payment = ask_payment()
            if check_payment(order,payment):
                profit = round(payment - MENU[order]["cost"],2)
                money += profit
                update_report(order)
                print(f"Here's your {order}. Enjoy!")

