import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from powerup import PowerUp  # Import power-up

# Constants
POWERUP_DURATION = 5  # Power-up lasts 5 seconds
POWERUP_SPAWN_RATE = 10  # Every 10 loops

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

# Initialize game objects
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
powerup = PowerUp()

# Listen for player input
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")  # Optional: Move down
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

# Game loop
game_is_on = True
n_loop = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create a new car every few loops
    if n_loop % 6 == 0:
        car_manager.create_car()

    car_manager.move_cars()

    # Spawn power-up occasionally
    if n_loop % POWERUP_SPAWN_RATE == 0:
        powerup.spawn()

    # **Collision Detection with Cars**
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    # **Check if player collects power-up**
    if powerup.active and player.distance(powerup) < 20:
        powerup.collect()
        player.activate_speed_boost()  # Correct way to speed up player
        # Reset speed and speed_boost after POWERUP_DURATION seconds
        screen.ontimer(lambda: player.reset_speed_boost(), POWERUP_DURATION * 1000)

    # **Check if player reaches finish line**
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.next_level()
        car_manager.increase_speed()

    n_loop += 1

screen.mainloop()
