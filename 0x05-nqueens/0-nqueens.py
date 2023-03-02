#!/usr/bin/python3

import sys

def n_queens(n):
    # Initialize board and solutions list
    board = [-1] * n
    solutions = []
    
    # Check if a queen can be placed in the given (row, col)
    def is_valid(row, col):
        for r, c in enumerate(board[:row]):
            if col == c or row - r == abs(col - c):
                return False
        return True
    
    # Recursive function to find solutions
    def backtrack(row):
        # Base case: all rows filled, add solution
        if row == n:
            solutions.append(board[:])
            return
        
        # Check each column in current row
        for col in range(n):
            if is_valid(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1
        
    # Start solving from the first row
    backtrack(0)
    
    # Print solutions
    for sol in solutions:
        print(" ".join(str(x+1) for x in sol))

# Parse command-line argument
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

# Solve N-Queens puzzle
n_queens(n)
