import art
import game_data
import random

# Print the game logo from the art module to introduce the game
print(art.logo)
print("Welcome to the Higher or Lower Game.")

# Initialize the game state
continue_game = True  # Variable to control the game loop
current_score = 0     # Variable to keep track of the player's score

# Main game loop
while continue_game:
    # Select two random options from the game data
    options = random.choices(game_data.data, k=2)
    option_a = options[0]  # First option (Person A)
    option_b = options[1]  # Second option (Person B)
    
    # Display details of Person A
    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
    
    # Print the "vs" graphic
    print(art.vs)
    
    # Display details of Person B
    print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")
    
    # Ask the user for their guess (A or B)
    user_answer = input("Who has more followers? Type 'A' or 'B': ")
    
    # Determine which option has more followers
    if option_a['follower_count'] > option_b['follower_count']:
        correct_answer = 'A'  # Person A has more followers
    else:
        correct_answer = 'B'  # Person B has more followers
    
    # Check if the user's guess is correct
    if user_answer == correct_answer:
        # If correct, increase the score and provide feedback
        current_score += 1
        print(f"You're right. Current score: {current_score}.")
    else:
        # If incorrect, end the game and display the final score
        continue_game = False
        print(f"Sorry, that's wrong. Final score: {current_score}.")

