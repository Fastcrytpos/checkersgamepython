# player.py

from constants import *
from checkers import *


class PlayerMove:
    @staticmethod
    def get_player_move(board):
        while True:
            start_position = input(ansi_green + "Enter start position (row col): ").strip().lower()
            
            if start_position == 'q':
                print(ansi_red + "Player has quit ")
                return None  # Indicate quitting by returning None
            elif start_position == 's':
                print(ansi_red + "Play has restarted.")
                from main import restart
                restart()
                return None  # Indicate restart by returning None
            
            try:
                start_row, start_col = map(int, start_position.split())
                
                if not (0 <= start_row <= 7 and 0 <= start_col <= 7):  # Adjusted range to 0-7
                    raise ValueError("Values must be between 0 and 7 inclusive.")
                
                if board[start_row][start_col] not in ("p", "K"):  # Check if position contains player's pieces
                    raise ValueError("You can only move your pieces")
                
                break  # Exit the loop if input is valid
            
            except ValueError as e:
                print(ansi_red + f"Invalid input. {e}")
                continue
        
        while True:
            end_position = input(ansi_green + "Enter end position (row col): ").strip().lower()
            
            if end_position == 'q':
                print(ansi_red + "Player has quit ")
                return None  # Indicate quitting by returning None
            elif end_position == 's':
                print(ansi_red + "Play has restarted.")
                from main import restart
                restart()
                return None  # Indicate restart by returning None
            
            try:
                end_row, end_col = map(int, end_position.split())
                
                if not (0 <= end_row <= 7 and 0 <= end_col <= 7):  # Adjusted range to 0-7
                    raise ValueError("Values must be between 0 and 7 inclusive.")
                
                if board[end_row][end_col] != " ":  # Check if position is empty
                    raise ValueError("You can not move to occupied positions")
                
               
            
            except ValueError as e:
                print(ansi_red + f"Invalid input. {e}")
                continue

        # After both loops, return the validated start and end positions
        return start_row, start_col, end_row, end_col

       
      

        


                







   
if __name__ == "__main__":
    game=Checkers()
    PlayerMove.get_player_move(game.board)