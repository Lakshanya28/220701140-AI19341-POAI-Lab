def minimax(board, depth, is_maximizing):
    # Base case: Check for terminal states (win, loss, or draw)
    winner = check_winner(board)
    if winner == "X":  # Maximizing player wins
        return 10 - depth
    elif winner == "O":  # Minimizing player wins
        return depth - 10
    elif is_draw(board):  # Draw
        return 0

    # Maximizing player's turn
    if is_maximizing:
        best_score = float("-inf")
        for move in get_available_moves(board):
            board[move] = "X"  # Simulate move
            score = minimax(board, depth + 1, False)
            board[move] = " "  # Undo move
            best_score = max(best_score, score)
        return best_score

    # Minimizing player's turn
    else:
        best_score = float("inf")
        for move in get_available_moves(board):
            board[move] = "O"  # Simulate move
            score = minimax(board, depth + 1, True)
            board[move] = " "  # Undo move
            best_score = min(best_score, score)
        return best_score


# Helper functions
def check_winner(board):
    # Winning combinations
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                            (0, 4, 8), (2, 4, 6)]             # Diagonals
    for (i, j, k) in winning_combinations:
        if board[i] == board[j] == board[k] and board[i] != " ":
            return board[i]  # Return the winner ("X" or "O")
    return None


def is_draw(board):
    return " " not in board


def get_available_moves(board):
    return [i for i, spot in enumerate(board) if spot == " "]


# Example usage: Simulate one step in a game
board = ["X", "O", "X", " ", "O", " ", " ", " ", " "]  # Example board
best_move = None
best_score = float("-inf")

for move in get_available_moves(board):
    board[move] = "X"  # Maximizing player makes a move
    score = minimax(board, 0, False)  # Call minimax for the minimizing player
    board[move] = " "  # Undo move
    if score > best_score:
        best_score = score
        best_move = move

print(f"Best move for 'X' is at position {best_move} with a score of {best_score}.")
