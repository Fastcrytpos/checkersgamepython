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
        
        # game.board[0][1]='k'
            
        piece,start_row,start_col,end_row,end_col=Player.get_player_move(game.board)
        Move_piece.move_piece(game.board,piece,start_row,start_col,end_row,end_col) 
        print("player moved")
        

        piece,start_row,start_col,end_row,end_col=ComputerMove.get_computer_move(game.board)
        Move_piece.move_piece(game.board,piece,start_row,start_col,end_row,end_col) 
        print("comp moved")



        
if __name__=="__main__":
    main()
              