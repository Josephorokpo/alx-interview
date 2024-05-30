#!/usr/bin/python3
"""
N Queens puzzle solver.

This script solves the N Queens puzzle, which is the challenge of placing N
non-attacking queens on an N×N chessboard. The script prints all possible
solutions.

Usage:
    nqueens N

Arguments:
    N : The size of the chessboard (N×N) and the number of queens.

Error handling:
    - If the user provides the wrong number of arguments, it prints:
      Usage: nqueens N
    - If N is not an integer, it prints:
      N must be a number
    - If N is less than 4, it prints:
      N must be at least 4

Requirements:
    - All files should end with a new line.
    - The first line of all files should be exactly #!/usr/bin/python3.
    - The code should follow PEP 8 style (version 1.7.*).
    - All files must be executable.
"""

import sys


def print_solution(solution):
    """
    Prints a single solution in the required format.

    Args:
        solution (list of list of int): A single solution where each inner
        list contains two integers, the row and column positions of a queen.
    """
    print(solution)


def is_safe(board, row, col):
    """
    Checks if a queen can be placed on board[row][col].

    Args:
        board (list of list of int): The chessboard.
        row (int): The row index.
        col (int): The column index.

    Returns:
        bool: True if it is safe to place the queen, False otherwise.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, solutions):
    """
    Utilizes backtracking to solve the N Queens problem.

    Args:
        board (list of list of int): The chessboard.
        col (int): The current column index.
        solutions (list of list of list of int): The list of solutions.
    """
    if col == len(board):
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, solutions)
            board[i][col] = 0


def solve_nqueens(n):
    """
    Solves the N Queens problem and prints all solutions.

    Args:
        n (int): The size of the chessboard (N×N) and the number of queens.
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, solutions)
    for solution in solutions:
        print_solution(solution)


def main():
    """
    Main entry point of the script.
    """
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

    solve_nqueens(n)


if __name__ == "__main__":
    main()
