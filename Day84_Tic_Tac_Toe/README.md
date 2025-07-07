# Day 84: Tic-Tac-Toe – Console Game in Python

This project implements a classic **Tic-Tac-Toe** game that runs in the terminal. Two players take turns marking spaces in a 3×3 grid. The first to align three symbols horizontally, vertically, or diagonally wins. If all spaces are filled without a winner, the game ends in a tie.

---

## Project Features

* Two-player game with alternating turns.
* Intuitive console board display using number hints.
* Validates user input and prevents invalid or duplicate moves.
* Detects win or tie conditions with clear messages.
* Option to replay the game without restarting the script.

---

## Technologies Used

* **Python** — for game logic and input/output
* **Standard I/O** — for interaction via the console

---

## How to Run

1. Clone the repository and navigate to the project directory:

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day84_Tic_Tac_Toe
   ```

2. Run the game:

   ```bash
   python tic_tac_toe.py
   ```

---

## Example Gameplay

```
Welcome to Tic-Tac-Toe!

 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 

Play X, please choose 1 number from 1-9 for the next move: 5
Play O, please choose 1 number from 1-9 for the next move: 1
...

🎉 Player X wins the match!
Would you like to play another game? (y/n)
```

---

## What I Learned

* How to manage and update a game board using lists.
* Techniques for detecting win and tie conditions with pattern checking.
* Implementing game loops and managing turn-based player logic.
* Building a replayable CLI game using basic Python.
