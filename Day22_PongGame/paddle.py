from turtle import Turtle


class Paddle(Turtle):
    """Represents a paddle in the Pong game, allowing vertical movement."""

    def __init__(self, position):
        """Initializes the paddle with shape, color, and position.

        Args:
            position (tuple): The (x, y) coordinates where the paddle starts.
        """
        super().__init__()
        self.shape("square")  # Set paddle shape
        self.color("white")  # Set paddle color
        self.shapesize(stretch_wid=5, stretch_len=1)  # Adjust paddle size (5 units tall, 1 unit wide)
        self.penup()  # Prevent drawing while moving
        self.goto(position)  # Position the paddle at the given coordinates

    def go_up(self):
        """Moves the paddle up by 20 pixels."""
        new_y = self.ycor() + 20  # Increase y-coordinate
        self.goto(self.xcor(), new_y)  # Move paddle to new position

    def go_down(self):
        """Moves the paddle down by 20 pixels."""
        new_y = self.ycor() - 20  # Decrease y-coordinate
        self.goto(self.xcor(), new_y)  # Move paddle to new position
