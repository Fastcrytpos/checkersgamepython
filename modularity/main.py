from board import BoardPrinter  # Importing BoardPrinter class to print the game board
from player import PlayerMove   # Importing PlayerMove class to handle player moves
from ComputerMove import ComputerMove  # Importing ComputerMove class to handle computer moves
from checkers import Checkers    # Importing Checkers class which represents the game logic

def print_game_rules():
    """Prints the game rules and waits for user to start."""
    print()
    print("\033[95m***************************************************************************************")
    print("                                WELCOME TO CHECKERS!")
    print("***************************************************************************************\033[0m")
    print()
    print("\033[92m1. To move a piece, enter the X and Y coordinates of the piece separated by a space.")
    print("2. For example: '5 0 4 1' moves a piece from row 5, col 0 to row 4, col 1.")
    print("3. Press 'Q' to quit the game.")
    print("Press enter s restart the game.")
    input("5. Press Enter to start the game...\033[0m")


def main():
    """Main function to run the game."""
    print_game_rules()  # Print game rules at the start
    game = Checkers()   # Initialize the game instance
    while True:  # Main game loop
        BoardPrinter.print_board(game.board)  # Print the current game board
        player_turn = True  # showing if it it is the players turn

        while player_turn:
            if player_turn == True:
                print("\033[92mPLAYER'S turn.\033[0m")
            start_row, start_col, end_row, end_col = PlayerMove.get_player_move()  # catching/getting the  player's move
            # trying to mMving the the piece for player
            valid_move, captured_piece_pos = game.move_piece(start_row, start_col, end_row, end_col, 'p')
            if not valid_move:
                print("\033[91mInvalid move. Please try again.\033[0m")
                continue  # If/ when the   move is invalid or against the rule, ask player to try again

            # CONfirming more or additional captures if there is a capture move
            while captured_piece_pos and game.has_capture_move(end_row, end_col, 'p'):
                BoardPrinter.print_board(game.board)
                print(f"Piece capTured   at position {captured_piece_pos} and removed.")
                # end_row, end_col = PlayerMove.get_player_move()  # Get next move after capture
                valid_move, captured_piece_pos = game.move_piece(start_row, start_col, end_row, end_col, 'p')

                if not valid_move:
                    continue  # If move after capture is invalid, ask player to try again

            player_turn = False  # End player's turn after successful move
        # Computer's turn to move
        comp_move = ComputerMove.get_computer_move(game.board)
        if comp_move is None:
            break  # If computer cannot move, end the game

        # Making  tthe computer's move on the board
        game.move_piece(comp_move[0], comp_move[1], comp_move[2], comp_move[3], 'c')

        # CHECKIng if computer is capturing a piece agt location
        if abs(comp_move[0] - comp_move[2]) == 2:
            print(f"Computer captured a piece and moved from ({comp_move[0]}, {comp_move[1]}) to ({comp_move[2]}, {comp_move[3]}).")
        
            # Check for continued captures by the computer
            while game.has_capture_move(comp_move[2], comp_move[3], 'c'):
                BoardPrinter.print_board(game.board)
                comp_move = ComputerMove.get_computer_move(game.board)
                if comp_move is None:
                    break
                game.move_piece(comp_move[0], comp_move[1], comp_move[2], comp_move[3], 'c')
                print(f"Computer continued capturing and moved to ({comp_move[2]}, {comp_move[3]}).")
        else:
            print(f"Computer moved from ({comp_move[0]}, {comp_move[1]}) to ({comp_move[2]}, {comp_move[3]}).")

    print("Game Over!")  # Print game over message when game ends

if __name__ == "__main__":
    main() 