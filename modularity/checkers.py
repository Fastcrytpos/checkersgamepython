from constants  import *
class Checkers:
    def __init__(self):
        self.board = [
            [' ', 'c', ' ', 'c', ' ', 'c', ' ', 'c'],
            ['c', ' ', 'c', ' ', 'c', ' ', 'c', ' '],
            [' ', 'c', ' ', 'c', ' ', 'c', ' ', 'c'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['p', ' ', 'p', ' ', 'p', ' ', 'p', ' '],
            [' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p'],
            ['p', ' ', 'p', ' ', 'p', ' ', 'p', ' ']
        ]

    def king(self, piece):
        return piece in ['K', 'Q']


    #function of moving of pieces oin the board    
    def move_piece(self, start_row, start_col, end_row, end_col, player):
       
        if not self.is_valid_position(start_row, start_col) or not self.is_valid_position(end_row, end_col):
            print("positioon is outside the range!! ")
            return False, None
        

        if self.board[start_row][start_col] !=player:
        
            print("you cannot move the computer piece")
            return False, None

        
        if self.board[end_row][end_col] != ' ':
            print("THE POSITION IS OCCUPIED")
            return False, None
        
        
        #using ternary operator to get the doirection if player else give computer
        direction = 1 if player == 'p' else -1
        
        if end_col == start_col + 1 or end_col == start_col - 1:
            if end_row == start_row - direction:  #pieces for player 'p' moving upwards
                self.board[end_row][end_col] = self.board[start_row][start_col]
                self.board[start_row][start_col] = ' '
                return True, None
    
        elif end_col == start_col + 2 or end_col == start_col - 2:
            if end_row == start_row - 2 * direction:  # skip two for player 'p' moving upwards
                captured_row = start_row - direction
                captured_col = start_col + (end_col - start_col) // 2
                
                if self.is_valid_position(captured_row, captured_col) and \
                   self.board[captured_row][captured_col]!= player and \
                   self.board[captured_row][captured_col] != ' ':
                #    print("a piece has been captured a loc :",captured_row, captured_col)
                    
                    self.board[end_row][end_col] = self.board[start_row][start_col]
                    self.board[start_row][start_col] = ' '
                    self.board[captured_row][captured_col] = ' '
                    
                     # Check for promotion after the move
                    if player == 'p' and end_row == 0:
                        self.board[end_row][end_col] = 'K'
                    elif player == 'c' and end_row == 7:
                        self.board[end_row][end_col] = 'Q'

                    return True, (captured_row, captured_col)
        
                print("move is not matching")
                return False, None

    def has_capture_move(self, row, col, player):
        if player == 'p':
            directions = [(-1, 1), (-1, -1)]  # player pieces for player is tpo 'p' moving upwards
        else:
            directions = [(1, 1), (1, -1)]  # computer player is  'c' moving downwards
#diagonal mov around the board
        for d_row, d_col in directions:
            if self.is_valid_position(row + d_row, col + d_col) and \
               self.board[row + d_row][col + d_col] != player and \
               self.board[row + d_row][col + d_col] != ' ' and \
               self.is_valid_position(row + 2 * d_row, col + 2 * d_col) and \
               self.board[row + 2 * d_row][col + 2 * d_col] == ' ':
                return True
        
        return False
#within the range of the boRD PIECES
    def is_valid_position(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8
    
