def print_board(board):
    print(board[0][0], "|", board[0][1], "|", board[0][2])
    print("---------")
    print(board[1][0], "|", board[1][1], "|", board[1][2])
    print("---------")
    print(board[2][0], "|", board[2][1], "|", board[2][2])

def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True
    return False

def tic_tac_toe():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = "X"
    game_over = False

    while not game_over:
        print_board(board)
        row = int(input("Enter the row number: "))
        col = int(input("Enter the column number: "))

        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("That spot is already taken!")
            continue

        if check_win(board):
            print_board(board)
            print("Congratulations,", player, "wins!")
            game_over = True
        elif " " not in board[0] and " " not in board[1] and " " not in board[2]:
            print_board(board)
            print("It's a tie!")
            game_over = True
        else:
            player = "O" if player == "X" else "X"

tic_tac_toe() 