# Day 19: Turtle Race Game

Welcome to the Turtle Race Game project! This Python program simulates an exciting race between colorful turtles using Python's Turtle graphics. With an interactive betting system and a fun countdown before the race begins, this project demonstrates how to create engaging, event-driven applications using modular functions and procedural programming.

---

## How It Works

### Game Setup:

- **Turtle Initialization**: The game creates several turtles, each with a unique color.
- **Starting Positions**: Turtles are positioned at fixed y-coordinates on the left side of the screen.
- **User Bet**: Before the race starts, the player is prompted to bet on which turtle (by color) they think will win.

---

### Race Execution:

1. **Countdown**:
   - A visual countdown (from 3 to 1, then "Go!") is displayed using the Turtle module.
   - This builds anticipation and signals the start of the race.

2. **The Race**:
   - Each turtle moves forward by a random distance in each iteration of the race loop.
   - The race continues until one turtle crosses the finish line (an x-coordinate threshold).

3. **Result Announcement**:
   - When a turtle wins, a popup message (via `tkinter.messagebox`) informs the player whether their bet was correct.
   - The winning turtle's color is displayed in the message.

4. **Rematch Option**:
   - After a race concludes, the player is given the option to have a rematch.
   - If chosen, turtles are reset to their starting positions and the race begins anew after another countdown.

---

## Program Design

### Functional Components:

- **`countdown()`**:
  - Displays a countdown sequence on the screen using a hidden turtle.
  - Uses a loop with a delay (`time.sleep()`) to show numbers and "Go!".

- **`get_user_bet(valid_colors)`**:
  - Prompts the user to input their bet based on the provided valid colors.
  - Validates the input, ensuring it matches one of the allowed colors.

- **`get_rematch_input()`**:
  - Asks the player if they want a rematch after the race.
  - Validates the input to accept only "y" or "n".

- **Main Race Loop**:
  - Iterates over all turtle objects, moving each by a random distance.
  - Checks for a winning turtle and triggers the end-of-race sequence with result display and rematch handling.

### Modularity & Encapsulation:

- **Separation of Concerns**:
  - Each function handles a distinct part of the game logic (countdown, input handling, race execution).
  - This modular design enhances code readability and makes future modifications or extensions straightforward.

- **Use of Standard Libraries**:
  - **Turtle**: For graphics and race visualization.
  - **tkinter.messagebox**: For user-friendly popup messages.
  - **Random & Time**: For simulating unpredictable movement and managing countdown timing.

---

## User Interactions

1. **Place a Bet**:
   - The game begins by asking, “Which turtle will win the race? Enter a color from: red, green, blue, black, orange, pink.”
   - Only valid color choices are accepted.

2. **Watch the Countdown**:
   - A countdown from 3 to 1 is displayed, building excitement before the race starts.

3. **Enjoy the Race**:
   - Turtles race across the screen with random forward movements.
   - The player watches the race unfold in real time.

4. **Receive the Result**:
   - Once a turtle wins, a popup message informs the player if their bet was correct.

5. **Rematch Option**:
   - After the race, the player can choose to play again or exit the game.

---

## How to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd 100-python-projects/Day19_TurtleRaceGame
   ```

2. **Run the Program**:
   ```bash
   python turtleracegame.py
   ```

3. **Follow On-Screen Prompts**:
   - Place your bet, watch the countdown, enjoy the race, and decide if you’d like a rematch!

---

## Example Run

```plaintext
Welcome to the Turtle Race Game!

Which turtle will win the race? Enter a color from: red, green, blue, black, orange, pink: red
(Countdown appears on the screen: 3, 2, 1, Go!)
Turtles race across the screen...
Popup Message: "You've won. The red turtle is the winner!" 
OR
Popup Message: "You've lost. The blue turtle is the winner!"
Do you want a rematch? (y/n): y
```

---

## Technologies Used

- **Python 3**
- **Turtle Graphics**: For visual race simulation.
- **tkinter**: To display interactive popup messages.
- **Random Module**: To simulate varying race progress.
- **Time Module**: For countdown timing and pauses.

---

## What I Learned

- **Interactive Graphics**: Utilizing the Turtle module for creating engaging visual simulations.
- **Modular Programming**: Breaking down the game logic into clear, reusable functions.
- **User Input Handling**: Validating and processing user inputs effectively.
- **Event-Driven Programming**: Managing game flow with loops, conditionals, and timely user feedback.

Enjoy the race, and may your chosen turtle always cross the finish line first! 🏁
