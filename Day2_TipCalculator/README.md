# Day 2: Tip Calculator

Welcome to the Tip Calculator! This interactive tool helps you easily calculate and split restaurant bills, including custom tips. Quickly determine how much each person should pay, whether splitting evenly or individually based on contributions.

Click here to play the demo

## How It Works

### Step-by-Step Guide:

1. **Enter Bill Amount**:
   - Provide the total bill amount (e.g., `$120.50`).

2. **Select Tip Percentage**:
   - Enter a custom tip percentage (e.g., `15` or `18.5`).

3. **Number of People Paying**:
   - Specify how many people will split the bill.

4. **Splitting Options**:
   - If one person pays, the total amount (bill + tip) is displayed immediately.
   - For multiple people, you can choose:
     - **Even Split**: The bill and tip are divided equally among all.
     - **Uneven Split**: Each person enters their individual contribution, and tips are distributed proportionally.

### Example Run:
```plaintext
What was the total bill? $100
What percentage tip would you like to give? (e.g., 10, 12.5, 15): 15
How many people are paying? 3
Would you like to split the bill evenly? (yes/no): yes

Final breakdown (even split):
Person 1: Base = $33.33, Tip = $5.00, Total = $38.33
Person 2: Base = $33.33, Tip = $5.00, Total = $38.33
Person 3: Base = $33.33, Tip = $5.00, Total = $38.33

Thank you for using the Tip Calculator! 😊
```

## Features

- **Custom Tip Percentages**: Flexible options for calculating gratuities.
- **Dynamic Splitting**: Even or proportional division of bills.
- **Error Handling**: Ensures valid numeric inputs and accurate totals.

## How to Use

1. Clone the repository and navigate to the `Day2_TipCalculator` folder:
   ```bash
   git clone https://github.com/yourusername/100-python-projects.git
   cd 100-python-projects/Day2_TipCalculator
   ```

2. Run the script:
   ```bash
   python tip_calculator.py
   ```

3. Follow the on-screen prompts to calculate your tip and split the bill accordingly!

## Technologies Used

- Python 3
- Robust error checking with exception handling

## What I Learned

- Handling user input and data validation.
- Implementing conditional logic for various use cases.
- Managing floating-point arithmetic for financial calculations.

Enjoy using the Tip Calculator to simplify your dining experience! 💸🍽️

