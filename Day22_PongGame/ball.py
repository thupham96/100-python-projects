from turtle import Turtle


class Ball(Turtle):
    """Represents the ball in the Pong game, handling movement and collisions."""

    def __init__(self):
        """Initializes the ball with shape, color, position, and movement settings."""
        super().__init__()
        self.shape("circle")  # Set ball shape
        self.color("white")  # Set ball color
        self.penup()  # Prevent drawing lines while moving
        self.x_move = 10  # Ball movement step in x direction
        self.y_move = 10  # Ball movement step in y direction
        self.move_speed = 0.1  # Initial movement speed

    def move(self):
        """Moves the ball to a new position based on current x and y movement values."""
        new_x = self.xcor() + self.x_move  # Calculate new x-coordinate
        new_y = self.ycor() + self.y_move  # Calculate new y-coordinate
        self.goto(new_x, new_y)  # Move the ball to the new position

    def bounce_y(self):
        """Reverses the ball's y-direction when it collides with the top or bottom walls."""
        self.y_move *= -1  # Change y movement direction

    def bounce_x(self):
        """Reverses the ball's x-direction when it collides with a paddle and increases speed."""
        self.x_move *= -1  # Change x movement direction
        self.move_speed *= 0.95  # Increase ball speed slightly after each paddle hit

    def reset_position(self):
        """Resets the ball to the center and restores initial speed after a point is scored."""
        self.goto(0, 0)  # Move the ball to the center of the screen
        self.move_speed = 0.1  # Reset movement speed to default
        self.bounce_x()  # Reverse x-direction to serve towards the opponent
