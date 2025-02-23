import random
from turtle import Turtle, Screen
from tkinter import messagebox  # For popup messages
import time

def countdown():
    countdown_turtle = Turtle()
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    countdown_turtle.goto(0, 0)
    # Display a countdown from 3 to 1, then "Go!"
    for i in range(3, 0, -1):
        countdown_turtle.write(i, align="center", font=("Arial", 24, "bold"))
        time.sleep(1)
        countdown_turtle.clear()
    countdown_turtle.write("Go!", align="center", font=("Arial", 24, "bold"))
    time.sleep(1)
    countdown_turtle.clear()

def get_user_bet(valid_colors):
    bet = screen.textinput(
        title="Make your bet",
        prompt=f"Which turtle will win the race? Enter a color from: {', '.join(valid_colors)}"
    )
    while bet not in valid_colors:
        bet = screen.textinput(
            title="Invalid Choice",
            prompt=f"Please choose a color from: {', '.join(valid_colors)}"
        )
    return bet

def get_rematch_input():
    rematch = screen.textinput(title="Rematch", prompt="Do you want a rematch? (y/n)")
    while rematch is None or rematch.lower() not in ['y', 'n']:
        rematch = screen.textinput(title="Invalid Input", prompt="Please enter 'y' or 'n' for rematch:")
    return rematch.lower()

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race Game")  # Changed window title

# Define valid colors (and matching starting positions)
valid_colors = ["red", "green", "blue", "black", "orange", "pink"]
y_positions = [-70, -40, -10, 20, 50, 80]

# Get a valid bet from the user
user_bet = get_user_bet(valid_colors)

all_turtles = []
for i in range(len(valid_colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(valid_colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)

# Start countdown before beginning the race
countdown()

is_race_on = True

while is_race_on:
    for t in all_turtles:
        t.forward(random.randint(0, 10))
        if t.xcor() > 230:
            winning_color = t.pencolor()
            if winning_color == user_bet:
                messagebox.showinfo("Race Result", f"You've won. The {winning_color} turtle is the winner!")
            else:
                messagebox.showinfo("Race Result", f"You've lost. The {winning_color} turtle is the winner!")
            rematch_choice = get_rematch_input()
            if rematch_choice == "n":
                is_race_on = False
            else:
                user_bet = get_user_bet(valid_colors)
                for index, t_reset in enumerate(all_turtles):
                    t_reset.goto(x=-230, y=y_positions[index])
                countdown()  # Run countdown again for a new race
            # End the current race round.
            break

screen.exitonclick()
