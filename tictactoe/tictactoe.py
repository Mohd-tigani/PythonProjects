"""
Tic Tac Toe Player
"""

import math
import copy

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
    count_X=0
    count_O=0
    for i in range( len( board ) ):
        for j in range( len( board[i] ) ):
            if board[i][j] == X:
                count_X+=1
            elif board[i][j]==O:
                count_O+=1

    if count_X>count_O:#player O turn when player X is 1 move ahead of O
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    board_1 = []

    for i in range( len( board ) ):
        for j in range( len( board[i] ) ):
            if board[i][j] == EMPTY:
                board_1.append( (i, j) )#store row & column values

    board_1 = tuple( board_1 )#convert list to a tuple
    possible_moves = set( board_1 )#create set of possible moves
    return possible_moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    board_copy = copy.deepcopy( board )  # create copy of board with no reference
    if board_copy[action[0]][action[1]]!=EMPTY:
        raise Exception("Not a valid action")

    board_copy[action[0]][action[1]]=player(board)

    return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range( len( board ) ):
        for j in range( len( board[i] ) ):
            if board[i][0] == X and board[i][1] == X and board[i][2] == X:#check horizontal
                return X
            elif board[0][j] == X and board[1][j] == X and board[2][j] == X:#check vertically
                return X
            elif board[0][0] == X and board[1][1] == X and board[2][2] == X:#check diagnonal
                return X
            elif board[0][2] == X and board[1][1] == X and board[2][0] == X:#check diagonal
                return X


    for i in range( len( board ) ):
        for j in range( len( board[i] ) ):
            if board[i][0] == O and board[i][1] == O and board[i][2] == O:#check horizontal
                return O
            elif board[0][j] == O and board[1][j] == O and board[2][j] == O:#check vertically
                return O
            elif board[0][0] == O and board[1][1] == O and board[2][2] == O:#check diagonal
                return O
            elif board[0][2] == O and board[1][1] == O and board[2][0] == O:#check diagonal
                return O

    return None
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    count = 0
    for i in range( len( board ) ):
        for j in range( len( board[i] ) ):
            if board[i][j] != EMPTY:
                count += 1  # count number of filled spaces, max is 9
    if winner(board) or count==9:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal( board ):
        return None

    optimal_action=None
    if player( board ) == X:
        v = -math.inf
        for action in actions( board ):
            min = min_value( result( board, action ) )
            if v < min:
                v = min
                optimal_action = action

    elif player( board ) == O:
        v = math.inf
        for action in actions( board ):
            max = max_value( result( board, action ) )
            if v > max:
                v = max
                optimal_action = action

    return optimal_action

def max_value(board):

    v = -math.inf#negative infinity

    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):

    v = math.inf#positive infinity
    if terminal( board ):
        return utility( board )

    for action in actions( board ):
        v = min( v, max_value( result( board, action ) ) )
    return v


