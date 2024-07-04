from board import Board
from intro import Intro
from player import Player
from movepiece import Move_piece
from computer import ComputerMove

def main():
    Intro.print_game_rules()
    game=Board()

    while True:
        Board.print_board(game)        
            
        piece,start_row,start_col,end_row,end_col=Player.get_player_move(game.board)
        Move_piece.move_piece(game.board,piece,start_row,start_col,end_row,end_col) 
        print("player moved")

         # Check for player piece promotion
        if piece == 'p' and end_row == 0:
            game.board[end_row][end_col] = 'K'
            print("Player's piece promoted to King")

        
        # computer turn
        piece,start_row,start_col,end_row,end_col=ComputerMove.get_computer_move(game.board)
        Move_piece.move_piece(game.board,piece,start_row,start_col,end_row,end_col) 
        print("comp moved")

         # Check for computer piece promotion
        if piece == 'c' and end_row == 7:
            game.board[end_row][end_col] = 'Q'
            print("Computer's piece promoted to Queen")
        



        
if __name__=="__main__":
    main()
              