#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    """Check if it's safe to place a queen in a given position."""
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    """Solve the N Queens problem and print solutions."""

    # Check for valid input
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize an empty N x N chessboard
    board = [[0 for _ in range(N)] for _ in range(N)]
    sols = []

    def solve_util(col):
        """Utility function to solve
        the N Queens problem using backtracking."""
        if col == N:
            sols.append([[i, row.index(1)] for i, row in enumerate(board)])
            return True

        res = False
        for i in range(N):
            if is_safe(board, i, col, N):
                board[i][col] = 1
                res = solve_util(col + 1) or res
                board[i][col] = 0

        return res

    solve_util(0)

    for solution in sols:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solve_nqueens(sys.argv[1])
