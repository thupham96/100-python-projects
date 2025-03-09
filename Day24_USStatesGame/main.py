import turtle
import pandas as pd
import os

# Setup screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load states data
us_states = pd.read_csv("50_states.csv")
states_list = us_states["state"].str.lower().tolist()

# Check if previous game data exists
try:
    guessed_states_previous = pd.read_csv("guessed_states.csv")
    guessed_states = guessed_states_previous["state"].tolist()

    continue_previous_game = screen.textinput(
        title="Welcome Back!",
        prompt="Would you like to continue your previous game? (yes/no)"
    ).strip().lower()

    if continue_previous_game != "yes":
        guessed_states = []
        if os.path.exists("guessed_states.csv"):
            os.remove("guessed_states.csv")
except FileNotFoundError:
    guessed_states = []

# Turtle for writing state names
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

# Write previously guessed states onto screen
for state in guessed_states:
    state_data = us_states[us_states['state'].str.lower() == state].iloc[0]
    writer.goto(int(state_data["x"]), int(state_data["y"]))
    writer.write(state_data["state"], align="center", font=("Arial", 10, "normal"))

incorrect_guesses = 0
max_incorrect_guesses = 5

# Main game loop
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt=f"What's another state name? (Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses})"
    )

    if answer_state is None:
        break

    answer_state = answer_state.strip().lower()

    # Save progress and exit game if user types "exit"
    if answer_state == "exit":
        guessed_states_df = pd.DataFrame(guessed_states, columns=["state"])
        guessed_states_df.to_csv("guessed_states.csv", index=False)
        break

    # Check if guess is correct and hasn't been guessed already
    if answer_state in states_list and answer_state not in guessed_states:
        guessed_states.append(answer_state)

        # Retrieve state coordinates
        state_data = us_states[us_states['state'].str.lower() == answer_state].iloc[0]
        x_cor, y_cor = int(state_data["x"]), int(state_data["y"])

        # Write state name at coordinates
        writer.goto(x_cor, y_cor)
        writer.write(state_data["state"], align="center", font=("Arial", 10, "normal"))

    else:
        incorrect_guesses += 1

    # Check for too many incorrect guesses
    if incorrect_guesses >= max_incorrect_guesses:
        for state in states_list:
            if state not in guessed_states:
                state_data = us_states[us_states['state'].str.lower() == state].iloc[0]
                x_cor, y_cor = int(state_data["x"]), int(state_data["y"])
                writer.goto(x_cor, y_cor)
                writer.write(state_data["state"], align="center", font=("Arial", 10, "normal"))
        screen.title("Game Over! Here are the states you missed.")
        game_is_on = False

    # Check for game completion
    if len(guessed_states) == 50:
        game_is_on = False
        screen.title("Congratulations! You've named all states.")

    # Save the current progress
    guessed_states_df = pd.DataFrame(guessed_states, columns=["state"])
    guessed_states_df.to_csv("guessed_states.csv", index=False)

screen.exitonclick()