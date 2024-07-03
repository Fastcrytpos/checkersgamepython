class Move_piece:
    def move_piece(board,piece,start_row,start_col,end_row,end_col,player):
        board[start_row][start_col]=' '
        board[end_row][end_col]=piece
    