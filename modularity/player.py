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
                            
            end_input = input(ansi_green + "Enter end position (row col): ").strip().split()
            if end_input[0].lower() == 'q':
                print(ansi_red + "Player has quit.")
                exit()
            try:
                start_row, start_col = map(int, start_input)
                end_row, end_col = map(int, end_input)
            except ValueError:
                print(ansi_red + "checking on  input. Please enter integers.")
                continue

            return start_row, start_col, end_row, end_col