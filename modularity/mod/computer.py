#from constants import *
import random

class ComputerMove:
    @staticmethod
    def get_computer_move(board):
        available_moves = []
        # Iterate over each cell in the board
        for start_row in range(8):
            for start_col in range(8):
                if board[start_row][start_col] == 'c':
                    piece=board[start_row][start_col]
                    # Normal moves for 'c': moving one step diagonally forward left or right
                    if start_row + 1 < 8 and start_col - 1 >= 0 and board[start_row + 1][start_col - 1] == ' ':
                        available_moves.append(
                            (piece,start_row, start_col, start_row + 1, start_col - 1))
                    if start_row + 1 < 8 and start_col + 1 < 8 and board[start_row + 1][start_col + 1] == ' ':
                        available_moves.append(
                            (piece,start_row, start_col, start_row + 1, start_col + 1))

                    # Jump moves for 'c': capturing opponent's piece by jumping over it
                    if start_row + 2 < 8 and start_col - 2 >= 0 and board[start_row + 1][start_col - 1] == 'p' and board[start_row + 2][start_col - 2] == ' ':
                        available_moves.append(
                            (piece,start_row, start_col, start_row + 2, start_col - 2))
                    if start_row + 2 < 8 and start_col + 2 < 8 and board[start_row + 1][start_col + 1] == 'p' and board[start_row + 2][start_col + 2] == ' ':
                        available_moves.append(
                            (piece,start_row, start_col, start_row + 2, start_col + 2))

        # If there are available moves, choose a random move
        if available_moves:
            capture_moves = [move for move in available_moves if abs(move[1] - move[3]) == 2]
            if capture_moves:
                # Choose a random capture move
                return random.choice(capture_moves)
            else:
                # Choose a random non-capture move
                return random.choice(available_moves)
        else:
            return None  # Return None if no moves are available