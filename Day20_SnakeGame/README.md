# Day 20: Snake Game with Obstacles  

Welcome to the **Snake Game with Obstacles** project! This Python program is an enhanced version of the classic Snake game, built using Python's **Turtle graphics** module. It includes features like food collection, an increasing score, dynamic speed adjustment, and randomly placed obstacles that make the game more challenging.  

---

## How It Works  

### Game Setup:  

- **Screen Initialization**:  
  - The game window is set to **600x600 pixels** with a black background.  
  - The **automatic screen update** is turned off for smoother animations.  

- **Object Creation**:  
  - **Snake**: The player controls a snake that moves in four directions.  
  - **Food**: The snake must eat food to grow and increase its score.  
  - **Scoreboard**: Tracks the player’s score and displays game-over messages.  
  - **Obstacles**: Randomly placed obstacles add difficulty by blocking paths.  

---

### Gameplay Mechanics  

1. **Snake Movement**:  
   - The snake moves forward continuously and responds to **arrow key inputs**.  

2. **Food Consumption**:  
   - When the snake eats food, it **grows in length**, the **score increases**, and the **speed gradually increases** to make the game more challenging.  

3. **Obstacle Avoidance**:  
   - The game randomly places obstacles on the screen.  
   - If the snake **collides with an obstacle**, the game ends.  

4. **Game Over Conditions**:  
   - The game ends when the snake **hits the wall**, **collides with itself**, or **crashes into an obstacle**.  
   - A "Game Over" message is displayed when any of these conditions are met.  

---

## Program Design  

### Functional Components  

- **`Snake` Class**:  
  - Controls the movement, growth, and direction changes of the snake.  

- **`Food` Class**:  
  - Generates food at random locations.  
  - Refreshes food when the snake eats it.  

- **`Scoreboard` Class**:  
  - Tracks and updates the score.  
  - Displays a **"Game Over"** message when the game ends.  

- **`Obstacle` Class**:  
  - Generates random obstacles on the screen.  
  - Causes a game over if the snake collides with an obstacle.  

- **Keyboard Event Handling**:  
  - **Arrow keys (`Up`, `Down`, `Left`, `Right`)** allow the player to control the snake.  

---

## User Interactions  

1. **Start the Game**  
   - The game begins as soon as the program is run.  

2. **Control the Snake**  
   - Use **arrow keys** to move the snake in different directions.  

3. **Eat Food & Score Points**  
   - Each time the snake eats food, it grows, and the score increases.  
   - The game speeds up slightly, making it progressively harder.  

4. **Avoid Walls, Yourself, and Obstacles**  
   - If the snake **hits a wall**, **collides with itself**, or **touches an obstacle**, the game ends.  

5. **Game Over & Restart**  
   - A **"Game Over"** message is displayed upon losing.  
   - The player can **restart the game manually** by running the script again.  

---

## How to Run  

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/thupham96/100-python-projects.git  
   cd 100-python-projects/Day20_SnakeGame
   ```  

2. **Run the Program**:  
   ```bash
   python snakegame.py
   ```  

3. **Control the Snake Using Arrow Keys**  
   - Move **Up**, **Down**, **Left**, or **Right** to navigate the snake.  

---

## Example Run  

```plaintext
Welcome to the Snake Game!  

(Use arrow keys to move the snake...)  
* The snake eats food and grows.  
* Score increases: 10 → 20 → 30...  
* Speed increases as the score gets higher.  
* A randomly placed obstacle appears on the screen.  
* Collision detected! GAME OVER  
```  

---

## Technologies Used  

- **Python 3**  
- **Turtle Graphics**: For snake movement, food, obstacles, and screen rendering.  
- **Random Module**: To generate food and obstacle placements.  
- **Time Module**: For handling game speed and smooth animations.  

---

## What I Learned  

- **Object-Oriented Programming (OOP)**:  
  - Implementing classes like `Snake`, `Food`, `Scoreboard`, and `Obstacle` for modular game design.  

- **Game Logic & Collision Detection**:  
  - Handling **wall collisions**, **self-collisions**, and **obstacle interactions**.  

- **Dynamic Game Speed**:  
  - Adjusting game difficulty by **increasing movement speed** after consuming food.  

- **User Input Handling**:  
  - Using `screen.listen()` and `screen.onkey()` for real-time player controls.  

Enjoy the challenge, and see how long you can survive in this **Snake Game with Obstacles**! 🐍🎮
