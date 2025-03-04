from turtle import Turtle

# Constants
STARTING_POSITION = (0, -280)
DEFAULT_MOVE_DISTANCE = 10  # Default speed
FINISH_LINE_Y = 280
LEFT_LIMIT = -280
RIGHT_LIMIT = 280

class Player(Turtle):
    def __init__(self):
        """Initializes the player turtle with movement controls."""
        super().__init__()
        self.color("black")
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.go_to_start()
        self.move_distance = DEFAULT_MOVE_DISTANCE  # Variable speed

    def move_up(self):
        """Moves the player forward (upward)."""
        self.forward(self.move_distance)

    def move_down(self):
        """Moves the player backward (downward)."""
        if self.ycor() > STARTING_POSITION[1]:
            self.backward(self.move_distance)

    def move_left(self):
        """Moves the player left, ensuring they stay within bounds."""
        if self.xcor() > LEFT_LIMIT:
            self.goto(self.xcor() - self.move_distance, self.ycor())

    def move_right(self):
        """Moves the player right, ensuring they stay within bounds."""
        if self.xcor() < RIGHT_LIMIT:
            self.goto(self.xcor() + self.move_distance, self.ycor())

    def go_to_start(self):
        """Resets the player's position to the starting point."""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Checks if the player has crossed the finish line."""
        return self.ycor() > FINISH_LINE_Y

    def activate_speed_boost(self):
        """Temporarily increases the player's movement speed."""
        self.move_distance = DEFAULT_MOVE_DISTANCE * 2  # Double speed

    def reset_speed_boost(self):
        """Resets the player's movement speed to normal."""
        self.move_distance = DEFAULT_MOVE_DISTANCE
