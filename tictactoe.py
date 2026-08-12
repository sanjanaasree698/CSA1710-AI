# Python Program for Tic Tac Toe Game

# Function to display the board
def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check winner
def check_winner(board, player):

    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Main Program
board = [[" " for _ in range(3)] for _ in range(3)]

current_player = "X"

for turn in range(9):

    print_board(board)

    print(f"Player {current_player}'s Turn")

    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))

    if board[row][col] == " ":
        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} Wins!")
            break

        current_player = "O" if current_player == "X" else "X"

    else:
        print("Cell already occupied. Try again.")
else:
    print_board(board)
    print("It's a Draw!")