**Day 19: Turtle Race Game**

Welcome to the **Turtle Race Game** project! This Python program uses Turtle graphics to simulate an exciting turtle race. With interactive elements like a countdown, a betting system, and a rematch option, it offers an engaging way to learn about GUI interactions, user input handling, and game loops.

---

### How It Works

**Project Setup:**
- The program employs the Turtle module to create and animate racing turtles on a graphical track.
- A countdown is displayed using Turtle graphics to build anticipation before the race starts.
- Users are prompted to bet on which turtle (by its color) will win the race.
- Turtles move forward by a random number of steps, creating an unpredictable race dynamic.
- The outcome is announced via a tkinter messagebox, and users are given the option to play another round.

**Program Features:**

- **Countdown:**  
  A countdown sequence is implemented to signal the start of the race. The countdown displays numbers from 3 to 1, followed by a "Go!" message to kick off the competition.

- **Betting System:**  
  Before the race begins, the user is asked to choose a turtle by its color. The input is validated to ensure the choice matches one of the predefined valid colors.

- **Race Simulation:**  
  Multiple turtles, each assigned a distinct color and starting position, race across the screen. Their movement is randomized to mimic the unpredictability of a real race.

- **Rematch Option:**  
  After a turtle wins the race, a messagebox informs the user of the result. The user is then prompted to decide whether to have a rematch, resetting the turtles and starting a new countdown if they choose to play again.

- **GUI Interaction:**  
  The integration of Turtle graphics for race visualization and tkinter for popup messages creates an interactive and dynamic gaming experience.

---

### How to Run the Program

1. **Clone the Repository & Navigate:**
   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd 100-python-projects/Day19_TurtleRaceGame
   ```

2. **Install Dependencies:**
   - Ensure you have Python 3 installed.
   - Tkinter is usually included with Python. If not, install it using your package manager.

3. **Run the Turtle Race Script:**
   ```bash
   python turtle_race.py
   ```

---

### Example Run

When you execute the script:
- A Turtle graphics window opens, displaying the race track and the turtles lined up at the start.
- A countdown appears in the center of the screen, counting from 3 to 1 and then displaying "Go!".
- The turtles race forward with randomized movements.
- When a turtle crosses the finish line, a popup message appears indicating whether your bet was correct.
- You are then asked if you want to have a rematch, and if you choose "yes," the turtles are reset and a new race begins.

---

### Technologies Used

- **Python 3**
- **Turtle Module:** For creating and animating the turtle graphics.
- **Tkinter:** For displaying popup messageboxes to inform the user of race results and handle rematch prompts.
- **Random Module:** To simulate unpredictable turtle movements.
- **Time Module:** For managing the countdown delays.

---

### What I Learned

- Implementing interactive game elements such as countdown timers and betting systems using Turtle graphics.
- Integrating different GUI modules (Turtle and Tkinter) to enhance user interaction.
- Creating a race simulation with randomized elements, reinforcing concepts like loops and conditionals.
- Handling user inputs effectively to manage game state transitions and rematches.

---

Enjoy the **Turtle Race Game** and feel free to experiment with different turtle colors, race speeds, or additional features to make the game even more exciting!
