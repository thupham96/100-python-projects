# Day 16: Coffee Machine with OOP

Welcome to the Coffee Machine project! This Python program simulates a real-world coffee vending machine, now enhanced with **Object-Oriented Programming (OOP)** principles. This refactored version introduces a structured and modular approach to simulate a coffee machine, making the code more reusable, scalable, and maintainable.

---

## How It Works

### Machine Setup:

- The coffee machine offers three types of drinks: **espresso**, **latte**, and **cappuccino**.
- It tracks resources such as water, milk, coffee, and money through dedicated classes.
- Users interact with the machine through a text-based interface, and each operation is handled via specific methods within the program's classes.

---

### Program Design with OOP:

1. **Classes and Responsibilities**:
   - **`Menu`**: Maintains the list of available drinks and their resource requirements.
   - **`CoffeeMaker`**: Manages resources and checks ingredient availability.
   - **`MoneyMachine`**: Handles monetary transactions, including validating payments and providing change.
   - **`CoffeeMachine`**: Coordinates interactions between classes and manages the main user interface.

2. **Encapsulation**:
   - Resources, recipes, and machine operations are encapsulated within their respective classes, providing clear boundaries and responsibilities.

3. **Reusability**:
   - Each class is reusable and can be extended or modified independently for additional features.

---

### User Interactions:

1. **Choose a Drink**:
   - The program prompts:
     **`What would you like? (espresso/latte/cappuccino):`**
   - The machine verifies resource availability before proceeding.

2. **Check Resources**:
   - Enter **`report`** to display the machine's current resource levels, including water, milk, coffee, and money.

3. **Turn Off the Machine**:
   - Enter **`off`** to shut down the program, intended for maintainers.

4. **Insert Coins**:
   - If resources are sufficient for the selected drink, the machine requests coin input to complete the transaction.

---

### Key Features:

1. **Resource Management**:
   - Tracks resource usage and ensures sufficient ingredients are available for selected drinks.

2. **Transaction Handling**:
   - Validates user payments, calculates and provides change, and maintains a record of earnings.

3. **Scalable Menu System**:
   - The menu can easily accommodate new drinks by modifying the `Menu` class.

4. **Error Handling**:
   - Displays appropriate error messages for insufficient resources or incorrect monetary input.

---

## How to Run

1. Clone the repository and navigate to the `Day16_CoffeeMachine_OOP` folder:
   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd 100-python-projects/Day16_CoffeeMachine_OOP
   ```

2. Run the program:
   ```bash
   python coffee_machine_oop.py
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
- Object-Oriented Programming (OOP)
- Classes and methods for modular design
- Dictionaries for data storage and resource management
- Input handling and mathematical calculations

---

## What I Learned

- Applying OOP principles to refactor procedural code.
- Designing modular and reusable components for real-world simulations.
- Encapsulating data and behavior within classes for better program structure.
- Enhancing maintainability and scalability of a project using OOP.

Enjoy using the Coffee Machine with OOP and customizing it to add even more exciting features! 🍵


