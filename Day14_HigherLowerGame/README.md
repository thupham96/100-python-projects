# Day 14: Higher or Lower Game

Welcome to the Higher or Lower Game! This Python project is a fun and interactive game that tests your knowledge of popular individuals' social media followings. The challenge is to guess whether the next person has a higher or lower follower count than the current one.

## How It Works

### Game Setup:

- The program provides data for multiple famous individuals, each with their social media follower counts.
- It displays the name, profession, and country of origin of two individuals (Person A and Person B).
- Your task is to determine if Person A has a higher or lower follower count compared to Person B.

### Gameplay:

1. The program shows details for Person A and Person B.
2. You input your guess:
   - Type `'A'` if you think Person A has more followers.
   - Type `'B'` if you think Person B has more followers.
3. The program reveals whether your guess is correct:
   - If correct, your score increases, and the program shows details for the next 2 people.
   - If incorrect, the game ends, and your final score is displayed.

### End of Game:

- Your final score is displayed when you make an incorrect guess.
- You can restart the game to try for a higher score!

## Features

- **Fascinating Comparisons**: Learn fun facts about popular individuals and their professions.
- **Simple Interface**: Input-based interaction ensures smooth gameplay.

## How to Play

1. Clone the repository and navigate to the `Day14_HigherLowerGame` folder:
   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd 100-python-projects/Day14_HigherLowerGame
   ```

2. Run the game script:
   ```bash
   python higher_lower_game.py
   ```

3. Follow the on-screen instructions to compare follower counts and see how far you can go!

## Example Run

```plaintext
Welcome to the Higher or Lower Game!
Compare A: David Beckham, a Footballer, from United Kingdom.
Against B: Gigi Hadid, a Model, from United States.
Who has more followers? Type 'A' or 'B': A
You're right! Current score: 1.

Compare A: Cardi B, a Musician, from United States.
Against B: FC Barcelona, a Football club, from Spain.
Who has more followers? Type 'A' or 'B': B
You're right. Current score: 2.

Compare A: Cardi B, a Musician, from United States.
Against B: Taylor Swift, a Musician, from United States.
Who has more followers? Type 'A' or 'B': A
Sorry, that's wrong. Final score: 2.
```

## Technologies Used

- Python 3
- Random module
- Custom dictionaries for data storage and retrieval

## What I Learned

- Using dictionaries to store and retrieve structured data.
- Implementing game loops and user input handling in Python.
- Generating random selections for engaging gameplay.
- Formatting and presenting data in a user-friendly way.

Enjoy playing the Higher or Lower Game, and challenge yourself to achieve the highest score possible! 🎉
