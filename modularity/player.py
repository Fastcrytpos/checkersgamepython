# player.py

from constants import *


class PlayerMove:
    @staticmethod#The get_player_move() method is decorated with @staticmethod to indicate that it does not depend on instance attributes and can be called directly from the class PlayerMove.
    def get_player_move():
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
                print(ansi_red + "checking on  input. Please enter integers.")
                continue
            #to not accep
            try:
                if (start_col- end_col>2 or start_row-end_row>2):
                    raise ValueError
                
            except ValueError:
                print(ansi_red + "Invalid move. You cant move two blocks at once")
                continue
            try:
                if (start_row==end_row or start_col==end_col):
                    raise ValueError
            except ValueError:
                print(ansi_red + "Invalid move. You can only move diagonally")
                continue
            return start_row, start_col, end_row, end_col
   
        