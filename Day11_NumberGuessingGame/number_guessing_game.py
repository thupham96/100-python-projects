import art
import random

print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Choose a random number between 1 and 100
chosen_number = random.randint(1, 100)

# Determine difficulty level
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty_level=="easy":
    number_of_attempts = 10
else:
    number_of_attempts = 5

continue_guessing = True

# Ask the player to guess and give feedback
while continue_guessing:
    guess = int(input(f"You have {number_of_attempts} attempts remaining to guess the number.\n"
                      f"Make a guess: "))
    if guess > chosen_number:
        print("Too high.")
    elif guess < chosen_number:
        print("Too low.")
    else:
        print(f"You got it! The answer was {chosen_number}.")
        continue_guessing = False

    number_of_attempts -= 1

    if number_of_attempts > 0 and continue_guessing == True:
        print("Guess again.")
    elif number_of_attempts == 0:
        print(f"You've run out of guesses. The answer was {chosen_number}.")
        continue_guessing = False

