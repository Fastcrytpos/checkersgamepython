from tile import Board

class ComputerMove:
    def __init__(self):
        self.board = Board(8, 8)
        self.human_player = 'p'
        self.computer_player = 'c'

    def play(self):
        while not self.board.is_game_over():
            self.board.display()
            if self.board.turn == self.human_player:
                move = self.get_player_move()
            else:
                move = self.get_computer_move()
            self.board.move_piece(move[0], move[1])
        self.board.display()
        print("Game Over!")

    def get_player_move(self):
        print("Your turn!")
        moves = self.board.get_possible_moves(self.human_player)
        for i, move in enumerate(moves):
            print(f"{i}: {move}")
        move_index = int(input("Choose your move: "))
        return moves[move_index]

    def get_computer_move(self):
        print("Computer's turn!")
        best_move = None
        best_value = float('-inf')
        # iterate over possible moves
        for move in self.board.get_possible_moves(self.computer_player):
            new_state = Board(8, 8)#creating new state for every possible move
            new_state.board = [row[:] for row in self.board.board]#copying the board state
            new_state.move_piece(move[0], move[1]) #simulates the current move on the new state

            #this evaluates the simulated move using the minimax algorithm
            move_value = self.minimax(new_state, 3, float('-inf'), float('inf'), False)
           
            #updating the best move
            if move_value > best_value:
                best_value = move_value
                best_move = move
        return best_move

#This algorithm is used to make optimal decisions in game of checkers.
    def minimax(self, state, depth, alpha, beta, maximizing_player):
        if depth == 0 or state.is_game_over():
            return state.evaluate()

        if maximizing_player:
            max_eval = float('-inf')
            for move in state.get_possible_moves(state.turn):
                new_state = Board(8, 8)
                new_state.board = [row[:] for row in state.board]
                new_state.move_piece(move[0], move[1])
                eval = self.minimax(new_state, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in state.get_possible_moves(state.turn):
                new_state = Board(8, 8)
                new_state.board = [row[:] for row in state.board]
                new_state.move_piece(move[0], move[1])
                eval = self.minimax(new_state, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

if __name__ == "__main__":
    game = ComputerMove()
    game.play()


    
