#!/usr/bin/python3

""" The N queens puzzle is the challenge of placing N non-attacking queens on
an N×N chessboard. Write a program that solves the N queens problem."""
import sys


def makeBoard(queenN):
    """Make Board N x N"""
    board = []
    [board.append([]) for i in range(queenN)]
    [row.append('.') for i in range(queenN) for row in board]
    return board


def isPossibe(board, queenN, row, col):
    """check for the col"""
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    """check for upper left"""
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 'Q':
            return False
    """check for upper right"""
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, queenN)):
        if board[i][j] == 'Q':
            return False

    return True


sol = []


def solve(board, queenN, row):
    """solve the problem using backtrack"""
    if row == queenN:
        sol1 = []
        for i in range(queenN):
            for j in range(queenN):
                if board[i][j] == 'Q':
                    sol1.append([i, j])
        sol.append(sol1)
        return sol

    for i in range(queenN):
        if isPossibe(board, queenN, row, i):
            board[row][i] = 'Q'
            solve(board, queenN, row + 1)
            board[row][i] = '.'

    return sol


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    nQueen = int(sys.argv[1])
    board = makeBoard(nQueen)
    solution = solve(board, nQueen, 0)
    for sol in solution:
        print(sol)
