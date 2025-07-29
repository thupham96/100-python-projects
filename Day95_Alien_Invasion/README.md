# Day 95: Alien Invasion – Pygame Shooter

A classic space shooter game built with **Python** and **Pygame**. You control a spaceship that fires bullets at waves of advancing aliens while dodging enemy fire. Stay sharp—if the aliens hit you or reach the bottom, it’s game over!

---

## Features

* Player-controlled **spaceship** with smooth left-right movement
* **Bullet shooting mechanics** with collision detection
* Multiple waves of **animated alien invaders**
* **Alien bullets** fire randomly to challenge your reflexes
* Aliens **descend every few seconds**, increasing pressure
* **Game Over** and **Victory** messages based on your performance
* Dynamic **score progression** and increasing difficulty
* Simple graphics with **custom ship and alien sprites**

---

## Technologies Used

* **Python 3**
* **Pygame** – game development framework for rendering, input, and animation
* **OOP principles** – separate classes for Ship, Alien, and Bullet

---

## Project Structure

```
.
├── main.py            # Main game loop and logic
├── ship.py            # Ship class: movement and rendering
├── alien.py           # Alien class: movement and sprite
├── bullet.py          # Bullet class: player and alien bullets
└── Assets/
    ├── ship.png       # Ship sprite
    └── alien.png      # Alien sprite
```

---

## How to Run

1. Install dependencies:

   ```bash
   pip install pygame
   ```

2. Clone or download this project:

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day95_Alien_Invasion
   ```

3. Run the game:

   ```bash
   python main.py
   ```

---

## How to Play

* **Arrow keys**: Move left and right
* **Spacebar**: Fire bullets
* **Avoid** alien bullets and don’t let aliens touch your ship
* **Eliminate all aliens** to win!

---

## What I Learned

* Managing multiple sprite groups using **Pygame**
* Implementing real-time **collision detection**
* Creating basic **enemy AI** to shoot and descend over time
* Using **timing and intervals** for in-game events (alien drops, enemy fire)
* Structuring game logic with **modular classes**
