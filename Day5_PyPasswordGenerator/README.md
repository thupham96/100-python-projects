# Day 5: PyPassword Generator

Welcome to the **PyPassword Generator!**
This interactive Python script helps you create strong, secure, and randomized passwords by combining **letters, numbers, and symbols**. It ensures flexibility while enforcing password strength with length validation.

---

## How It Works

### Step-by-Step Guide:

1. **Enter Password Requirements**

   * Choose how many **letters**, **symbols**, and **numbers** you’d like.

2. **Validation Rules**

   * Password must be **at least 6 characters**.
   * Password cannot exceed **50 characters**.
   * If invalid, you’ll be prompted to re-enter values.

3. **Password Generation**

   * The script randomly selects characters from each pool.
   * All characters are shuffled to maximize randomness.
   * Final password is displayed.

---

### Example Run

```plaintext
Welcome to the PyPassword Generator!
How many letters would you like in your password?
> 5
How many symbols would you like?
> 2
How many numbers would you like?
> 3

Your password is: zE3!a6q%1K
```

---

## Features

* **Customizable** — Choose the number of letters, symbols, and numbers.
* **Validation** — Enforces secure length between 6–50 characters.
* **Randomized Shuffle** — Prevents predictable character order.
* **Error Handling** — Keeps prompting until valid inputs are provided.

---

## 🛠️ How to Use

1. Clone the repository and navigate to the `Day5_PyPasswordGenerator` folder:

   ```bash
   git clone https://github.com/yourusername/100-python-projects.git
   cd 100-python-projects/Day5_PyPasswordGenerator
   ```

2. Run the script:

   ```bash
   python password_generator.py
   ```

3. Follow the prompts to generate your secure password!

---

## Technologies Used

* Python 3
* `random` module for randomness
* Basic input validation

---

## What I Learned

* Using **Python lists** to store and manage character sets.
* Applying **random.choices()** and **random.sample()** for random generation and shuffling.
* Adding **validation logic** to ensure strong and practical passwords.
* Handling user input gracefully with loops and error messages.

---

Enjoy creating secure passwords with **PyPassword Generator!**
