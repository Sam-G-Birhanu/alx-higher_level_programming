#!/usr/bin/python3
"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
Example:
    $ ./101-nqueens.py N
N must be an integer greater than or equal to 4.
Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.
Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def initialize_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = [[' '] * n for _ in range(n)]
    return board


def deepcopy_board(board):
    """Return a deepcopy of a chessboard."""
    return [row[:] for row in board]


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def mark_unavailable(board, row, col):
    """Mark unavailable spots on a chessboard.
    All spots where non-attacking queens can no
    longer be placed are marked as unavailable.
    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last placed.
        col (int): The column where a queen was last placed.
    """
    n = len(board)
    # Mark all forward spots as unavailable
    for c in range(col + 1, n):
        board[row][c] = "x"
    # Mark all backward spots as unavailable
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # Mark all spots below as unavailable
    for r in range(row + 1, n):
        board[r][col] = "x"
    # Mark all spots above as unavailable
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # Mark all spots diagonally down to the right as unavailable
    for r, c in zip(range(row + 1, n), range(col + 1, n)):
        board[r][c] = "x"
    # Mark all spots diagonally up to the left as unavailable
    for r, c in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        board[r][c] = "x"
    # Mark all spots diagonally up to the right as unavailable
    for r, c in zip(range(row - 1, -1, -1), range(col + 1, n)):
        board[r][c] = "x"
    # Mark all spots diagonally down to the left as unavailable
    for r, c in zip(range(row + 1, n), range(col - 1, -1, -1)):
        board[r][c] = "x"


def solve_nqueens(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.
    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for col in range(len(board)):
        if board[row][col] == " ":
            tmp_board = deepcopy_board(board)
            tmp_board[row][col] = "Q"
            mark_unavailable(tmp_board, row, col)
            solutions = solve_nqueens(tmp_board, row + 1,
                                      queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = initialize_board(int(sys.argv[1]))
    solutions = solve_nqueens(board, 0, 0, [])
    for sol in solutions:
        print(sol)
