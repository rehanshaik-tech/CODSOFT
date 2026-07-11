# Tic-Tac-Toe AI using Minimax
# Internship Task 2

board = [" " for _ in range(9)]

# Display board
def show_board():
    print()
    for i in range(3):
        print(" " + board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i < 2:
            print("---|---|---")
    print()

# Check winner
def check_winner(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(board[pos] == player for pos in line) for line in wins)

# Check draw
def is_draw():
    return " " not in board

# Minimax Algorithm
def minimax(is_ai):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_ai:
        best = -100
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)
        return best

# AI Move
def ai_move():
    best_score = -100
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

# Human Move
def human_move():
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move. Try again.")
        except:
            print("Enter a valid number.")

# Main Game
print("TIC-TAC-TOE")
print("You = X | AI = O")
print("Board Positions:")
print("1 | 2 | 3")
print("4 | 5 | 6")
print("7 | 8 | 9")

while True:
    show_board()
    human_move()

    if check_winner("X"):
        show_board()
        print("🎉 You Win!")
        break

    if is_draw():
        show_board()
        print("🤝 It's a Draw!")
        break

    ai_move()

    if check_winner("O"):
        show_board()
        print("🤖 AI Wins!")
        break

    if is_draw():
        show_board()
        print("🤝 It's a Draw!")
        break