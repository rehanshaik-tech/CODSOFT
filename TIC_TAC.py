import math

board = [" " for _ in range(9)]

def show_board():
    print()
    for i in range(0, 9, 3):
        print(" " + board[i] + " | " + board[i+1] + " | " + board[i+2])
        if i < 6:
            print("---+---+---")
    print()

def check_winner(player):
    win = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for line in win:
        if all(board[i] == player for i in line):
            return True
    return False

def board_full():
    return " " not in board

def minimax(is_ai):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if board_full():
        return 0

    if is_ai:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)
        return best

def ai_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"

def player_move():
    while True:
        try:
            pos = int(input("Enter position (1-9): ")) - 1

            if pos < 0 or pos > 8:
                print("Choose between 1 and 9.")
            elif board[pos] != " ":
                print("Position already taken.")
            else:
                board[pos] = "X"
                break

        except:
            print("Enter a valid number.")

print("====== TIC-TAC-TOE AI ======")
print("You are X")
print()

while True:

    print("Board Positions")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")

    show_board()

    player_move()

    if check_winner("X"):
        show_board()
        print("🎉 You Win!")
        break

    if board_full():
        show_board()
        print("It's a Draw!")
        break

    print("AI is thinking...")
    ai_move()

    if check_winner("O"):
        show_board()
        print("🤖 AI Wins!")
        break

    if board_full():
        show_board()
        print("It's a Draw!")
        break