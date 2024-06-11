import string  # Import the string module to access ASCII characters

class Board:
    def __init__(self, rows, cols):
        # Initialize the Board class with rows, columns, an empty board, and empty lists for player and computer pieces
        self.rows = rows
        self.cols = cols
        self.board = [['---' for _ in range(cols)] for _ in range(rows)]  # Create an empty board
        self.player_pieces = []  # List to store player pieces
        self.computer_pieces = []  # List to store computer pieces
        self.turn = 'player'
        self.initialize_pieces()  # Call the method to initialize player and computer pieces

    def initialize_pieces(self):
        player_piece_counter = 1  # Initialize a counter for player pieces
        computer_piece_counter = 1  # Initialize a counter for computer pieces

        # Place player pieces on the board
        for row in range(3):
            for col in range(self.cols):
                if (row + col) % 2 == 1:  # Check if the sum of row and column is odd (alternate squares)
                    symbol = f"p{player_piece_counter}"  # Player piece symbol (p1, p2, p3, ...)
                    self.player_pieces.append((row, col, symbol))  # Add player piece to the list
                    self.board[row][col] = symbol  # Place player piece on the board
                    player_piece_counter += 1  # Increment player piece counter

        # Place computer pieces on the board
        for row in range(self.rows - 3, self.rows):
            for col in range(self.cols):
                if (row + col) % 2 == 1:  # Check if the sum of row and column is odd (alternate squares)
                    symbol = f"c{string.ascii_lowercase[computer_piece_counter - 1]}"  # Computer piece symbol (ca, cb, cc, ...)
                    self.computer_pieces.append((row, col, symbol))  # Add computer piece to the list
                    self.board[row][col] = symbol  # Place computer piece on the board
                    computer_piece_counter += 1  # Increment computer piece counter

    def display(self):
        # Display the board and instructions to the players
        print("\nYou enter the coordinates in the form x,y by reading the coordinates e.g., to move b50 enter 5,0 to 4,1.")
        print("Quit by entering 'q' or 'Q'.")
        print("Walk away by pressing 's'.")
        print("Sign and start the game!")

        print("\nAgree if jumping is mandatory?[Y/n]: n\n")

        for row in range(self.rows):
            row_str = f"{row}  |"
            for col in range(self.cols):
                row_str += f" {self.board[row][col]} "  # Add each cell of the board to the row string
            print(row_str)  # Print the row with cell contents

        print("\n   ", end="")
        for col in range(self.cols):
            print(f"  {col} ", end="")
        print("\n")

# this the switch turn
    def player_move(self):
        # Logic for player's move
        pass

    def computer_move(self):
        # Logic for computer's move using minimax or any other algorithm
        pass

    def game_loop(self):
        while True:
            self.display()
            if self.turn == 'player':
                self.player_move()
            else:
                self.computer_move()
            self.switch_turn()

# have enhanced the board to include methods for moving pieces,checking valid moves and
# and updating the board state
    def move_piece(self, start, end):
            start_row, start_col = start
            end_row, end_col = end
            piece = self.board[start_row][start_col]
            self.board[start_row][start_col] = '---'
            self.board[end_row][end_col] = piece

    def get_possible_moves(self, player):
        moves = []
        direction = 1 if player == 'p' else -1
        pieces = self.player_pieces if player == 'p' else self.computer_pieces
        for piece in pieces:
            row, col, symbol = piece
            if 0 <= row + direction < 8:
                if 0 <= col - 1 < 8 and self.board[row + direction][col - 1] == '---':
                    moves.append(((row, col), (row + direction, col - 1)))
                if 0 <= col + 1 < 8 and self.board[row + direction][col + 1] == '---':
                    moves.append(((row, col), (row + direction, col + 1)))
        return moves  

    def is_game_over(self):
        player_pieces_left = any('p' in cell for row in self.board for cell in row)
        computer_pieces_left = any('c' in cell for row in self.board for cell in row)
        return not player_pieces_left or not computer_pieces_left

    def evaluate(self):
        player_pieces = sum(cell.startswith('p') for row in self.board for cell in row)
        computer_pieces = sum(cell.startswith('c') for row in self.board for cell in row)
        return player_pieces - computer_pieces 

if __name__ == "__main__":
    # Example usage
    board = Board(8, 8)  # Create a board object with 8 rows and 8 columns
    board.display()  # Display the initial state of the board

