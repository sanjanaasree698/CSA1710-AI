# Python Program to Solve the 8-Queen Problem

N = 8

# Function to print the solution
def print_solution(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))

# Check if a queen can be placed safely
def is_safe(board, row, col):
    
    # Check left side of current row
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j]:
            return False
        i += 1
        j -= 1

    return True

# Solve using Backtracking
def solve_queen(board, col):
    
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_queen(board, col + 1):
                return True

            board[i][col] = 0

    return False

# Main Program
board = [[0 for _ in range(N)] for _ in range(N)]

if solve_queen(board, 0):
    print("Solution for 8-Queen Problem:")
    print_solution(board)
else:
    print("No Solution Exists")