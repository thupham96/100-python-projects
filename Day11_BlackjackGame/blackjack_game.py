import random
import art

# Display the Blackjack game logo
print(art.logo)

# Define the deck of cards with face cards (10) and Ace (11)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Ask the user if they want to start the game
continue_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

# Function to calculate the sum of cards in hand
def sum_cards(cards):
    sum_of_cards = sum(cards)  # Initial sum of all cards
    count_of_11 = cards.count(11)  # Count the number of Aces (11s)
    # Adjust the value of Ace (11 -> 1) if the total exceeds 21
    while sum_of_cards > 21 and count_of_11 > 0:
        sum_of_cards -= 10
        count_of_11 -= 1
    return sum_of_cards

# Function to check if the hand is a Blackjack (Ace + 10)
def has_black_jack(cards):
    if 10 in cards and 11 in cards and len(cards) == 2:
        return True
    return False

# Main game loop
while continue_game == "y":
    # Deal initial two cards to player and computer
    player_cards = random.choices(cards, k=2)
    player_score = sum_cards(player_cards)
    computer_cards = random.choices(cards, k=2)
    computer_score = sum_cards(computer_cards)

    # Display the player's cards and computer's first card
    print(f"Your cards: {str(player_cards)}, current score: {str(player_score)}")
    print(f"Computer's first card: {str(computer_cards[0])}")

    # Check for Blackjack conditions
    computer_has_black_jack = has_black_jack(computer_cards)
    player_has_black_jack = has_black_jack(player_cards)

    # If no immediate Blackjack and scores are under 21, ask the player to continue or pass
    if player_score <= 21 and computer_score <= 21 and not computer_has_black_jack and not player_has_black_jack:
        continue_next_card = input("Type 'y' to get another card, type 'n' to pass: ")
    else:
        continue_next_card = "n"

    # Player's turn to draw additional cards
    while continue_next_card == "y" and player_score <= 21:
        player_cards.append(random.choice(cards))  # Draw a new card
        player_score = sum_cards(player_cards)  # Update the player's score
        print(f"Your cards: {str(player_cards)}, current score: {str(player_score)}")
        print(f"Computer's first card: {str(computer_cards[0])}")
        if player_score <= 21:
            continue_next_card = input("Type 'y' to get another card, type 'n' to pass: ")

    # Dealer's turn: Draw cards until the total is at least 17
    while computer_score < 17:
        computer_cards.append(random.choice(cards))  # Dealer draws a new card
        computer_score = sum_cards(computer_cards)  # Update the dealer's score

    # Display final hands and scores
    print(f"Your final hand: {str(player_cards)}, final score: {str(player_score)}")
    print(f"Computer's final hand: {str(computer_cards)}, final score: {str(computer_score)}")

    # Determine the game result
    if computer_has_black_jack:
        print("Computer has Blackjack! You lose.\n")
    elif player_has_black_jack:
        print("You have Blackjack! You win!\n")
    elif player_score > 21:
        print("You went over. You lose.\n")
    elif computer_score > 21:
        print("Computer went over 21. You win!\n")
    elif player_score > computer_score:
        print("Your score is higher than the computer's! You win!\n")
    elif player_score == computer_score:
        print("It's a tie! No winner this time.\n")
    else:
        print("Computer has a higher score. You lose!\n")

    # Ask if the player wants to play another game
    continue_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if continue_game == "y":
        print("\n" * 100)  # Clear the screen for the next game

