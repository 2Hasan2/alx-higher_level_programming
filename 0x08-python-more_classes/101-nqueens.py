#!/usr/bin/python3

""" solve the N queens problem """

import sys


def printSolution(board):
    """ print the solution """
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


def isSafe(board, row, col):
    """ check if the position is safe """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solveNQUtil(board, col):
    """ solve the N queens problem """
    if col >= len(board):
        printSolution(board)
        return True
    for i in range(len(board)):
        if isSafe(board, i, col):
            board[i][col] = 1
            solveNQUtil(board, col + 1)
            board[i][col] = 0
    return False


def solveNQ():
    """ solve the N queens problem """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    board = [[0 for j in range(n)] for i in range(n)]
    solveNQUtil(board, 0)


if __name__ == "__main__":
    solveNQ()
