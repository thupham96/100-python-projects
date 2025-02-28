# Import necessary module
from turtle import Turtle

# Constants for text alignment and font style
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    """Class to manage the scoreboard in the Snake game."""

    def __init__(self):
        """Initialize the scoreboard with default settings."""
        super().__init__()  # Inherit from the Turtle class
        self.score = 0  # Initialize the score
        self.color("white")  # Set text color to white
        self.penup()  # Lift pen to prevent drawing lines
        self.goto(0, 270)  # Position the scoreboard at the top of the screen
        self.update_scoreboard()  # Display the initial score
        self.hideturtle()  # Hide the turtle cursor

    def update_scoreboard(self):
        """Display the current score on the screen."""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase the score by 1 and update the display."""
        self.score += 1  # Increment score
        self.clear()  # Clear the previous score
        self.update_scoreboard()  # Display the updated score

    def game_over(self):
        """Display 'GAME OVER' message at the center of the screen."""
        self.goto(0, 0)  # Move to the center of the screen
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
