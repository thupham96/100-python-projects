# Day 87: Breakout Game – Python Turtle Arcade Classic

This project is a modern recreation of the **Breakout** arcade game using **Python Turtle graphics**. The player controls a paddle to bounce a ball and break rows of bricks. The game tracks score, provides win/lose messages, and includes a clickable restart button for repeated playthroughs.

---

## Features

* Classic **Breakout-style gameplay**
* Real-time visual feedback and collision detection:

  * Paddle collision
  * Brick destruction
  * Wall bouncing
* Live tracking of:

  * **Score**
  * **Remaining bricks**
* Win condition when all bricks are cleared
* Game Over if the ball falls below the paddle
* Clickable **Restart** button to try again
* Smooth paddle movement with arrow keys

---

## Technologies Used

* **Python**
* **Turtle** – for game graphics and animation
* **event listeners** – for keyboard and mouse interactions
* **random** – imported for future use

---

## How to Run

1. Clone the repository or copy the code:

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day87_Breakout_Game
   ```

3. Run the application:

   ```bash
   python main.py
   ```

---

## Example Usage

1. Launch the game — a paddle, ball, and brick wall appear.
2. Use the **Left** and **Right** arrow keys to move the paddle.
3. The ball starts bouncing and destroys bricks on contact.
4. Keep the ball in play to break all bricks and win.
5. If the ball falls below the paddle, you lose.
6. Click the **Restart** button in the top right to play again.

---

## What I Learned

* Using the Turtle module to build animated arcade games.
* Controlling object motion and bounce mechanics.
* Detecting and managing collisions dynamically in a loop.
* Handling interactive input from both keyboard and mouse.
* Structuring a game loop with restart logic and state control.
