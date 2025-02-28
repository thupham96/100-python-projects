# Import necessary modules
import random
from turtle import Turtle

class Food(Turtle):
    """Class to create and manage the food object in the Snake game."""

    def __init__(self):
        """Initialize the food object with default settings."""
        super().__init__()  # Inherit from Turtle class
        self.shape("circle")  # Set shape to a circle
        self.penup()  # Lift pen to prevent drawing
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Make the food smaller (default size is 20x20, so this makes it 10x10)
        self.color("blue")  # Set color to blue
        self.speed("fastest")  # Set the fastest movement speed to avoid flickering
        self.refresh()  # Call refresh method to place food at a random location

    def refresh(self):
        """Move the food to a new random position on the screen."""
        random_x = random.randint(-280, 280)  # Generate random x-coordinate
        random_y = random.randint(-280, 280)  # Generate random y-coordinate
        self.goto(random_x, random_y)  # Move food to the new position
