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
    """
    Returns player who has the next turn on a board.
    """
    count_X = 0
    count_O = 0
    
    for row in board:
        count_X += row.count(X)
        count_O += row.count(O)
    
    if count_X > count_O:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = [row[:] for row in board]
    i, j = action
    current_player = player(board)
    
    if new_board[i][j] is not EMPTY:
        raise Exception("Invalid action")
    
    new_board[i][j] = current_player
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player in [X, O]:
        # Check rows
        for row in board:
            if row.count(player) == 3:
                return player
        
        # Check columns
        for j in range(len(board)):
            if [board[i][j] for i in range(len(board))].count(player) == 3:
                return player
        
        # Check diagonals
        if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
           (board[0][2] == player and board[1][1] == player and board[2][0] == player):
            return player
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(all(cell is not EMPTY for cell in row) for row in board)
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)
    
    if current_player == X:
        max_value_action = max_value(board)
        return max_value_action[1]
    else:
        min_value_action = min_value(board)
        return min_value_action[1]
 
    
def max_value(board):
    if terminal(board):
        return utility(board), None
    
    v = float('-inf')
    best_action = None
    
    for action in actions(board):
        new_board = result(board, action)
        min_value_result = min_value(new_board)
        
        if min_value_result[0] > v:
            v = min_value_result[0]
            best_action = action
    
    return v, best_action


def min_value(board):
    if terminal(board):
        return utility(board), None
    
    v = float('inf')
    best_action = None
    
    for action in actions(board):
        new_board = result(board, action)
        max_value_result = max_value(new_board)
        
        if max_value_result[0] < v:
            v = max_value_result[0]
            best_action = action
    
    return v, best_action
