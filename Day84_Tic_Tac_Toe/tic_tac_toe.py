# set up the board
board = [" " for _ in range(9)]

# display the board
def display_board():
    print("\n")
    print(f" {board[0] if board[0] != " " else '1'} | {board[1] if board[1] != " " else '2'} | {board[2] if board[2] != " " else '3'} ")
    print("---+---+---")
    print(f" {board[3] if board[3] != " " else '4'} | {board[4] if board[4] != " " else '5'} | {board[5] if board[5] != " " else '6'} ")
    print("---+---+---")
    print(f" {board[6] if board[6] != " " else '7'} | {board[7] if board[7] != " " else '8'} | {board[8] if board[8] != " " else '9'} ")
    print("\n")


# check for a win
def check_win():
    win_combo = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for i in range(len(win_combo)):
        if board[win_combo[i][0]] == board[win_combo[i][1]] == board[win_combo[i][2]] \
            and board[win_combo[i][0]] != " ":
            return True
    return False

# check for a tie
def check_tie():
    for i in range(len(board)):
        if board[i] == " ":
            return False
    return True

# game logic
def game_logic():
    game_is_on = True
    current_player = "X"
    while game_is_on:
        move_is_valid = False
        while not move_is_valid:
            next_move = input(f"Play {current_player}, please choose 1 number from 1-9 for the next move: ")
            next_move = int(next_move) - 1
            if next_move < 0 or next_move > 8:
                print("Invalid move. Please choose another number position between 1-9.")
            elif board[next_move] != " ":
                print("This position is not available. Please choose another number position.")
            else:
                board[next_move] = current_player
                move_is_valid = True
        if check_win():
            print(f"🎉 Player {current_player} wins the match!")
            game_is_on = False
        if check_tie():
            print("😮 It's a stalemate! No winner this time.")
            game_is_on = False
        display_board()
        current_player = "X" if current_player == "O" else "O"

# main loop
def main():
    print("Welcome to Tic-Tac-Toe!")
    display_board()
    next_game = "y"
    while next_game.lower() == "y":
        # reset board
        global board
        board = [" " for _ in range(9)]
        game_logic()
        next_game = input("Would you like to play another game? (y/n) ")

main()
