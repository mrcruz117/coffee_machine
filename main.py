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


def check_resources(choice):
    ingredients = MENU[choice]['ingredients']

    good_to_go = True
    for item in ingredients:
        if resources[item] - ingredients[item] < 0:
            good_to_go = False
    return good_to_go


def coffee_machine():
    print('Welcome to the Virtual Coffee Machine!\n')
    print(f'Resource Report:\nWater: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\n')

    # coffee_choice = (input('What kind of coffee would you like?\n(cappuccino/latte/espresso)\n')).lower()
    coffee_choice = 'latte'
    while coffee_choice != 'cappuccino' and coffee_choice != 'latte' and coffee_choice != 'espresso':
        coffee_choice = (input('Spelling Error: Please choose again\n(cappuccino/latte/espresso)\n')).lower()
    if not check_resources(coffee_choice):
        print("Out of resources! Please refill.")

    print(f"total cost: ${MENU[coffee_choice]['cost']}0")
    quarters = int(input("How many quarters?\n"))
    dimes = int(input("How many dimes?\n"))
    nickels = int(input("How many nickels?\n"))
    pennies = int(input("How many pennies?\n"))

    total = quarters * .25 + dimes * .1 + nickels * .05 + pennies * .01

    if total < MENU[coffee_choice]['cost']:
        print(f"Insufficient cash entered!\nYou entered ${total}\nTotal cost: ${MENU[coffee_choice]['cost']}")
        print(f"Please come try again with an extra ${MENU[coffee_choice]['cost'] - total}")
    else:
        print("Brrrrrrrrrrrr.... ding!\n\nHere is your drink enjoy!")


coffee_machine()

# TODO 1 print resource report
# TODO 2 make sure resources are sufficient
# TODO 3 process coins. quantity of each
# TODO 4 each coin number is an input. calc total.
# TODO 5 transaction successful?
# TODO 6 make coffee
