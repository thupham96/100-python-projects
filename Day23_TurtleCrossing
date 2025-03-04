# Day 23: Turtle Crossing Game  

Welcome to the **Turtle Crossing Game** project! This Python game is inspired by the classic arcade-style **Frogger**, built using the **Turtle graphics** module. Players control a turtle as it navigates a busy road, avoiding moving cars, collecting power-ups, and progressing through levels.  

---

## How It Works  

### Game Setup  

- **Screen Initialization**:  
  - The game window is set to **600x600 pixels** with a title “Turtle Crossing Game.”  
  - The **automatic screen update** is turned off for smooth animations.  
  - The game listens for **keyboard inputs** to control the turtle.  

- **Game Objects**:  
  - **Player (`player`)**: A turtle that moves in four directions (`Up`, `Down`, `Left`, `Right`).  
  - **Car Manager (`car_manager`)**: Generates and moves cars across the screen at increasing speeds.  
  - **Scoreboard (`scoreboard`)**: Tracks levels and displays a game-over message when the player collides with a car.  
  - **Power-Up (`powerup`)**: Appears occasionally and provides a **temporary speed boost** when collected.  

---

### Gameplay Mechanics  

1. **Player Movement**:  
   - The turtle moves **up, down, left, and right** using arrow keys.  
   - The goal is to **reach the top of the screen** to progress to the next level.  

2. **Car Spawning & Movement**:  
   - Cars randomly appear and move from **right to left**.  
   - The speed of the cars **increases with each level**.  

3. **Collision Detection**:  
   - If the turtle **touches a car**, the game ends, displaying a “Game Over” message.  
   - If the turtle **reaches the top of the screen**, the level increases, cars get faster, and the turtle resets to the starting position.  

4. **Power-Up Mechanic**:  
   - A **power-up** appears every few loops.  
   - If the player collects it, they receive a **speed boost** for a limited time (5 seconds).  
   - After the effect expires, the player’s speed returns to normal.  

5. **Level Progression & Increasing Difficulty**:  
   - Each time the turtle **reaches the top**, the level increases.  
   - Car speed gradually increases, making the game more challenging.  

---

## Program Design  

### Functional Components  

- **`Player` Class**:  
  - Manages movement and detects when the turtle reaches the finish line.  

- **`CarManager` Class**:  
  - Generates and moves cars across the screen.  
  - Increases speed as levels progress.  

- **`Scoreboard` Class**:  
  - Displays the current level.  
  - Shows a "Game Over" message when the player loses.  

- **`PowerUp` Class**:  
  - Spawns power-ups at random times.  
  - Grants a **temporary speed boost** when collected.  

- **Keyboard Event Handling**:  
  - **Arrow keys (`Up`, `Down`, `Left`, `Right`)** move the turtle.  

---

## User Interactions  

1. **Start the Game**  
   - The turtle starts at the **bottom of the screen**.  
   - The player moves the turtle towards the top, avoiding cars.  

2. **Avoid Cars**  
   - Cars randomly appear and **move across the screen**.  
   - If the turtle **collides with a car**, the game ends.  

3. **Collect Power-Ups**  
   - Power-ups **appear occasionally**.  
   - If the player **touches a power-up**, they gain **temporary speed boost**.  

4. **Level Up & Increase Difficulty**  
   - When the turtle **reaches the top**, the level increases.  
   - Cars move **faster** as the game progresses.  

5. **Game Over**  
   - If the player collides with a car, the game ends.  
   - The final level is displayed before closing the game.  

---

## How to Run  

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/thupham96/100-python-projects.git  
   cd 100-python-projects/Day23_TurtleCrossing
   ```  

2. **Run the Program**:  
   ```bash
   python turtle_crossing.py
   ```  

3. **Control the Turtle & Play**  
   - Use **arrow keys** to move.  
   - Avoid **cars** and collect **power-ups**.  
   - Reach the top to **level up**!  

---

## Example Run  

```plaintext
Welcome to Turtle Crossing!  

* Level 1  
* Cars start appearing...  
* The turtle moves across the screen  
* A power-up appears!  
* Player collects the power-up → Speed boost activated!  
* The turtle reaches the finish line → Level Up!  
* Cars move faster...  
* Press "X" to exit the game.  
```  

---

## Technologies Used  

- **Python 3**  
- **Turtle Graphics**: For rendering the game objects and movement.  
- **Random Module**: For generating cars and power-up positions.  
- **Time Module**: For managing game speed and power-up duration.  

---

## What I Learned  

- **Object-Oriented Programming (OOP)**:  
  - Implementing modular classes (`Player`, `CarManager`, `Scoreboard`, `PowerUp`).  

- **Game Physics & Collision Detection**:  
  - Checking collisions between the player and cars.  

- **Event Handling & User Input**:  
  - Mapping keyboard inputs to control movement.  

- **Difficulty Scaling in Games**:  
  - Increasing car speed with level progression.  

Challenge yourself in **Turtle Crossing Game** and see how many levels you can reach! 🐢🚗💨
