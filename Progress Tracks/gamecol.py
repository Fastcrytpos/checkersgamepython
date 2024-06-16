import random

ansi_black = "\u001b[30m"
ansi_red = "\u001b[31m"
ansi_ansi_black = "\u001b[32m"
ansi_yellow = "\u001b[33m"
ansi_blue = "\u001b[34m"
ansi_magenta = "\u001b[35m"
ansi_cyan = "\u001b[36m"
ansi_white = "\u001b[37m"
ansi_reset = "\u001b[0m"

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
            print(ansi_magenta + f" {col} ", end=" ")
        print()
        print(" +---+---+---+---+---+---+---+---+")
        for row in range(8):
            print(ansi_blue + f"{row}", end="|")
            for col in range(8):
                piece = self.board[row][col]
                
                print(f" {piece} |", end="")
            print(ansi_magenta + f"{row} ") # Print the row number again at the end of the row
            print(" +---+---+---+---+---+---+---+---+") 
        print(" ", end=" ")
        for col in range(8):
            print(ansi_blue + f" {col} " , end=" ")
        print()
        print()
        player_pieces = sum(row.count('p') + row.count('K') for row in self.board)
        computer_pieces = sum(row.count('c') + row.count('Q') for row in self.board)
        print(f"Player Pieces:{ansi_blue} {player_pieces}" )
        print(f"Computer Pieces:{ansi_cyan} {computer_pieces}" )

    def king(self, piece):
        return piece in [ansi_yellow+'K', 'Q']

    def move_piece(self, start_row, start_col, end_row, end_col, player):
        piece = self.board[start_row][start_col]
        captured_piece_pos = None  # Initialize captured piece position

        #This allows both the player and computer to move its kings'
        if player == 'p':
            if piece not in ['p', 'K']:
                print(ansi_red+ f"Invalid move. You can only move 'p' or 'K' pieces.")
                return False, captured_piece_pos
        elif player == 'c':
            if piece not in ['c', 'Q']:
                print(ansi_red + "Invalid move. You can only move 'c' or 'Q' pieces.")
                return False, captured_piece_pos

        if piece == ' ':
            print(ansi_red+"No piece at starting position.")
            return False, captured_piece_pos

        # Normal pieces move in one direction, kings can move in any direction
        if not self.king(piece):
            if player == 'p' and end_row > start_row:  # Player 'p' moves upwards
                print(ansi_red+"Invalid move. Only move upwards.")
                return False, captured_piece_pos
            if player == 'c' and end_row < start_row:  # Computer 'c' moves downwards
                print(ansi_red+"Invalid move. Only move downwards.")
                return False, captured_piece_pos

        if abs(start_row - end_row) != abs(start_col - end_col):
            print(ansi_yellow+"Invalid move. Moves must be diagonal.")
            return False, captured_piece_pos
        if abs(start_row - end_row) > 2:
            print(ansi_yellow+"Invalid move. Can only move one or two spaces.")
            return False, captured_piece_pos
        if abs(start_row - end_row) == 2:
            mid_row = (start_row + end_row) // 2
            mid_col = (start_col + end_col) // 2
            if self.board[mid_row][mid_col] == ' ':
                print(ansi_red+"Invalid move. Must jump over opponent's piece.")
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

        print(ansi_yellow+"Valid move!")
        return True, captured_piece_pos  # Return captured piece position

    def quit_game(self):
        print(ansi_red+"Game quit by user.")  # Added quit game
        exit()

    def surrender_game(self):
        print(ansi_red+"Player Surrendered the game. Buree kabisaa!!!")  # Added the surrender game
        exit()

def main():
    game = Checkers()
    print(ansi_magenta+"        ""WELCOME TO CHECKERS, HERE ARE GAME RULES")
    print(ansi_blue+F"1. To move a piece, enter the  X and  Y coordinates of the piece seperated by a space.")
    print(ansi_blue+"2. For example: '2 1 3 2' moves a piece occupying cordinate 2 1 from row 2, col 1 to row 3, col 2.")
    print(ansi_blue+f"3. Press  Q to quit the game.")
    print(ansi_blue+f"4. Press  S to surrender and restart the game.")
    input("Press Enter to start the game...")
    while True:
        game.print_board()
        start_input = input(ansi_white+"Enter start position (row col): ").split()
        if start_input[0].lower() == 'q':
            game.quit_game()
        if start_input[0].lower() == 's':
            game.surrender_game()
            continue
        end_input = input(ansi_white+"Enter end position (row col): ").split()

        if len(start_input) != 2 or len(end_input) != 2:
            print(ansi_red+"Invalid input. Please enter row and column separated by space.")
            continue
        try:
            start_row, start_col = map(int, start_input)
            end_row, end_col = map(int, end_input)
        except ValueError:
            print(ansi_red +"Invalid input. Please enter integers.")
            continue
        if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
            print(ansi_white+"Invalid input. Position out of range.")
            continue
        valid_move, captured_piece_pos = game.move_piece(start_row, start_col, end_row, end_col, 'p')
        if not valid_move:
            print(ansi_red+"Invalid move. Please try again.")
            continue
        if captured_piece_pos:
            print(ansi_magenta+f"PLAYER  captured Piece at position {captured_piece_pos} and removed.")

        # Check for win condition
        x_count = sum(row.count('p') for row in game.board)
        o_count = sum(row.count('c') for row in game.board)
        if x_count == 0:
            print(ansi_magenta+"Congratulations! 'c' wins!")
            break
        elif o_count == 0:
            print(ansi_magenta+"Congratulations! 'p' wins!")
            break

        # Computer's move
        available_moves = []
        for row in range(8):
            for col in range(8):
                if game.board[row][col] == 'c':
                    # Normal moves for 'c'
                    if row + 1 < 8 and col - 1 >= 0 and game.board[row + 1][col - 1] == ' ':
                        available_moves.append((row, col, row + 1, col - 1))
                    if row + 1 < 8 and col + 1 < 8 and game.board[row + 1][col + 1] == ' ':
                        available_moves.append((row, col, row + 1, col + 1))
                    # Jump moves for 'c'
                    if row + 2 < 8 and col - 2 >= 0 and game.board[row + 1][col - 1] == 'p' and game.board[row + 2][col - 2] == ' ':
                        available_moves.append((row, col, row + 2, col - 2))
                    if row + 2 < 8 and col + 2 < 8 and game.board[row + 1][col + 1] == 'p' and game.board[row + 2][col + 2] == ' ':
                        available_moves.append((row, col, row + 2, col + 2))
                elif game.board[row][col] == 'Q':
                    # Moves for 'Q' (king)
                    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                        if 0 <= row + dr < 8 and 0 <= col + dc < 8 and game.board[row + dr][col + dc] == ' ':
                            available_moves.append((row, col, row + dr, col + dc))
                        if 0 <= row + 2*dr < 8 and 0 <= col + 2*dc < 8 and game.board[row + dr][col + dc].lower() == 'p' and game.board[row + 2*dr][col + 2*dc] == ' ':
                            available_moves.append((row, col, row + 2*dr, col + 2*dc))

        if available_moves:
            capture_moves = [move for move in available_moves if abs(move[0] - move[2]) == 2]
            if capture_moves:
                comp_move = random.choice(capture_moves)
            else:
                comp_move = random.choice(available_moves)
            game.move_piece(comp_move[0], comp_move[1], comp_move[2], comp_move[3], 'c')
            if abs(comp_move[0] - comp_move[2]) == 2:
                captured_piece_row = (comp_move[0] + comp_move[2]) // 2
                captured_piece_col = (comp_move[1] + comp_move[3]) // 2
                print(ansi_magenta+"Computer captured a piece at position ({captured_piece_row}, {captured_piece_col}) and moved from ({comp_move[0]}, {comp_move[1]}) to ({comp_move[2]}, {comp_move[3]}).")
            else:
                print(ansi_blue+f"Computer moved from ({comp_move[0]}, {comp_move[1]}) to ({comp_move[2]}, {comp_move[3]}).")
        else:
            print(ansi_blue+"No available moves for the computer. YOU WIN!!!")
            break

if __name__ == "__main__":
    main()
