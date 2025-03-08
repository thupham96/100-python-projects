print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  `. ,_""._;   |
          |           | ;`"=._o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____|__________________
____/______/______/_/"=._o._; | ;_.--"o.--"_/______/______/_____/_____________
____/______/______/______/______/_____"=.o|o_.--""_/______/______/______/_____
*******************************************************************************
''')

left_or_right = input('You\'re at a crossroad, where do you want to go? Type "left" or "right"\n').lower()

if left_or_right == "left":
    puzzle_answer = input('A mysterious sage blocks your path with a puzzle: "What has a head and a tail but no body?"\n').lower()
    if puzzle_answer == "coin":
        swim_or_wait = input('Correct! You reach a lake with an island in the middle. Type "wait" for a boat, or "swim" across.\n').lower()
        if swim_or_wait == "wait":
            riddle_answer = input('You safely arrive. A magical guardian appears. Solve this: "I speak without a mouth and hear without ears. I have nobody, but I come alive with wind. What am I?"\n').lower()
            if riddle_answer == "echo":
                second_riddle = input('The guardian gives you one more riddle: "The more of this there is, the less you see. What am I?"\n').lower()
                if second_riddle == "darkness":
                    final_puzzle = input('One final puzzle awaits: "What can you break, even if you never pick it up or touch it?"\n').lower()
                    if final_puzzle == "promise":
                        which_door = input('Correct! Three doors appear: Red, Yellow, Blue. Choose wisely.\n').lower()
                        if which_door == "red":
                            print("Room full of fire. Game Over.")
                        elif which_door == "yellow":
                            print("You found the treasure! You Win!")
                        elif which_door == "blue":
                            print("Room full of beasts. Game Over.")
                        else:
                            print("That door doesn't exist. Game Over.")
                    else:
                        print("Incorrect! A broken promise ends your quest. Game Over.")
                else:
                    print("Incorrect! Darkness envelops you. Game Over.")
            else:
                print("Incorrect. The guardian banishes you. Game Over.")
        else:
            print("Attacked by an angry trout. Game Over.")
    else:
        print("Wrong answer! The sage curses you. Game Over.")
else:
    print("You fell into a pit of snakes. Game Over.")
