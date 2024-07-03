from constants import *
from board import Board
class Player:

    def get_player_move(board):
                
        while True:
            
            start_input = input(ansi_green + "Enter start position (row col): ").strip().split()

            if start_input[0].lower() == 'q':
                print(ansi_red+"plAYER HAS QUITE 😞😞")
                exit()
            if start_input[0].lower() == 's':
                print(ansi_red + "Play Has Restarted.")
                from main import restart
                restart()
                break
                           
            end_input = input(ansi_green + "Enter end position (row col): ").strip().split()

            if end_input[0].lower() == 'q':
                print(ansi_red+"plAYER HAS QUITE 😞😞")
                exit()
            if end_input[0].lower() == 's':
                print(ansi_red + "Play Has Restarted.")
                from main import restart
                restart()
                break
            try:
                start_row, start_col = map(int, start_input)
                end_row, end_col = map(int, end_input)
            except ValueError:
                print(ansi_red + "checking on input. Please enter integers.")
                continue
            #to not accept skipping boxes. Only move one at a time
            try:
                if not (0<=start_col<8 and 0<=start_row<8 and 0<=end_col<8 and 0<=end_col<8):
                    raise ValueError
            except ValueError:
                print(ansi_red + "Invalid move. You cant move outside of the board")
                continue

            try:
                if (start_col- end_col>2 or start_row-end_row>2):
                    raise ValueError
                
            except ValueError:
                print(ansi_red + "Invalid move. You cant move two blocks at once")
                continue

            try:
                if board[end_row][end_col] !=" ":
                    raise ValueError
                
            except ValueError:
                print(ansi_red + "Invalid move. You cant move tO AN OCCUPIED POSITION")
                continue
            try:
                if board[start_row][start_col] !="K" and end_row>start_row:
                    raise ValueError
                
            except ValueError:
                print(ansi_red + "Invalid move. You cant move only move a normal piece forward")
                continue

            #can only move diagonally
            try:
                if (start_row==end_row or start_col==end_col):
                    raise ValueError
            except ValueError:
                print(ansi_red + "Invalid move. You can only move diagonally from your start Position")
                continue
            if board[start_row][start_col]=='p' or 'K':
                piece = board[start_row][start_col]

            return ( piece, start_row, start_col, end_row, end_col)
        
if __name__=="__main__":
    game=Board()
    Player.get_player_move(game.board)
        