import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

play_again = "y"

while play_again == "y":
    user_score = 0
    computer_score = 0
    rounds = int(input("How many rounds would you like to play? (Best of N): "))
    rounds_to_win = (rounds // 2) + 1
    current_round = 1

    print(f"\n🎮 Starting Best of {rounds} — First to {rounds_to_win} wins!\n")

    while current_round <= rounds:
        print(f"--- Round {current_round} ---")
        try:
            user_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
            if user_choice not in [0, 1, 2]:
                print("Invalid input. You lose this round by default!")
                computer_score += 1
            else:
                computer_choice = random.randint(0, 2)
                print(f"\nYou chose:\n{choices[user_choice]}")
                print(f"Computer chose:\n{choices[computer_choice]}")

                if user_choice == computer_choice:
                    print("It's a draw!")
                elif (user_choice == 0 and computer_choice == 2) or \
                     (user_choice == 1 and computer_choice == 0) or \
                     (user_choice == 2 and computer_choice == 1):
                    print("You win this round!")
                    user_score += 1
                else:
                    print("Computer wins this round!")
                    computer_score += 1
        except ValueError:
            print("Invalid input. You lose this round by default!")
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer\n")
        current_round += 1

    if user_score > computer_score:
        print("🎉 You won the game!")
    elif user_score < computer_score:
        print("😞 Computer won the game!")
    else:
        print("It's a draw!")

    play_again = input("\nDo you want to play another Best of N game? (y/n): ").lower()

print("Thanks for playing!")
