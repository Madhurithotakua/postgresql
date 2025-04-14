import psycopg2
from psycopg2 import sql

MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 20.00,
    },
    "filtercoffee": {
        "ingredients": {"water": 200, "coffee": 24, "milk": 150},
        "cost": 15.00,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "coffee": 24, "milk": 100},
        "cost": 25.00,
    }
}

resources = {
    "water": 500,
    "milk": 300,
    "coffee": 100,
}

money = 0

# Database connection setup
def connect_db():
    conn = psycopg2.connect(
        host="localhost",
        database="madhuri",
        user="postgres",
        password="bunny",
        port="5432"
    )
    return conn

# Insert sale record into the database
def insert_sale(coffee_type, change, income):
    conn = connect_db()
    cur = conn.cursor()
    insert_query = sql.SQL("""
        INSERT INTO coffee_sales (coffee_type, change_given, income)
        VALUES (%s, %s, %s)
    """)
    cur.execute(insert_query, (coffee_type, change, income))
    conn.commit()
    cur.close()
    conn.close()

# Insert report record into the database
def insert_report():
    conn = connect_db()
    cur = conn.cursor()
    insert_query = sql.SQL("""
        INSERT INTO coffee_report (water_remaining, milk_remaining, coffee_remaining, total_income)
        VALUES (%s, %s, %s, %s)
    """)
    cur.execute(insert_query, (
        resources["water"],
        resources["milk"],
        resources["coffee"],
        money
    ))
    conn.commit()
    cur.close()
    conn.close()

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    total = int(input("Enter the number of 1 Rupee Notes: ")) * 1
    total += int(input("Enter the number of 2 Rupee Notes: ")) * 2
    total += int(input("Enter the number of 5 Rupee Notes: ")) * 5
    total += int(input("Enter the number of 10 Rupee Notes: ")) * 10
    total += int(input("Enter the number of 20 Rupee Notes: ")) * 20
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is {change} in change.")
        global money
        money += drink_cost
        return True, change
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False, 0

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

def coffee_machine():
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/filtercoffee/cappuccino): ")
        if choice == "off":
            is_on = False
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: {money}")
            insert_report()  # Save report data to the database
        elif choice in MENU:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                successful, change = is_transaction_successful(payment, drink["cost"])
                if successful:
                    make_coffee(choice, drink["ingredients"])
                    insert_sale(choice, change, drink["cost"])

coffee_machine()
