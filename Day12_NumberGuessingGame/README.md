# Day 12: Number Guessing Game

Welcome to the Number Guessing Game! This project is a simple yet engaging Python game that tests your guessing skills. The program challenges you to guess a number between 1 and 100, with helpful feedback provided after each guess.

---

## How It Works

1. **Game Setup**:
   - The program generates a random number between 1 and 100 (inclusive).
   - You are asked to choose a difficulty level:
     - **Easy**: You get 10 attempts.
     - **Hard**: You get 5 attempts.

2. **Gameplay**:
   - On each turn, you guess a number.
   - The program provides feedback:
     - "Too high!" if your guess is higher than the target number.
     - "Too low!" if your guess is lower than the target number.
   - The game continues until:
     - You guess the correct number.
     - You run out of attempts.

3. **End of Game**:
   - If you guess correctly, the program congratulates you.
   - If you run out of attempts, the program reveals the target number.

---

## Features

- Random number generation for an unpredictable experience.
- Two difficulty levels for varied challenge levels.
- User-friendly feedback to guide your guesses.

---

## How to Play

1. Clone the repository and navigate to the `Day11_NumberGuessingGame` folder:
   ```bash
   git clone https://github.com/yourusername/100-python-projects.git
   cd 100-python-projects/Day12_NumberGuessingGame
   ```

2. Run the game script:
   ```bash
   python number_guessing_game.py
   ```

3. Follow the on-screen instructions to choose a difficulty level and start guessing!

---

## Example Run

```text
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts remaining to guess the number.
Make a guess: 50
Too low.
You have 9 attempts remaining to guess the number.
Make a guess: 75
Too high.
You have 8 attempts remaining to guess the number.
Make a guess: 62
You got it! The answer was 62.
```

---

## Technologies Used

- Python 3
- Random module

---

## What I Learned

- Generating random numbers in Python using the `random` module.
- Implementing conditional logic for user feedback.
- Managing game states and player attempts.

---

Enjoy the game, and happy guessing!


