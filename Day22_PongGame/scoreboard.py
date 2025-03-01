from turtle import Turtle

# Font settings for the scoreboard display
FONT = ("Courier", 80, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    """Handles the scoreboard display and scoring system for the Pong game."""

    def __init__(self):
        """Initializes the scoreboard, setting up colors, positioning, and initial scores."""
        super().__init__()
        self.color("white")  # Set scoreboard text color
        self.penup()  # Lift the pen to avoid drawing lines
        self.hideturtle()  # Hide the turtle cursor for a cleaner look
        self.l_score = 0  # Left player's score
        self.r_score = 0  # Right player's score
        self.update_scoreboard()  # Display the initial scoreboard

    def update_scoreboard(self):
        """Clears and updates the scoreboard with the current scores."""
        self.clear()  # Clear the previous score before updating
        self.goto(-100, 200)  # Position for the left player's score
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)  # Position for the right player's score
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        """Increments the left player's score and updates the scoreboard."""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Increments the right player's score and updates the scoreboard."""
        self.r_score += 1
        self.update_scoreboard()

    def reset_score(self):
        """Resets both players' scores to zero and updates the scoreboard."""
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
