```python
# Define the menu for the coffee machine with the required ingredients and costs
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

# Initialize resources available in the machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0.00  # Track total money earned
continue_running = True  # Set flag to control the main loop

# Start the main program loop
while continue_running:
    # Prompt the user for their choice
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    
    # If the user requests a report, display the current resources and money
    if user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    
    # If the user chooses to turn off the machine, end the loop
    elif user_choice == "off":
        continue_running = False
        print("Machine turning off. Goodbye!")
    
    # If the user selects a valid drink option, proceed with processing
    elif user_choice in MENU:
        # Get the required ingredients for the selected drink
        water_needed = MENU[user_choice]['ingredients']['water']
        coffee_needed = MENU[user_choice]['ingredients']['coffee']
        milk_needed = MENU[user_choice]['ingredients'].get('milk', 0)  # Default to 0 for espresso
        money_needed = MENU[user_choice]['cost']
        
        # Check if there are sufficient resources for the selected drink
        if water_needed > resources['water']:
            print("Sorry there is not enough water.")
        elif coffee_needed > resources['coffee']:
            print("Sorry there is not enough coffee.")
        elif milk_needed > resources['milk']:
            print("Sorry there is not enough milk.")
        else:
            # Prompt the user to insert coins
            print("Please insert coins.")
            quarters_count = int(input("How many quarters?: "))
            dimes_count = int(input("How many dimes?: "))
            nickles_count = int(input("How many nickles?: "))
            pennies_count = int(input("How many pennies?: "))
            
            # Calculate the total money inserted
            money_inserted = (
                0.25 * quarters_count +
                0.10 * dimes_count +
                0.05 * nickles_count +
                0.01 * pennies_count
            )
            
            # Check if the user inserted enough money
            if money_inserted < money_needed:
                print("Sorry that's not enough money. Money refunded.")
            else:
                # Deduct the cost of the drink, update resources, and calculate change
                money += money_needed
                change = round(money_inserted - money_needed, 2)
                resources['water'] -= water_needed
                resources['coffee'] -= coffee_needed
                resources['milk'] -= milk_needed
                print(f"Here is ${change} in change.")
                print(f"Here is your {user_choice} ☕️. Enjoy!")
    else:
        # Handle invalid input
        print("You have chosen an invalid option. Please choose again.")
    print("\n\n")  # Print a newline for better readability between interactions
```
