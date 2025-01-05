import art
import random

# Display the logo
print(art.logo)

# Introduction message
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Choose a random number between 1 and 100
chosen_number = random.randint(1, 100)

# Determine difficulty level
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty_level == "easy":
    number_of_attempts = 10  # 10 attempts for easy mode
else:
    number_of_attempts = 5   # 5 attempts for hard mode

continue_guessing = True

# Start the guessing loop
while continue_guessing:
    # Prompt the user for a guess
    guess = int(input(f"You have {number_of_attempts} attempts remaining to guess the number.\n"
                      f"Make a guess: "))
    
    # Check if the guess is too high
    if guess > chosen_number:
        print("Too high.")
    # Check if the guess is too low
    elif guess < chosen_number:
        print("Too low.")
    # Correct guess
    else:
        print(f"You got it! The answer was {chosen_number}.")
        continue_guessing = False  # End the loop after a correct guess

    # Decrease the number of attempts after each guess
    number_of_attempts -= 1

    # Continue prompting the user if they still have attempts left
    if number_of_attempts > 0 and continue_guessing == True:
        print("Guess again.")
    # If no attempts are left, end the game
    elif number_of_attempts == 0:
        print(f"You've run out of guesses. The answer was {chosen_number}.")
        continue_guessing = False  # End the loop when attempts are exhausted
