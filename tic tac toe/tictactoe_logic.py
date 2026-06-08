import math

# --- Game Board ---
# The board is represented as a list of 9 elements.
# Each element can be 'X', 'O', or a space ' ' for empty.
# Indices:
# 0 | 1 | 2
# --+---+--
# 3 | 4 | 5
# --+---+--
# 6 | 7 | 8

def create_board():
    """Initializes and returns an empty Tic-Tac-Toe board."""
    return [' ' for _ in range(9)]

def display_board_console(board):
    """
    Prints the current state of the Tic-Tac-Toe board to the console.
    This is primarily for debugging or console-only versions.
    """
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

# --- Game Logic ---

def check_win(board, player):
    """
    Checks if the given player has won the game.
    Args:
        board (list): The current game board.
        player (str): The player ('X' or 'O') to check for a win.
    Returns:
        bool: True if the player has won, False otherwise.
    """
    win_conditions = [
        # Rows
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        # Columns
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        # Diagonals
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw(board):
    """
    Checks if the game is a draw (no empty spaces left).
    Args:
        board (list): The current game board.
    Returns:
        bool: True if the game is a draw, False otherwise.
    """
    return ' ' not in board and not check_win(board, 'X') and not check_win(board, 'O')

def is_game_over(board):
    """
    Checks if the game has ended (either a win or a draw).
    Args:
        board (list): The current game board.
    Returns:
        bool: True if the game is over, False otherwise.
    """
    return check_win(board, 'X') or check_win(board, 'O') or check_draw(board)

# --- AI (Minimax Algorithm) ---

def evaluate(board):
    """
    Evaluates the current state of the board.
    Returns:
        int: +10 if AI ('O') wins, -10 if Human ('X') wins, 0 for draw or ongoing.
    """
    if check_win(board, 'O'):
        return 10
    elif check_win(board, 'X'):
        return -10
    else:
        return 0

def minimax(board, depth, is_maximizing_player):
    """
    The Minimax algorithm to find the optimal move.
    Args:
        board (list): The current game board.
        depth (int): The current depth in the game tree.
        is_maximizing_player (bool): True if it's the AI's turn (maximizing player),
                                     False if it's the human's turn (minimizing player).
    Returns:
        int: The optimal score for the current board state.
    """
    score = evaluate(board)

    # Base cases: If game is over, return the score
    if score == 10:  # AI wins
        return score - depth # Subtract depth to prefer faster wins
    if score == -10: # Human wins
        return score + depth # Add depth to prefer slower losses (or force faster loss for opponent)
    if check_draw(board):
        return 0

    # Recursive cases
    if is_maximizing_player: # AI's turn (maximizing player)
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O' # Make a move
                best_score = max(best_score, minimax(board, depth + 1, False))
                board[i] = ' ' # Undo the move
        return best_score
    else: # Human's turn (minimizing player)
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X' # Make a move
                best_score = min(best_score, minimax(board, depth + 1, True))
                board[i] = ' ' # Undo the move
        return best_score

def find_best_move(board):
    """
    Finds the best move for the AI ('O') using the Minimax algorithm.
    Args:
        board (list): The current game board.
    Returns:
        int: The index of the best move.
    """
    best_score = -math.inf
    best_move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O' # Try this move
            # Call minimax for the minimizing player (human)
            move_score = minimax(board, 0, False)
            board[i] = ' ' # Undo the move

            if move_score > best_score:
                best_score = move_score
                best_move = i
    return best_move

