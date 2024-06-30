from constants import *

class Checkers:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.initialize_board()

    def initialize_board(self):
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.board[row][col] = 'c'

        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.board[row][col] = 'p'

    def print_board(self):
        print()
        print()
        print(" ", end=" ")
        for col in range(8):
            print(ansi_magenta + f" {col} " + ansi_reset, end=" ")
        print()
        print(" +---+---+---+---+---+---+---+---+")
        for row in range(8):
            print(f"{ansi_magenta}{row}{ansi_reset}", end="|")
            for col in range(8):
                piece = self.board[row][col]
                if piece == 'p':
                    piece = ansi_yellow + piece + ansi_reset
                elif piece == 'c':
                    piece = ansi_green + piece + ansi_reset
                print(f" {piece} |", end="")
            print(ansi_magenta + f"{row} {ansi_reset} ")
            print(" +---+---+---+---+---+---+---+---+")
        for col in range(8):
            print(f" {ansi_magenta}  {col}{ansi_reset}",end="")
        print()
        print()
        #calculate the pieces left, both computer and player
        player_pieces = sum(row.count('p') + row.count('K') for row in self.board)
        computer_pieces = sum(row.count('c') + row.count('Q') for row in self.board)
        print(f"{ansi_green}Player Pieces Left:{ansi_reset}{ansi_yellow} {player_pieces}{ansi_reset}")
        print(f"{ansi_green}Computer Pieces Left: {ansi_reset}{ansi_magenta} {computer_pieces}{ansi_reset}")

    def king(self, piece):
        return piece in ['K', 'Q']

    def move_piece(self, start_row, start_col, end_row, end_col, player):
        piece = self.board[start_row][start_col]
        captured_piece_pos = None  # Initialize captured piece position

        # This allows both the player and computer to move its kings'
        if player == 'p':
            if piece not in ['p', 'K']:
                print(ansi_red + f"Invalid move. You can only move 'p' or 'K' pieces.")
                return False, captured_piece_pos
        elif player == 'c':
            if piece not in ['c', 'Q']:
                print(ansi_red + f"Invalid move. You can only move 'c' or 'Q' pieces.")
                return False, captured_piece_pos

        # CANNOT MOVE TO OCCUPIED LOCATION
        if self.board[end_row][end_col] != ' ':
            print(ansi_red + "Invalid move. Cannot move to occupied location😞😞.")
            return False, captured_piece_pos

        # Normal pieces move in one direction, kings can move in any direction
        if not self.king(piece):
            if player == 'p' and end_row > start_row:  # Player 'p' moves upwards
                print(ansi_red + "Invalid move. Only move upwards.")
                return False, captured_piece_pos
            if player == 'c' and end_row < start_row:  # Computer 'c' moves downwards
                print(ansi_red + "Invalid move. Only move downwards.")
                return False, captured_piece_pos

        if abs(start_row - end_row) != abs(start_col - end_col):
            print(ansi_red + "Invalid move. Moves must be diagonal😞.")
            return False, captured_piece_pos
        if abs(start_row - end_row) > 2:
            print(ansi_red + "Invalid move. Can only move one or two spaces.")
            return False, captured_piece_pos
        if abs(start_row - end_row) == 2:
            mid_row = (start_row + end_row) // 2
            mid_col = (start_col + end_col) // 2
            if self.board[mid_row][mid_col] == ' ':
                print(ansi_red + "Invalid move. Must jump over opponent's piece.")
                return False, captured_piece_pos
            # not to capture yourself
            if self.board[mid_row][mid_col] == player:
                print(ansi_red + "invalid.Cannot capture your MATE 😞!!")
                return False, captured_piece_pos
            captured_piece_pos = (mid_row, mid_col)  # Set captured piece position
            self.board[mid_row][mid_col] = ' '
        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = ' '

        # Check for promotion
        if player == 'p' and end_row == 0:
            self.board[end_row][end_col] = 'K'
        elif player == 'c' and end_row == 7:
            self.board[end_row][end_col] = 'Q'

        print("Valid move!")
        return True, captured_piece_pos  # Return captured piece position

    def has_capture_move(self, row, col, player):
        if player == 'p' or self.board[row][col] == 'K':
            directions = [(-1, -1), (-1, 1)]
        elif player == 'c' or self.board[row][col] == 'Q':
            directions = [(1, -1), (1, 1)]

        for dr, dc in directions:
            if 0 <= row + 2 * dr < 8 and 0 <= col + 2 * dc < 8:
                if self.board[row + dr][col + dc] in ['c', 'p'] and self.board[row + dr][col + dc] != player and self.board[row + 2 * dr][col + 2 * dc] == ' ':
                    return True
        return False
