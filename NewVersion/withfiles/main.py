
from game import *



def main():
    
    
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

    game.print_board()

   
if __name__ == "__main__":
    main()

