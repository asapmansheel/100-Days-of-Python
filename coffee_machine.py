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

def resources_sufficient(drink):
    ingredients = MENU[drink]['ingredients']
    for item in ingredients :
        if ingredients[item] > resources[item]:
            print(f'Sorry there is not enough {item}.')
            return False
    
    return True

def process_coins(quarters, dimes, nickles, pennies, drink):
    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return total

def transaction_successful(payment,drink):
    if payment < MENU[drink]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = payment - MENU[drink]['cost']
        print('Here is ${:.2f} in change.'.format(change) )
        print(f'Here is your {drink}. Enjoy!')
        return True

def make_coffee(drink):
    ingredients = MENU[drink]['ingredients']
    for item in ingredients:
        resources[item] -= ingredients[item]

profit = 0
turn_on = True

while turn_on:
    user_response = input('What would you like? (espresso/latte/cappuccino): ').lower()

    if user_response == 'off':
        turn_on = False

    elif user_response == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${profit}')

    elif user_response == 'espresso' or user_response == 'latte' or user_response == 'cappuccino':
        if resources_sufficient(user_response) == True:
            print('Please insert coins.')
            quarters = int(input('How many quarters?: '))
            dimes = int(input('How many dimes?: '))
            nickles = int(input('How many nickles?: '))
            pennies = int(input('How many pennies?: '))

            payment = process_coins(quarters, dimes, nickles, pennies,user_response)

            if transaction_successful(payment,user_response):
                profit += MENU[user_response]['cost']
                make_coffee(user_response)
