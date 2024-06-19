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
ansi_green = "\033[92m"

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

def main():
    
    game = Checkers()
    print()
    print(ansi_magenta + "***************************************************************************************")
    print("                                WELCOME TO CHECKERS!")
    print("***************************************************************************************" + ansi_reset)

    print()
    print(ansi_green + "1. To move a piece, enter the  X and  Y coordinates of the piece separated by a space.")
    print("2. For example: '5 0 4 1' moves a piece from row 5, col 0 to row 4, col 1.")
    print("3. Press 'Q' to quit the game.")
    print("4. Press 'S' to surrender and restart the game.")
    input("5. Press Enter to start the game..." + ansi_reset)

    while True:
        game.print_board()
        player_turn = True

        while player_turn:
            while True:
                start_input = input(ansi_green + "Enter start position (row col): ").strip().split()
                if not start_input:
                    print(ansi_red + "Invalid input. Please enter only two integers separated by a space.")
                    continue
                if start_input[0].lower() == 'q':
                    print(ansi_red+"plAYER HAS QUITE 😞😞")
                    exit()
                    
                if start_input[0].lower() == 's':
                    print("Player Surrendered the game.😞😞 Buree kabisaa!!!")  # Added the surrender game
                    
                    main()

                break
            while True:
                end_input = input(ansi_green + "Enter end position (row col): ").strip().split()
                if not end_input:
                    print(ansi_red + "Invalid input. Please enter only two integers separated by a space.")
                    continue
                if end_input[0].lower() == 'q':
                    print(ansi_red+"plAYER HAS QUITE 😞😞")
                    exit()
                    
                if end_input[0].lower() == 's':
                    print("Player Surrendered the game.😞😞 Buree kabisaa!!!")  # Added the surrender game
                    
                    main()

                break
            try:
                start_row, start_col = map(int, start_input)
                end_row, end_col = map(int, end_input)
            except ValueError:
                print(ansi_red + "Invalid input. Please enter integers.")
                continue
            if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
                print(ansi_red + "Invalid input. Position out of range.")
                continue
            valid_move, captured_piece_pos = game.move_piece(start_row, start_col, end_row, end_col, 'p')
            if not valid_move:
                print(ansi_red + "Invalid move. Please try again.")
                continue

            while captured_piece_pos and game.has_capture_move(end_row, end_col, 'p'):
                game.print_board()
                print(f"Piece captured at position {captured_piece_pos} and removed.")
                start_row, start_col = end_row, end_col
                while True:
                    end_input = input(ansi_green + "Enter new end position for continued capture (row col): ").strip().split()
                    if not end_input:
                        print(ansi_red + "Invalid input. Please enter row and column separated by space.")
                        continue
                    if end_input[0].lower() == 'q':
                        break
                    if start_input[0].lower() == 's':
                      print("Player Surrendered the game.😞😞 Buree kabisaa!!!")  # Added the surrender game
                      main()
                    if len(end_input) != 2:
                        print(ansi_red + "Invalid input. Please enter exactly two integers separated by a space." + ansi_reset)
                        continue
                    try:
                        end_row, end_col = map(int, end_input)
                    except ValueError:
                        print(ansi_red + "Invalid input. Please enter integers.")
                        continue
                    if not (0 <= end_row < 8 and 0 <= end_col < 8):
                        print(ansi_red + "Invalid input. Position out of range.")
                        continue
                    valid_move, captured_piece_pos = game.move_piece(start_row, start_col, end_row, end_col, 'p')
                    if valid_move:
                        break
                    else:
                        print(ansi_red + "Invalid move. Please try again.")

            # Check for win condition
            x_count = sum(row.count('c') for row in game.board)
            o_count = sum(row.count('p') for row in game.board)
            if x_count == 0:
                print("PLAYER WON")
                print("WISH ME Congratulations!😄")
                break
            if o_count == 0:
                print("COMPUTER WON, 😄!")
                print("🎉🎉🎉!")

                break

            player_turn = False

        # Computer's move
        available_moves = []
        # iterate over the board and fin the available move for a computer piece
        for row in range(8):
            for col in range(8):
                if game.board[row][col] == 'c':
                    # Normal moves for 'c'
                    #inside the board and next available space in the board for computer piece
                    #to check right 
                    if row + 1 < 8 and col - 1 >= 0 and game.board[row + 1][col - 1] == ' ':
                        available_moves.append((row, col, row + 1, col - 1))
                    #to check left 
                    if row + 1 < 8 and col + 1 < 8 and game.board[row + 1][col + 1] == ' ':
                        available_moves.append((row, col, row + 1, col + 1))
                    # Jump moves for 'c'
                    #check right 
                    if row + 2 < 8 and col - 2 >= 0 and game.board[row + 1][col - 1] == 'p' and game.board[row + 2][col - 2] == ' ':
                        available_moves.append((row, col, row + 2, col - 2))
                    #check left
                    if row + 2 < 8 and col + 2 < 8 and game.board[row + 1][col + 1] == 'p' and game.board[row + 2][col + 2] == ' ':
                        available_moves.append((row, col, row + 2, col + 2))
                elif game.board[row][col] == 'Q':
                    # Moves for 'Q' (king)                
                    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]: #dr save first iteration of the index of the tuple
                        #check normal move 
                        if 0 <= row + dr < 8 and 0 <= col + dc < 8 and game.board[row + dr][col + dc] == ' ':
                            available_moves.append((row, col, row + dr, col + dc))
                        #check capture move 
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
                print(f"😄I master Computer captured a piece at position ({captured_piece_row}, {captured_piece_col}) and moved from ({comp_move[0]}, {comp_move[1]}) to ({comp_move[2]}, {comp_move[3]}).")
                while game.has_capture_move(comp_move[2], comp_move[3], 'c'):
                    game.print_board()
                    possible_moves = []
                    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                        new_row, new_col = comp_move[2] + 2*dr, comp_move[3] + 2*dc
                        if 0 <= new_row < 8 and 0 <= new_col < 8 and game.board[comp_move[2] + dr][comp_move[3] + dc].lower() == 'p' and game.board[new_row][new_col] == ' ':
                            possible_moves.append((comp_move[2], comp_move[3], new_row, new_col))
                    if possible_moves:
                        comp_move = random.choice(possible_moves)
                        game.move_piece(comp_move[0], comp_move[1], comp_move[2], comp_move[3], 'c')
                        captured_piece_row = (comp_move[0] + comp_move[2]) // 2
                        captured_piece_col = (comp_move[1] + comp_move[3]) // 2
                        print(f"Computer continued capturing a piece at position ({captured_piece_row}, {captured_piece_col}) and moved to ({comp_move[2]}, {comp_move[3]}).")
                    else:
                        break
            else:
                print(f"Computer moved from ({comp_move[0]}, {comp_move[1]}) to ({comp_move[2]}, {comp_move[3]}).")
        else:
            break

if __name__ == "__main__":
    main()
