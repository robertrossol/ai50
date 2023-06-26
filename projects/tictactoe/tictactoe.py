"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    def count_sym(board, sym):
      sym_count = 0
      for row in board:
        sym_count += row.count(sym)
      return sym_count
    
    if count_sym(board, "X") <= count_sym(board, "O"):
      return X
    else:
      return O
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = list() 
    for x in range(0, len(board)):
       for y in range(0, len(board[x])):
          if board[x][y] == None:
            moves.append((x, y)) 
    return moves
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board[action[0]][action[1]] = player(board)
    return board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winning_combinations = ([(0,0), (0,1), (0,2)],  [(1,0), (1,1), (1,2)],  [(2,0), (2,1), (2,2)],  [(0,0), (1,0), (2,0)],  [(0,1), (1,1), (2,1)],  [(0,2), (1,2), (2,2)],  [(0,0), (1,1), (2,2)],  [(0,2), (1,1), (2,0)])

    for combo in winning_combinations:
      row = [board[x][y] for x, y in combo]
      if all(space == "X" for space in row):
        return X
      elif all(space == "O" for space in row):
        return O
    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # row = [board[x][y] for x, y in combo]
    if not winner(board):
      for row in board:
        if any(space == None for space in row):
          return False
    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner = winner(board)
    if winner == X:
       return 1
    elif winner == O:
       return -1
    else:
       return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # !temporary! returns first available action
    return actions(board)[0]
    raise NotImplementedError
