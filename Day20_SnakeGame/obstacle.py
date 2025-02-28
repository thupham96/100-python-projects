# Import necessary modules
from turtle import Turtle
import random


class Obstacle:
    """Class to create and manage obstacles in the Snake game."""

    def __init__(self):
        """Initialize the obstacle list and create a set number of obstacles."""
        self.obstacles = []  # List to store obstacle objects
        for _ in range(3):  # Create 3 obstacles initially
            self.add_obstacle()

    def add_obstacle(self):
        """Create a new obstacle at a random position and add it to the list."""
        obstacle = Turtle()  # Create a new turtle object for the obstacle
        obstacle.shape("square")  # Set shape to square
        obstacle.color("red")  # Set color to red (dangerous element)
        obstacle.penup()  # Lift the pen to prevent drawing
        obstacle.goto(random.randint(-250, 250), random.randint(-250, 250))  # Place randomly on the screen
        self.obstacles.append(obstacle)  # Store the obstacle in the list
