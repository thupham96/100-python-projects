import turtle as t
import random

# Define the color list
colors = [(1, 9, 30), (229, 235, 242), (239, 232, 238), (121, 95, 41), (72, 32, 21),
          (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170),
          (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78),
          (3, 78, 28), (1, 64, 147), (221, 179, 218), (4, 220, 218), (80, 135, 179),
          (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220),
          (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165),
          (70, 70, 45), (185, 190, 201), (126, 225, 231), (88, 49, 45), (61, 65, 66)]

# Setup turtle
t.colormode(255)
timmy = t.Turtle()
timmy.speed(0)
timmy.penup()

# Grid size calculation
dot_size = 20
spacing = 50
grid_size = 10 * spacing  # 500 pixels total width & height

# Calculate center position (start in the top-left of the grid)
start_x = -grid_size // 2 + spacing // 2  # -250 + 25 = -225
start_y = grid_size // 2 - spacing // 2    # 250 - 25 = 225

# Set starting position
timmy.setpos(start_x, start_y)

# Draw 10x10 dots grid
for row in range(10):  # 10 rows
    for _ in range(10):  # 10 dots per row
        timmy.dot(dot_size, random.choice(colors))
        timmy.forward(spacing)  # Move forward to place next dot
    # Move turtle to the beginning of the next row
    timmy.setpos(start_x, start_y - (row + 1) * spacing)  # Move down one row

# Hide the turtle and exit
timmy.hideturtle()
screen = t.Screen()
screen.exitonclick()
