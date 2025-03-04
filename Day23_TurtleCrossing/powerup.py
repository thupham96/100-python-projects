from turtle import Turtle
import random

class PowerUp(Turtle):
    def __init__(self):
        """Creates a power-up item that appears randomly on the screen."""
        super().__init__()
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.hideturtle()
        self.active = False  # Whether the power-up is currently on screen

    def spawn(self):
        """Makes the power-up appear at a random location."""
        if not self.active:
            self.goto(random.randint(-250, 250), random.randint(-250, 250))
            self.showturtle()
            self.active = True

    def collect(self):
        """Handles what happens when the player collects the power-up."""
        self.hideturtle()
        self.active = False  # Power-up is no longer active
