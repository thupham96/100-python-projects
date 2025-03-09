# Day 24: U.S. States Game

Welcome to the **U.S. States Game** project! This interactive Python project uses the **Turtle graphics** module and **Pandas** to create an engaging educational experience where players attempt to name all 50 U.S. states by entering their names, with visual feedback provided directly on a U.S. map.

---

## How It Works

### Game Setup

- **Screen Initialization**:
  - The game window displays an image of a blank map of the U.S. states.
  - Players type state names into pop-up text boxes.

- **Data Loading**:
  - Loads coordinates for each state from a CSV file (`50_states.csv`).

- **Progress Saving & Loading**:
  - Automatically saves the player's progress to continue later.

---

### Gameplay Mechanics

1. **User Interaction**:
   - Players input the names of U.S. states into a prompt.
   - Correct answers are written directly onto the map at the correct locations.

2. **Incorrect Guesses**:
   - Players have a limited number of incorrect guesses (default: 5).
   - Incorrect guesses reduce the remaining attempts.

3. **Game Progression**:
   - Guessed states are saved and visually displayed on the map.
   - Players can continue previous games or start fresh.

4. **Game Completion & Exit**:
   - Game ends when all 50 states are guessed correctly or the player exhausts all incorrect guesses.
   - Player can exit anytime by typing "exit," and progress will be saved automatically.

---

## Program Design

### Functional Components

- **Turtle Graphics**:
  - Visual display and interactive window.
  - Displays correct guesses directly onto the map.

- **Pandas**:
  - Efficiently manages and processes state data from CSV files.

- **Data Persistence**:
  - Progress saving/loading functionality (`guessed_states.csv`).

- **Interactive Text Prompts**:
  - Players provide inputs through pop-up prompts.

---

## User Interactions

1. **Starting a New or Continuing Game**:
   - Prompt to continue from previous progress or start new.

2. **Guessing States**:
   - Player inputs state names; correct guesses appear on the map.

3. **Handling Incorrect Answers**:
   - Limited incorrect guesses before revealing missed states.

4. **Game Over Scenario**:
   - Missed states are displayed when incorrect guesses run out.

5. **Exit and Save Progress**:
   - Typing "exit" saves the current progress and exits the game.

---

## How to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd 100-python-projects/Day24_USStatesGame
   ```

2. **Run the Program**:
   ```bash
   python us_states_game.py
   ```

3. **Play the Game**:
   - Type state names in the pop-up window.
   - Guess all states correctly or use "exit" to save progress.

---

## Example Run

```plaintext
Welcome to the U.S. States Game!

* 0/50 States Correct
* Player types "Texas"
* "Texas" is marked on the map.
* Incorrect guesses left: 5
* Player continues guessing...
* Types "exit" → progress saved!
```

---

## Technologies Used

- **Python 3**
- **Turtle Graphics**: Visualization and user interface.
- **Pandas**: CSV data handling and state coordinates.
- **CSV Data Files**: `50_states.csv` (coordinates), `guessed_states.csv` (saved progress).

---

## What I Learned

- **Interactive Data Visualization**:
  - Displaying dynamic data on graphical maps using Turtle.

- **Data Management**:
  - Reading and writing CSV data with Pandas.

- **Game Logic & State Management**:
  - Managing user inputs, saving/loading game states, and implementing gameplay rules.

Challenge yourself in **U.S. States Game** and test your geographic knowledge! 🌎🇺🇸

