# Day 22: Pong Game with AI & Multiplayer  

Welcome to the **Pong Game with AI & Multiplayer** project! This Python program is a modern take on the classic Pong game, built using Python’s **Turtle graphics** module. The game features a **single-player mode with AI-controlled paddle** and a **two-player mode** for competitive play. It also includes difficulty settings, pause/resume functionality, and a scoreboard to track points.  

---

## How It Works  

### Game Setup  

- **Screen Initialization**:  
  - The game window is set to **800x600 pixels** with a black background.  
  - The **automatic screen update** is turned off for smoother animations.  
  - The user is prompted to select **Single Player (AI) or Two-Player Mode**.  
  - In **Single Player Mode**, an additional prompt allows the user to choose **difficulty levels** (`easy`, `medium`, `hard`).  

- **Game Objects**:  
  - **Left Paddle (`l_paddle`)**: Controlled by the player (`W` and `S` keys) or AI in single-player mode.  
  - **Right Paddle (`r_paddle`)**: Controlled by the player (`Up` and `Down` arrow keys).  
  - **Ball**: Moves across the screen and bounces off paddles and walls.  
  - **Scoreboard**: Displays the score and updates when a player earns a point.  

---

### Gameplay Mechanics  

1. **Paddle Movement**:  
   - In **two-player mode**, both paddles are manually controlled using keyboard inputs.  
   - In **single-player mode**, the left paddle is **controlled by AI**, which reacts based on difficulty settings.  

2. **Ball Movement & Bouncing**:  
   - The ball continuously moves in a set direction.  
   - When it **hits the top or bottom walls**, it bounces off.  
   - If it **collides with a paddle**, it bounces back, increasing in speed.  

3. **AI-Controlled Paddle (Single Player Mode Only)**:  
   - The AI paddle **tracks** the ball’s movement and moves up or down accordingly.  
   - **Difficulty levels** adjust the AI’s **reaction time**, **error chance**, and **speed limit**.  

4. **Scoring System**:  
   - When the **right paddle misses**, the left player scores a point.  
   - When the **left paddle (or AI) misses**, the right player scores a point.  
   - The scoreboard updates and displays the new scores.  

5. **Pause & Restart Functionality**:  
   - Press **"P"** to pause or resume the game.  
   - Press **"R"** to restart the game with reset scores and ball position.  

6. **Game Over Conditions**:  
   - The game runs continuously until manually closed by the player.  

---

## Program Design  

### Functional Components  

- **`Paddle` Class**:  
  - Controls paddle movement and positioning.  

- **`Ball` Class**:  
  - Handles movement, bouncing, and speed adjustments upon collision.  

- **`Scoreboard` Class**:  
  - Tracks scores and displays updated results.  

- **Keyboard Event Handling**:  
  - **Arrow keys (`Up`, `Down`)** control the right paddle.  
  - **"W" and "S" keys** control the left paddle (if in two-player mode).  
  - **"P" key** toggles pause/resume.  
  - **"R" key** restarts the game.  

---

## User Interactions  

1. **Start the Game**  
   - Upon launch, the user selects **Single Player (AI) or Two-Player Mode**.  
   - If **Single Player Mode** is chosen, the user selects a **difficulty level**.  

2. **Control the Paddles**  
   - **Two-Player Mode**:  
     - Left paddle: **"W" (Up), "S" (Down)**.  
     - Right paddle: **"Up" (Up), "Down" (Down)**.  
   - **Single Player Mode**:  
     - Right paddle: **Controlled manually**.  
     - Left paddle: **AI-controlled**.  

3. **Score Points**  
   - If a paddle **misses** the ball, the opponent scores a point.  

4. **Pause & Resume the Game**  
   - Press **"P"** to pause or resume at any time.  

5. **Restart the Game**  
   - Press **"R"** to reset the ball and scoreboard.  

6. **Exit the Game**  
   - Click the screen to close the game window.  

---

## How to Run  

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/thupham96/100-python-projects.git  
   cd 100-python-projects/Day22_PongGame
   ```  

2. **Run the Program**:  
   ```bash
   python pong.py
   ```  

3. **Select Game Mode & Difficulty**  
   - Choose **Single Player** (`1`) or **Two Player** (`2`).  
   - If **Single Player**, select difficulty (`easy`, `medium`, `hard`).  

4. **Play & Have Fun!**  

---

## Example Run  

```plaintext
Welcome to Pong Game!  

(Choose mode: Single Player or Two Player...)  
* Single Player Mode selected  
* Difficulty set to "medium"  

Game Starting...  
* The ball moves across the screen.  
* AI paddle reacts to the ball’s movement.  
* Player controls the right paddle with arrow keys.  
* Score updates as points are won.  
* Press "P" to pause, "R" to restart.  
```  

---

## Technologies Used  

- **Python 3**  
- **Turtle Graphics**: For game rendering, paddle movement, and ball physics.  
- **Random Module**: For AI reaction time and slight randomness in paddle movement.  
- **Time Module**: For smooth game timing and AI movement speed adjustments.  

---

## What I Learned  

- **Object-Oriented Programming (OOP)**:  
  - Implementing modular classes (`Paddle`, `Ball`, `Scoreboard`).  

- **Game AI Development**:  
  - Creating an AI-controlled paddle with **difficulty settings**.  

- **Collision Detection & Game Physics**:  
  - Handling paddle-ball interactions and bounce mechanics.  

- **User Input & Event Handling**:  
  - Managing keyboard controls (`Up`, `Down`, `W`, `S`, `P`, `R`).  

Enjoy the game and challenge yourself against AI or a friend in **Pong Game with AI & Multiplayer**! 🏓🎮
