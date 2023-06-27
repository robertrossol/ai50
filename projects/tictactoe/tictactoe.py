"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
CHECKED = 0


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
    temp_board = copy.deepcopy(board)
    temp_board[action[0]][action[1]] = player(temp_board)
    return temp_board
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
    x = winner(board)
    if x == X:
       return 1
    elif x == O:
       return -1
    else:
       return 0
    raise NotImplementedError


def minimax(board):
  """
    Returns the optimal action for the current player on the board.
  """
    # !temporary! returns first available action
    # return actions(board)[0]
  # player = player(board)
  # moves = actions(board)
    # goal = 0

  def max_value(board):
     global CHECKED
     CHECKED += 1
     best_move = tuple()
     if terminal(board):
        return [utility(board), best_move]
     v = -100
     for move in actions(board):
        current_v = v
        y = min_value(result(board, move))[0]
        if y < v: break
        v = max(v, y)
        if v != current_v:
          best_move = move
        if v == 1 : break
     return [v, best_move]

  def min_value(board):
     global CHECKED
     CHECKED += 1
     best_move = tuple()
     if terminal(board):
        return [utility(board), best_move]
     v = 100
     for move in actions(board):
        current_v = v
        y = max_value(result(board, move))[0]
        if y > v : break
        v = min(v, y)
        if v != current_v:
          best_move = move
        if v == -1 : break
     return [v, best_move]

  if player(board) == X:
    return max_value(board)[-1]

  if player(board) == O:
    return min_value(board)[-1]

  # return best_move
  raise NotImplementedError
