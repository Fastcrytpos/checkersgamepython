class Move_piece:
    def move_piece(board, piece, start_row, start_col, end_row, end_col):
        
        if not (0 <= start_row < len(board) and 0 <= start_col < len(board[0]) and
                0 <= end_row < len(board) and 0 <= end_col < len(board[0])):
            raise IndexError("Move out of bounds of the board")
        
        # Normal move
        if abs(start_row - end_row) == 1 and board[end_row][end_col] == ' ':
            board[start_row][start_col] = ' '
            board[end_row][end_col] = piece
        
        # Capture moving up
        elif start_row - end_row == 2:
            board[start_row][start_col] = ' '
            if start_col - end_col == -2:  # capturing right
                board[start_row-1][start_col+1] = ' '
            else:  # capturing left
                board[start_row-1][start_col-1] = ' '
            board[end_row][end_col] = piece
        
        # Capture moving down
        elif start_row - end_row == -2:
            board[start_row][start_col] = ' '
            if start_col - end_col == -2:  # capturing left
                board[start_row+1][start_col+1] = ' '
            else:  # capturing right
                board[start_row+1][start_col-1] = ' '
            board[end_row][end_col] = piece
        
        # King move
        elif piece == "K" or piece == "Q":
            board[start_row][start_col] = ' '
            board[end_row][end_col] = piece
        
        # Promoting a piece
        elif piece == "c" and end_row == 7:  # promoting pawn to queen
            board[start_row][start_col] = ' '
            board[end_row][end_col] = "Q"
        
        elif piece == "p" and end_row == 0:  # promoting pawn to king
            board[start_row][start_col] = ' '
            board[end_row][end_col] = "K"
        
        else:
            raise ValueError("Invalid move")
