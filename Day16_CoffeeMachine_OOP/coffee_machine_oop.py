from menu import Menu, MenuItem  # Import Menu and MenuItem classes
from coffee_maker import CoffeeMaker  # Import CoffeeMaker class
from money_machine import MoneyMachine  # Import MoneyMachine class

# Initialize the machine and its components
machine_is_on = True  # Variable to control the main loop
coffee_machine = CoffeeMaker()  # Create an instance of CoffeeMaker
menu = Menu()  # Create an instance of Menu
money_machine = MoneyMachine()  # Create an instance of MoneyMachine

# Main loop to keep the machine running
while machine_is_on:
    # Prompt user for their choice of drink or command
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice=="off":  # Check if the user wants to turn off the machine
        machine_is_on = False
        print("Machine turning off. Goodbye!")  # Notify the user
    elif user_choice=="report":  # Check if the user wants a status report
        coffee_machine.report()  # Display resources status
        money_machine.report()  # Display money status
    else:
        # Try to find the drink in the menu
        selected_drink = next((item for item in menu.menu if item.name.lower()==user_choice), None)
        if selected_drink:
            # Check if resources are sufficient for the selected drink
            if coffee_machine.is_resource_sufficient(selected_drink):
                # Attempt to process payment
                if money_machine.make_payment(selected_drink.cost):
                    # Make the coffee if payment is successful
                    coffee_machine.make_coffee(selected_drink)
        else:
            # Inform the user if the drink is not on the menu
            print(f"Sorry, {user_choice} is not on the menu.")
