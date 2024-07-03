class Move_piece:
    def move_piece(board,piece,start_row,start_col,end_row,end_col):

        #if a normal move 
        if abs(start_row-end_row)==1:
            board[start_row][start_col]=' '
            board[end_row][end_col]=piece

        #if a capture moving up 
        if start_row-end_row==2:
            board[start_row][start_col]=' '
            #capturing right
            if start_col-end_col==-2:
               #captured piece
               board[start_row-1][start_col+1]=' '
            #capturing left 
            else:
               #captured piece
               board[start_row-1][start_col+1]=' '
            board[end_row][end_col]=piece


         #if a capture moving down 
        if start_row-end_row==-2:
            board[start_row][start_col]=' '
            #capturing left
            if start_col-end_col==-2:
               #captured piece
               board[start_row+1][start_col+1]=' '
            #capturing right
            else:
               #captured piece
               board[start_row+1][start_col-1]=' '
            board[end_row][end_col]=piece

        #if a king move
        if piece== ("K" or "Q"):
            board[start_row][start_col]=' '
            board[end_row][end_col]=piece

        


   