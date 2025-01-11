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
    # Declaring X and O counts
    x_count = 0
    o_count = 0

    # Looping the board
    # Looping the rows
    for row in board:

        # Looping the columns
        for col in row:

            # If value in that position is X
            # Then plus one in x_count
            if col == X:
                x_count += 1

            # If value in that position is O
            # Then plus one in o_count
            elif col == O:
                o_count += 1

    # If there are more X in the board,
    # Then return O
    if x_count > o_count:
        return O

    # Else return X
    else:
        return X            


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Creating a empty list for all posibles actions
    posible_worlds = list()
    # Createing a board deep copy
    board_copy = copy.deepcopy(board)

    # Looping the length of rows
    for row in len(board):
        # Looping the lenght of columns
        for col in len(row):
            
            # If on this (row,col) is empty
            # Then add this coordenate to posible_worlds
            if board_copy[row][col] == EMPTY:
                posible_worlds.append((row,col))

    # Finally return all the actions
    return posible_worlds


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Verify if action input position is not taken
    if board[action[0]][action[1]] != EMPTY:
        # If, raise and exception
        raise Exception("Action not valid")

    # Create new board
    new_board = copy.deepcopy(board)
    # Get the player that have to move
    current_player = player(new_board)
    # Put the player on action input position
    new_board[action[0]][action[1]] = current_player
    # Return the new board
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    win_positions = [
        # Horizontally winner positions
        [(0,0),(0,1),(0,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],
        # Vertically winner positions
        [(0,0),(1,0),(2,0)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,2),(2,2)],
        # Diagonally winner positions
        [(0,0),(1,1),(2,2)],
        [(2,0),(1,1),(0,2)]
    ]

    for position in win_positions:
        # Create a number = 0
        # For compare after looping the positions
        n = 0

        # Looping each position
        for row, col in position:

            # If coordenate is X, then n + 1
            if board[row][col] == X:
                n += 1
            # If coordenate is O, then n - 1
            elif board[row][col] == O:
                n -= 1
        

        # If n is 3, then return X
        if n == 3:
            return X

        # If n is -3, then return O
        elif n == -3:
            return O

        # Else return None
        else:
            return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Get the posible winner
    posible_winner = winner(board)

    # Defining a count variable in 0
    positions_taken = 0
    #Looping the rows of the board
    for row in board:
        # Looping the columns
        for col in row:

            # If in this position (row,col) is empty
            # Then add 1 to the count variable
            if board[row][col] != EMPTY:
                positions_taken += 1


    # If there is a winner or all fields are taken
    # Then return True
    if posible_winner == X or posible_winner == O or positions_taken == 9:
        return True

    # Else return False
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Get the posible winner
    winner_player = winner(board)

    # If that winner is X, then return 1
    if winner_player == X:
        return 1

    # If that winner is O, then return -1
    elif winner_player == O:
        return -1

    # Else return 0
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
