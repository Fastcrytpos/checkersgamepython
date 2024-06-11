import string
from tile import Board

class PlayerMoves:
    valid_player = []

    def _init_(self, board, player_pieces, computer_pieces, fromposition, toposition, player):
        self.board = board
        self.player_pieces = player_pieces
        self.computer_pieces = computer_pieces
        self.frompositionx = int(fromposition[0])
        self.frompositiony = int(fromposition[1])
        self.topositionx = int(toposition[0])
        self.topositiony = int(toposition[1])
        self.player = player
        self.check()

    def check(self):
        if self.frompositionx < 0 or self.frompositionx >= len(self.board) or self.frompositiony < 0 or self.frompositiony >= len(self.board[0]):
            print("Invalid move! Coordinates out of bounds.")
            return False

        if self.topositionx < 0 or self.topositionx >= len(self.board) or self.topositiony < 0 or self.topositiony >= len(self.board[0]):
            print("Invalid move! Coordinates out of bounds.")
            return False

        if self.player == "c" and self.board[self.frompositionx][self.frompositiony] in self.computer_pieces:
            return True

        if self.player == "p" and self.board[self.frompositionx][self.frompositiony] in self.player_pieces:
            return True

        print("Invalid move! Wrong player or piece.")
        return False

    def displayoptions(self):
        if self.player == "p":
            if (self.topositionx == self.frompositionx - 1 and self.topositiony == self.frompositiony - 1) or \
               (self.topositionx == self.frompositionx - 1 and self.topositiony == self.frompositiony + 1):
                if self.board[self.topositionx][self.topositiony] == '---':
                    self.valid_player.append(f"{self.topositionx}:{self.topositiony}")
                    print(f"Valid move {self.topositionx}:{self.topositiony}")
                elif self.board[self.topositionx][self.topositiony] in self.computer_pieces:
                    print(f"Opponent's piece at {self.topositionx}:{self.topositiony}")
                else:
                    print("Invalid move")
            else:
                print("Invalid move")
        elif self.player == "c":
            if (self.topositionx == self.frompositionx + 1 and self.topositiony == self.frompositiony - 1) or \
               (self.topositionx == self.frompositionx + 1 and self.topositiony == self.frompositiony + 1):
                if self.board[self.topositionx][self.topositiony] == '---':
                    self.valid_player.append(f"{self.topositionx}:{self.topositiony}")
                    print(f"Valid move {self.topositionx}:{self.topositiony}")
                elif self.board[self.topositionx][self.topositiony] in self.player_pieces:
                    print(f"Opponent's piece at {self.topositionx}:{self.topositiony}")
                else:
                    print("Invalid move")
            else:
                print("Invalid move")

if __name__ == "_main_":
    board = Board(8, 8)
    board.display()

    while True:
        from_pos = input("Enter position to move from (row,col): ")
        if from_pos.lower() == 'q':
            break
        to_pos = input("Enter position to move to (row,col): ")
        if to_pos.lower() == 'q':
            break
        
        player_move = PlayerMoves(board.board, board.player_pieces, board.computer_pieces, from_pos.split(','), to_pos.split(','), 'p')
        if player_move.check():
            player_move.displayoptions()
            print("Valid move!")
        else:
            print("Invalid move! Try again.")