import random
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Prompt user for game mode
screen = Screen()
mode = screen.textinput("Choose Mode", "Enter '1' for Single Player or '2' for Dual Player: ")

# If single-player mode is selected, prompt for difficulty level
if mode == '1':
    difficulty = screen.textinput("Difficulty", "Choose difficulty: 'easy', 'medium', or 'hard'")

# Set up the game screen
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)  # Turns off automatic screen updates for smoother animation

# Create paddles, ball, and scoreboard
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Game control variables
game_is_on = True
paused = False

# AI Difficulty Settings (for Single Player Mode)
if mode == '1':
    ai_reaction_delay = 0.2 if difficulty == "easy" else 0.1 if difficulty == "medium" else 0.05  # AI reaction time
    ai_error_chance = 0.3 if difficulty == "easy" else 0.15 if difficulty == "medium" else 0.05  # AI mistake chance
    ai_speed_limit = 10 if difficulty == "easy" else 15 if difficulty == "medium" else 20  # AI max movement speed

def toggle_pause():
    """Pause or resume the game."""
    global paused
    paused = not paused

def restart_game():
    """Restart the game by resetting all elements."""
    global paused
    paused = False
    ball.reset_position()
    scoreboard.reset_score()
    l_paddle.goto(-350, 0)
    r_paddle.goto(350, 0)

# Paddle controls for player(s)
screen.listen()
screen.onkey(r_paddle.go_up, "Up")  # Right paddle moves up
screen.onkey(r_paddle.go_down, "Down")  # Right paddle moves down

# Dual Player Mode: Left paddle controls
if mode == '2':
    screen.onkey(l_paddle.go_up, "w")  # Left paddle moves up
    screen.onkey(l_paddle.go_down, "s")  # Left paddle moves down

# Pause and Restart keys
screen.onkey(toggle_pause, "p")  # Press 'p' to pause/resume
screen.onkey(restart_game, "r")  # Press 'r' to restart the game

# Main game loop
while game_is_on:
    if paused:  # Pause logic
        screen.update()
        time.sleep(0.1)
        continue  # Skip the rest of the loop when paused

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Ball collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Ball collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # AI Paddle movement in Single Player Mode
    if mode == '1':
        if random.random() > ai_error_chance:  # AI makes occasional mistakes
            if l_paddle.ycor() < ball.ycor() and abs(ball.ycor() - l_paddle.ycor()) > ai_speed_limit:
                l_paddle.go_up()
            elif l_paddle.ycor() > ball.ycor() and abs(ball.ycor() - l_paddle.ycor()) > ai_speed_limit:
                l_paddle.go_down()
        time.sleep(ai_reaction_delay)  # Simulate AI reaction time

    # Detect when right paddle misses (Left player scores)
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when left paddle misses (Right player scores)
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()  # Close game window when clicked
