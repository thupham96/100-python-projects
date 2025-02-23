# Day 11: Blackjack Game

Welcome to the Blackjack Game! This project recreates the classic card game of Blackjack, where your goal is to get as close to 21 as possible without going over. You will compete against the computer, which acts as the dealer.

[Click here to play the demo](https://trinket.io/python3/cd9b9a08145c?outputOnly=true)

## House Rules

1. **Deck Configuration**:
   - The deck is unlimited in size.
   - No jokers are included.
   - Face cards (Jack, Queen, King) are valued at 10.
   - An Ace can count as either 11 or 1, depending on what benefits the player’s or dealer’s hand.

2. **Card List**:
   ```python
   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
   ```
   - All cards have an equal probability of being drawn.
   - Cards are not removed from the deck after being drawn.

3. **Gameplay**:
   - You play against the computer, which acts as the dealer.
   - Your goal is to reach a hand value closer to 21 than the dealer without exceeding 21.
   - The dealer must draw cards until their total is 17 or higher.

## How It Works

### Game Flow:

1. **Initial Deal**:
   - Both the player and the dealer are dealt two cards.
   - One of the dealer’s cards is hidden until the end of the round.

2. **Player Turn**:
   - You can choose to:
     - Type 'y' to get another card
     - Type 'n' to pass

3. **Dealer Turn**:
   - The dealer will reveal their hidden card.
   - The dealer draws cards until their hand value is at least 17.

4. **Winning Conditions**:
   - You win if:
     - Your hand is closer to 21 than the dealer’s.
     - The dealer’s hand exceeds 21 (busts).
   - You lose if:
     - Your hand exceeds 21 (busts).
     - The dealer’s hand is closer to 21 without busting.

### Example Run:
```plaintext
Do you want to play a game of Blackjack? Type 'y' or 'n': y
Your cards: [7, 3], current score: 10
Computer's first card: 6
Type 'y' to get another card, type 'n' to pass: y
Your cards: [7, 3, 10], current score: 20
Computer's first card: 6
Type 'y' to get another card, type 'n' to pass: n
Your final hand: [7, 3, 10], final score: 20
Computer's final hand: [6, 8, 10], final score: 24
Computer went over 21. You win!
```

## Features

- **Dynamic Hand Scoring**: Adjusts the value of Aces based on the hand's total score.
- **Dealer AI**: Follows standard Blackjack rules for drawing cards.
- **Unlimited Deck**: Cards are drawn with replacement for infinite gameplay possibilities.

## How to Play

1. Clone the repository and navigate to the `Day11_BlackjackGame` folder:
   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd 100-python-projects/Day11_BlackjackGame
   ```

2. Run the game script:
   ```bash
   python blackjack_game.py
   ```

3. Follow the on-screen instructions to play the game!

## Technologies Used

- Python 3
- Random module for shuffling and drawing cards

## What I Learned

- Implementing game logic and rules for a turn-based card game.
- Managing dynamic data structures like lists for player and dealer hands.
- Using conditional logic to determine game outcomes and handle edge cases.

Enjoy the Blackjack Game and see how lucky you can get! 🎲🃏

