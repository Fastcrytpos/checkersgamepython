
from compmoves import *


class Gameloop:
    game=Compmove.game

    while True:
        
        player_turn = True

        while player_turn:
            while True:
                start_input = input(ansi_green + "Enter start position (row col): ").strip().split()
                if not start_input:
                    print(ansi_red + "Invalid input. Please enter only two integers separated by a space.")
                    continue
                if start_input[0].lower() == 'q':
                    print(ansi_red+"plAYER HAS QUITE 😞😞")
                    exit()
                    
                if start_input[0].lower() == 's':
                    print("Player Surrendered the game.😞😞 Buree kabisaa!!!")  # Added the surrender game
                    
                    #main()

                break
            while True:
                end_input = input(ansi_green + "Enter end position (row col): ").strip().split()
                if not end_input:
                    print(ansi_red + "Invalid input. Please enter only two integers separated by a space.")
                    continue
                if end_input[0].lower() == 'q':
                    print(ansi_red+"plAYER HAS QUITE 😞😞")
                    exit()
                    
                if end_input[0].lower() == 's':
                    print("Player Surrendered the game.😞😞 Buree kabisaa!!!")  # Added the surrender game
                    
                    #main()

                break
            try:
                start_row, start_col = map(int, start_input)
                end_row, end_col = map(int, end_input)
            except ValueError:
                print(ansi_red + "Invalid input. Please enter integers.")
                continue
            if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
                print(ansi_red + "Invalid input. Position out of range.")
                continue
            valid_move, captured_piece_pos = game.move_piece(start_row, start_col, end_row, end_col, 'p')
            if not valid_move:
                print(ansi_red + "Invalid move. Please try again.")
                continue

            while captured_piece_pos and game.has_capture_move(end_row, end_col, 'p'):
                game.print_board()
                print(f"Piece captured at position {captured_piece_pos} and removed.")
                start_row, start_col = end_row, end_col
                while True:
                    end_input = input(ansi_green + "Enter new end position for continued capture (row col): ").strip().split()
                    if not end_input:
                        print(ansi_red + "Invalid input. Please enter row and column separated by space.")
                        continue
                    if end_input[0].lower() == 'q':
                        break
                    if start_input[0].lower() == 's':
                      print("Player Surrendered the game.😞😞 Buree kabisaa!!!")  # Added the surrender game
                      #main()
                    if len(end_input) != 2:
                        print(ansi_red + "Invalid input. Please enter exactly two integers separated by a space." + ansi_reset)
                        continue
                    try:
                        end_row, end_col = map(int, end_input)
                    except ValueError:
                        print(ansi_red + "Invalid input. Please enter integers.")
                        continue
                    if not (0 <= end_row < 8 and 0 <= end_col < 8):
                        print(ansi_red + "Invalid input. Position out of range.")
                        continue
                    valid_move, captured_piece_pos = game.move_piece(start_row, start_col, end_row, end_col, 'p')
                    if valid_move:
                        break
                    else:
                        print(ansi_red + "Invalid move. Please try again.")

            # Check for win condition
            x_count = sum(row.count('c') for row in game.board)
            o_count = sum(row.count('p') for row in game.board)
            if x_count == 0:
                print("PLAYER WON")
                print("WISH ME Congratulations!😄")
                break
            if o_count == 0:
                print("COMPUTER WON, 😄!")
                print("🎉🎉🎉!")

                break

            player_turn = False
            # Computer's move

                    
            game.move_piece(comp_move[0], comp_move[1], comp_move[2], comp_move[3], 'c')
            if abs(comp_move[0] - comp_move[2]) == 2:
                captured_piece_row = (comp_move[0] + comp_move[2]) // 2
                captured_piece_col = (comp_move[1] + comp_move[3]) // 2
                print(f"😄I master Computer captured a piece at position ({captured_piece_row}, {captured_piece_col}) and moved from ({comp_move[0]}, {comp_move[1]}) to ({comp_move[2]}, {comp_move[3]}).")
                while game.has_capture_move(comp_move[2], comp_move[3], 'c'):
                    game.print_board()
                    possible_moves = []
                    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                        new_row, new_col = comp_move[2] + 2*dr, comp_move[3] + 2*dc
                        if 0 <= new_row < 8 and 0 <= new_col < 8 and game.board[comp_move[2] + dr][comp_move[3] + dc].lower() == 'p' and game.board[new_row][new_col] == ' ':
                            possible_moves.append((comp_move[2], comp_move[3], new_row, new_col))
                    if possible_moves:
                        comp_move = random.choice(possible_moves)
                        game.move_piece(comp_move[0], comp_move[1], comp_move[2], comp_move[3], 'c')
                        captured_piece_row = (comp_move[0] + comp_move[2]) // 2
                        captured_piece_col = (comp_move[1] + comp_move[3]) // 2
                        print(f"Computer continued capturing a piece at position ({captured_piece_row}, {captured_piece_col}) and moved to ({comp_move[2]}, {comp_move[3]}).")
                    else:
                        break
            else:
                print(f"Computer moved from ({comp_move[0]}, {comp_move[1]}) to ({comp_move[2]}, {comp_move[3]}).")
        else:
            break
