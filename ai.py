"""
ai.py


This module contains the AI functionality for the tictactoe game.
It holds the ai_move function, which is a wrapper for either the
minimax
"""


from math import inf, sqrt, log
from random import randint
from copy import deepcopy
import time
import game
from main import SetLayout

boards = 0


class Node:
    """
    # Node
    The Node class defines a node in a
    Monte-Carlo Search Tree, with all
    requisite parameters.
    """
    def __init__(self, board, player_id, move):
        self.wins = 0.0
        self.games = 0.0
        self.move = move
        self.board = board
        self.player_id = player_id
        self.children = []



def Evalute(board,player_id,depth):
    winner = game.check_win(board)
    if winner == player_id:  # win
        return 10 + depth
    if winner not in (' ', "draw"):
        return -10 - depth
    if winner == "draw":
        return 0
    if depth == 0:
        return None


def Evalutee(board,player_id):
    rowx,columnx,rowo,columno,diagnoalo,diagnoalx=0
    row,column,diagnoal=0;
    row0= [0, 1, 2, 3,4]
    row1 = [5, 6, 7, 8, 9]
    row2 = [10, 11, 12, 13, 14]
    row3 = [15, 16, 17, 18, 19]
    row4 = [20, 21, 22, 23, 24]

    column0=[0,5,10,15,20]
    column1 = [1, 6, 11, 16, 21]
    column2 = [2, 7, 12, 17, 22]
    column3 = [3, 8, 13, 18, 23]
    column4 = [4, 9, 14, 19, 24]

    diagnoal0 =[0,6,12,18,24]
    diagnoal1 = [1, 7, 13, 19]
    diagnoal2 = [3, 7, 11, 15]
    diagnoal3 = [4, 8, 12, 16,20]
    diagnoal3 = [9, 13, 17, 21]



    for i in range(row0):
        if board[i] == ' ' or board[i] == 'X':
            rowx+=1
            row=1
        if board[i] == 'O' and row ==0 :
            rowo += 1
        row = 0

    for i in range(row1):
        if board[i] == ' ' or board[i] == 'X':
            rowx+=1
            row = 1
        if board[i] == 'O' and row == 0:
            rowo += 1
        row = 0

    for i in range(row2):
         if board[i] == ' ' or board[i] == 'X':
             rowx += 1
             row = 1
         if board[i] == 'O' and row == 0:
             rowo += 1
         row = 0

    for i in range(row3):
         if board[i] == ' ' or board[i] == 'X':
             rowx += 1
             row = 1
         if board[i] == 'O' and row == 0:
             rowo += 1
         row = 0

    for i in range(row4):
         if board[i] == ' ' or board[i] == 'X':
             rowx += 1
             row = 1
         if board[i] == 'O' and row == 0:
             rowo += 1
         row = 0


    for i in range(column0):
        if board[i] == ' ' or board[i] == 'X':
            columnx+=1
            column = 1
        if board[i] == 'O' and column== 0:
             columno += 1
        column = 0

    for i in range(column1):
        if board[i] == ' ' or board[i] == 'X':
            columnx+=1
            column = 1
        if board[i] == 'O' and column == 0:
            columno += 1
        column = 0

    for i in range(column2):  # nextstate
         if board[i] == ' ' or board[i] == 'X':
             columnx += 1
             column = 1
         if board[i] == 'O' and column == 0:
             columno += 1
         column = 0


    for i in range(column3):  # nextstate
         if board[i] == ' ' or board[i] == 'X':
             columnx += 1
             column = 1
         if board[i] == 'O' and column == 0:
             columno += 1
         column = 0


    for i in range(column4):  # nextstate
         if board[i] == ' ' or board[i] == 'X':
             columnx += 1
             column = 1
         if board[i] == 'O' and column == 0:
             columno += 1
         column = 0

    # for i in range(row0): #nextstate
    #     if board[i] == ' ' or board[i] == 'O':
    #         rowo+=1
    # for i in range(row1): #nextstate
    #     if board[i] == ' ' or board[i] == 'O':
    #         rowo+=1
    # for i in range(row2):  # nextstate
    #      if board[i] == ' ' or board[i] == 'O':
    #          rowo += 1
    # for i in range(row3):  # nextstate
    #      if board[i] == ' ' or board[i] == 'O':
    #          rowo += 1
    # for i in range(row4):  # nextstate
    #      if board[i] == ' ' or board[i] == 'O':
    #          rowo += 1
    #
    #
    # for i in range(column0): #nextstate
    #     if board[i] == ' ' or board[i] == 'O':
    #         columno+=1
    # for i in range(column1): #nextstate
    #     if board[i] == ' ' or board[i] == 'O':
    #         columno+=1
    # for i in range(column2):  # nextstate
    #      if board[i] == ' ' or board[i] == 'O':
    #          columno += 1
    # for i in range(column3):  # nextstate
    #      if board[i] == ' ' or board[i] == 'O':
    #          columno += 1
    # for i in range(column4):  # nextstate
    #      if board[i] == ' ' or board[i] == 'O':
    #          columno += 1

    for i in range(diagnoal0):
        if board[i] == ' ' or board[i] == 'O':
            diagnoalo+=1
            diagnoal=1
        if board[i] == 'X' and diagnoal == 0:
            diagnoalo+=1
        diagnoal = 0


    for i in range(diagnoal1):
        if board[i] == ' ' or board[i] == 'O':
            diagnoalo+=1
            diagnoal=1
        if board[i] == 'X' and diagnoal == 0:
            diagnoalo+=1
        diagnoal = 0


    for i in range(diagnoal2):
        if board[i] == ' ' or board[i] == 'O':
            diagnoalo+=1
            diagnoal=1
        if board[i] == 'X' and diagnoal == 0:
            diagnoalo+=1
        diagnoal = 0


    for i in range(diagnoal3):  # nextstate
        if board[i] == ' ' or board[i] == 'O':
            diagnoalo += 1
            diagnoal = 1
        if board[i] == 'X' and diagnoal == 0:
            diagnoalo += 1
        diagnoal = 0


    if player_id == 'O':
       return (rowo+columno+diagnoalo) - (rowx+columnx+diagnoalx)

    if player_id == 'X':
       return (rowx+columnx+diagnoalx) - (rowo+columno+diagnoalo)

def minimax_ab(board, player_id, depth, maximize, alpha=-inf, beta=-inf) -> (int, int):

    winner = game.check_win(board)
    if winner == player_id:#win
        return None, 10+Evalute(board, player_id, depth)
    if winner not in (' ', "full"):
        return None, -10-Evalute(board, player_id, depth)
    if winner == "full":
        return None, 0
    if depth == 0:
        return None, 0


    #Evalute(board, player_id, depth)
    global boards
    boards += 1

    best_move = None
    value = None

    for i in range(25): #nextstate
        if board[i] == ' ':
            board[i] = player_id
            _, value = minimax_ab(board,
                                  'O' if player_id == 'X' else 'X',
                                  depth - 1,
                                  False,
                                  alpha,
                                  beta)
            board[i] = ' '
            if (value is not None
                    and (value > alpha if maximize else value < beta)):
                if maximize:
                    alpha = value
                else:
                    beta = value
                if (alpha != -inf and beta != inf
                    and alpha >= beta if maximize else beta >= alpha):
                    break
                best_move = i

    if maximize:
        return best_move, alpha

    return best_move, beta


def ai_move(board, player_id, algorithm):


    global boards
    boards = 0

    if algorithm == "Easy":

        move, _ = minimax_ab(board, player_id, 3, True)

        if move is None:
            move = randint(0, 24)
            while board[move]!=' ':
                move = randint(0, 24)
            print("raaaaaaaaaaaaaaaaaaaaaa")
            print(move)
        board[move] = player_id
        print(move)
        print("EASY")
        print(f"Calls to minimax_ab: {boards}")
    elif algorithm == "Hard":

        move, _ = minimax_ab(board, player_id, 5, True)

        if move is None:
            move = randint(0, 24)
            while board[move]!=' ':
                move = randint(0, 24)
            print("raaaaaaaaaaaaaaaaaaaaaa")
            print(move)
        board[move] = player_id
        print("HARD")
        print(f"Calls to minimax_ab: {boards}")

