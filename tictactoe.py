"""
tictactoe.py
Dylan Palmieri
2021-02-07
main function for 5x5 Tic-Tac-Toe

This module contains the main UI loop for the tictactoe module.

It holds the read_file, replay_game, and main functions.
"""


from time import sleep
from game import game
from game import print_board


# def read_file(board):
#     """
#     This function loads the last board state from a file,
#     specified by an absolute path.
#     """
#     path = input("Please enter the absolute path of the game file: ")
#     state = ""
#     with open(path, "r") as fin:
#         line = ""
#         for line in fin:
#             pass
#         state = line
#
#     for i in range(25):
#         board[i] = state[i]
#
#     return path
#
#
# def replay_game():
#     """
#     This function reads a board state from a file, and calls the
#     game.print_board function to print the board state.
#     """
#     path = input("Please enter the absolute path of the game file: ")
#     board = []
#     for _ in range(25):
#         board.append(' ')
#     with open(path, "r") as fin:
#         for line in fin:
#             for i in range(25):
#                 board[i] = line[i]
#             print_board(board)
#             sleep(1)
