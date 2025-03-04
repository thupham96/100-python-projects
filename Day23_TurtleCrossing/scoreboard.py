from turtle import Turtle

# Constants
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
SCOREBOARD_POSITION = (-200, 250)

class Scoreboard(Turtle):
    def __init__(self):
        """Initializes the scoreboard, setting up colors, positioning, and initial scores."""
        super().__init__()
        self.color("black")  # Set scoreboard text color
        self.penup()  # Lift the pen to avoid drawing lines
        self.hideturtle()  # Hide the turtle cursor for a cleaner look
        self.level = 1  # Initial game level
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears and redraws the scoreboard."""
        self.clear()
        self.goto(SCOREBOARD_POSITION)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def next_level(self):
        """Increments the player's level and updates the scoreboard."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Displays 'GAME OVER' at the center of the screen."""
        self.goto(0, 0)  # Move to the center
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
