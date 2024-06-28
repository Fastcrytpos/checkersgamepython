from constants import *
import random

class ComputerMove:
    @staticmethod
    def get_computer_move(board):
        available_moves = []
        # Iterate over each cell in the board
        for print_rows in range(8):
            for print_column in range(8):
                if board[print_rows][print_column] == 'c':
                    # Normal moves for 'c': moving one step diagonally forward left or right
                    if print_rows + 1 < 8 and print_column - 1 >= 0 and board[print_rows + 1][print_column - 1] == ' ':
                        available_moves.append(
                            (print_rows, print_column, print_rows + 1, print_column - 1))
                    if print_rows + 1 < 8 and print_column + 1 < 8 and board[print_rows + 1][print_column + 1] == ' ':
                        available_moves.append(
                            (print_rows, print_column, print_rows + 1, print_column + 1))

                    # Jump moves for 'c': capturing opponent's piece by jumping over it
                    if print_rows + 2 < 8 and print_column - 2 >= 0 and board[print_rows + 1][print_column - 1] == 'p' and board[print_rows + 2][print_column - 2] == ' ':
                        available_moves.append(
                            (print_rows, print_column, print_rows + 2, print_column - 2))
                    if print_rows + 2 < 8 and print_column + 2 < 8 and board[print_rows + 1][print_column + 1] == 'p' and board[print_rows + 2][print_column + 2] == ' ':
                        available_moves.append(
                            (print_rows, print_column, print_rows + 2, print_column + 2))

                    # Crown (promotion) for 'c': if 'c' piece reaches the last row, promote to 'Q'
                    if print_rows == 6 and board[print_rows][print_column] == 'c':
                        available_moves.append((print_rows, print_column, 7, print_column))
        # If there are available moves, choose a random move
        if available_moves:
            capture_moves = [move for move in available_moves if abs(
                move[0] - move[2]) == 2]
            if capture_moves:
                # Choose a random capture move
                return random.choice(capture_moves)
            else:
                # Choose a random non-capture move
                return random.choice(available_moves)
        else:
            return None  # Return None if no moves are available