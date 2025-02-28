# Import necessary module
from turtle import Turtle

# Constants for movement and direction
MOVE_DISTANCE = 20  # Distance the snake moves per step
UP = 90  # Angle representing the "Up" direction
DOWN = 270  # Angle representing the "Down" direction
LEFT = 180  # Angle representing the "Left" direction
RIGHT = 0  # Angle representing the "Right" direction


class Snake:
    """Class to create and control the snake in the game."""

    def __init__(self):
        """Initialize the snake by creating its segments and setting the head."""
        self.segments = []  # List to store all snake segments
        self.create_snake()  # Create initial snake body
        self.head = self.segments[0]  # Define the first segment as the head

    def create_snake(self):
        """Create the initial three-segment snake."""
        for i in range(3):  # The snake starts with three segments
            x = 0 - i * 20  # Position segments in a row (horizontally)
            self.add_segment(x, 0)  # Create and place each segment

    def move(self):
        """Move the snake forward by shifting segment positions."""
        # Move each segment to the position of the previous one (starting from the tail)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # Get x-coordinate of previous segment
            new_y = self.segments[seg_num - 1].ycor()  # Get y-coordinate of previous segment
            self.segments[seg_num].goto(new_x, new_y)  # Move current segment to new position

        self.head.forward(MOVE_DISTANCE)  # Move the head forward

    def up(self):
        """Change direction to 'Up' if not currently moving 'Down'."""
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change direction to 'Down' if not currently moving 'Up'."""
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change direction to 'Left' if not currently moving 'Right'."""
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change direction to 'Right' if not currently moving 'Left'."""
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self, x, y):
        """Create a new snake segment and add it to the body."""
        new_turtle = Turtle()  # Create a new turtle object for the segment
        new_turtle.shape("square")  # Set shape to square
        new_turtle.color("white")  # Set color to white
        new_turtle.penup()  # Lift the pen to prevent drawing lines
        new_turtle.goto(x, y)  # Place segment at specified coordinates
        self.segments.append(new_turtle)  # Add segment to the snake's body

    def extend(self):
        """Extend the snake by adding a new segment at the last segment's position."""
        last_x, last_y = self.segments[-1].position()  # Get position of the last segment
        self.add_segment(last_x, last_y)  # Add a new segment at that position
