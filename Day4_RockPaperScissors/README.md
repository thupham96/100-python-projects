# Day 4: Rock Paper Scissors Game ✊📄✂️

Welcome to the **Rock Paper Scissors Game**! This classic hand game is brought to life in Python with a best-of-N rounds format, ASCII graphics, input validation, and real-time score tracking. A fun way to practice game logic and user interaction in a console environment!

## How It Works

1. **Choose Rounds**: Player selects how many rounds to play (Best of N).
2. **Play Turns**: In each round, the player chooses Rock (0), Paper (1), or Scissors (2).
3. **Game Logic**: The computer randomly chooses its move, and the winner of the round is determined.
4. **Track Score**: Scores are updated and displayed after every round.
5. **Decide Winner**: Once all rounds are played, a final winner is declared.
6. **Replay Option**: Player can choose to replay the game.

## Example Run

```
🎮 Starting Best of 3 — First to 2 wins!

--- Round 1 ---
Type 0 for Rock, 1 for Paper or 2 for Scissors: 0

You chose:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Computer chose:
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

Computer wins this round!
Score: You 0 - 1 Computer
```

## Features

- **Best-of-N Format**: Game continues until one player reaches the majority win count.
- **ASCII Art Visuals**: Fun visual representation of Rock, Paper, and Scissors.
- **Score Tracking**: Updates and displays current scores after every round.
- **Input Handling**: Gracefully handles invalid inputs and penalizes accordingly.
- **Replay Option**: Replay without restarting the program.

## How to Use

1. Clone or download the project:
   ```bash
   git clone https://github.com/thupham96/python-projects.git
   cd Day4_RockPaperScissors
   ```

2. Run the script:
   ```bash
   python rock_paper_scissors.py
   ```

3. Follow the prompts in the terminal to play rounds against the computer.

## Technologies Used

- Python 3
- `random` module for computer choice
- ASCII art for UI enhancement

## What I Learned

- Implementing game logic and conditional structures.
- Creating loops for replayability and round control.
- Using ASCII art to enhance terminal-based UI.
- Handling user input robustly and dealing with edge cases.
- Structuring console games for readability and fun.

A fun little battle of luck and logic—play the **Rock Paper Scissors Game** and challenge your computer opponent! 🕹️
