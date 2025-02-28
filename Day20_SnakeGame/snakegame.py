# Import necessary modules
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from obstacle import Obstacle

# Set up the game screen
screen = Screen()
screen.setup(height=600, width=600)  # Define screen size
screen.bgcolor("black")  # Set background color
screen.title("Snake Game")  # Set window title
screen.tracer(0)  # Disable automatic screen updates for smooth animation

# Create game objects
snake = Snake()  # Initialize the snake
food = Food()  # Initialize the food object
scoreboard = Scoreboard()  # Initialize the scoreboard
obstacle = Obstacle()  # Initialize obstacles

# Listen for keypress events to control the snake
screen.listen()
screen.onkey(snake.up, "Up")  # Move up
screen.onkey(snake.down, "Down")  # Move down
screen.onkey(snake.left, "Left")  # Move left
screen.onkey(snake.right, "Right")  # Move right

# Game control variables
game_is_on = True
speed = 0.2  # Initial game speed

# Main game loop
while game_is_on:
    screen.update()  # Refresh screen
    time.sleep(speed)  # Control game speed
    snake.move()  # Move the snake forward

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()  # Generate new food location
        scoreboard.increase_score()  # Update score
        snake.extend()  # Grow the snake
        speed *= 0.95  # Increase difficulty by making the snake move faster

    # Detect collision with wall (game over condition)
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_is_on = False
        scoreboard.game_over()  # Display game over message

    # Detect collision with itself (game over condition)
    for seg in snake.segments[1:]:  # Exclude the head
        if snake.head.distance(seg) < 10:
            game_is_on = False
            scoreboard.game_over()  # Display game over message

    # Detect collision with obstacles (game over condition)
    for obs in obstacle.obstacles:
        if snake.head.distance(obs) < 15:
            game_is_on = False
            scoreboard.game_over()  # Display game over message

# Close the game window when clicked
screen.exitonclick()
