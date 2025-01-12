# Day 15: Coffee Machine  

Welcome to the Coffee Machine project! This Python program simulates a real-world coffee vending machine, allowing users to choose from a menu of popular drinks and interact with a virtual coffee machine. It's a fun way to practice programming concepts while creating a functional simulation.

---

## How It Works  

### Machine Setup:  

- The coffee machine offers three types of drinks: **espresso**, **latte**, and **cappuccino**.  
- It tracks resources such as water, milk, coffee, and money, and generates a status report upon request.  
- Users can interact with the machine through a text-based interface.

---

### User Interactions:  

1. **Choose a Drink**:  
   - The program prompts:  
     **`What would you like? (espresso/latte/cappuccino):`**  
   - Based on the user's choice, the machine checks resource availability and processes the transaction.

2. **Check Resources**:  
   - Enter **`report`** to display the machine's current resource levels, including water, milk, coffee, and money.

3. **Turn Off the Machine**:  
   - Enter **`off`** to shut down the program. This is intended for maintainers.

4. **Insert Coins**:  
   - If the machine has enough resources for the chosen drink, it prompts the user to insert coins.  
   - Coin values are as follows:  
     - Quarters = $0.25  
     - Dimes = $0.10  
     - Nickels = $0.05  
     - Pennies = $0.01  

---

### Program Features:  

1. **Resource Management**:  
   - The machine ensures there are enough ingredients before making a drink.  
   - Example: If latte requires 200ml of water but only 100ml is available, it displays:  
     **`Sorry there is not enough water.`**

2. **Transaction Handling**:  
   - If the user inserts insufficient funds, the machine refunds the money:  
     **`Sorry that's not enough money. Money refunded.`**  
   - If the user inserts too much money, the machine calculates and returns the change:  
     **`Here is $0.45 dollars in change.`**

3. **Drink Preparation**:  
   - After a successful transaction, the machine deducts the required ingredients from its resources and serves the drink:  
     **`Here is your latte. Enjoy!`**

---

## How to Play  

1. Clone the repository and navigate to the `Day15_CoffeeMachine` folder:  
   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd 100-python-projects/Day15_CoffeeMachine
   ```

2. Run the program:  
   ```bash
   python coffee_machine.py
   ```

3. Follow the on-screen prompts to order drinks, check resource reports, or turn off the machine.

---

## Example Run  

```plaintext
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is $0.50 dollars in change.
Here is your latte. Enjoy!

What would you like? (espresso/latte/cappuccino): report
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5

What would you like? (espresso/latte/cappuccino): off
Machine turning off. Goodbye!
```

---

## Technologies Used  

- Python 3  
- Conditional statements and loops  
- Dictionaries for storing data  
- Input handling and mathematical calculations  

---

## What I Learned  

- Implementing resource management and transaction validation.  
- Writing user-friendly prompts and interactive programs.  
- Managing and updating data dynamically.  
- Simulating real-world functionality in Python.  

Enjoy using the Coffee Machine program and customizing it to enhance its features! ☕
