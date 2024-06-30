from checker import *
import random




class Compmove:
    game=Checkers()
    available_moves = []
            # iterate over the board and fin the available move for a computer piece
    for row in range(8):
        for col in range(8):
            if game.board[row][col] == 'c':
                # Normal moves for 'c'
                #inside the board and next available space in the board for computer piece
                #to check right 
                if row + 1 < 8 and col - 1 >= 0 and game.board[row + 1][col - 1] == ' ':
                    available_moves.append((row, col, row + 1, col - 1))
                #to check left 
                if row + 1 < 8 and col + 1 < 8 and game.board[row + 1][col + 1] == ' ':
                    available_moves.append((row, col, row + 1, col + 1))
                # Jump moves for 'c'
                #check right 
                if row + 2 < 8 and col - 2 >= 0 and game.board[row + 1][col - 1] == 'p' and game.board[row + 2][col - 2] == ' ':
                    available_moves.append((row, col, row + 2, col - 2))
                #check left
                if row + 2 < 8 and col + 2 < 8 and game.board[row + 1][col + 1] == 'p' and game.board[row + 2][col + 2] == ' ':
                    available_moves.append((row, col, row + 2, col + 2))
            elif game.board[row][col] == 'Q':
                # Moves for 'Q' (king)                
                for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]: #dr save first iteration of the index of the tuple
                    #check normal move 
                    if 0 <= row + dr < 8 and 0 <= col + dc < 8 and game.board[row + dr][col + dc] == ' ':
                        available_moves.append((row, col, row + dr, col + dc))
                    #check capture move 
                    if 0 <= row + 2*dr < 8 and 0 <= col + 2*dc < 8 and game.board[row + dr][col + dc].lower() == 'p' and game.board[row + 2*dr][col + 2*dc] == ' ':
                        available_moves.append((row, col, row + 2*dr, col + 2*dc))
            if available_moves:
                capture_moves = [move for move in available_moves if abs(move[0] - move[2]) == 2]
            if capture_moves:
                comp_move = random.choice(capture_moves)
            else:
                comp_move = random.choice(available_moves)
