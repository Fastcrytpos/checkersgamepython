					**Checkers** 
Checkers is a classic two-player board game. It is a strategy game that requires players to move their pieces across the board, capturing their opponent's pieces and ultimately trying to reach the other end of the board with one of their pieces to become a king. The  goal is to provide an overview of the game, breaking it down into several classes that work together to provide the game's functionality. We will be using Python for this project.

 **MVPS**
 1. A user should be able to see the board on the console.
 2. the user should be prompted to play. He should also be given a sample move.
 3. the user should be able to type coordinates for a valid move.
 5. the program should display that the move is valid and it should only move diagonally forward on the board for regular players
 6. Once the user inputs a valid move the program will play as the opponent playing a random valid move with its players.
 7. the program should display to the user the move that it played and consequently prompt him to input another move
 8. the user should be able to capture opponents' players,
 9. the program should crown a player, "King" when it reaches the opponent's bedroom
 10. the user should be able to move the king backward and forwards and capture it as well

**functionalities**
1. parseMove(): Parse user input into coordinates representing moves on a game board, returning a list of tuples indicating row and column positions.
2. checkWinner(): Determine the winner based on the remaining pieces on the board and update the game state accordingly.
3. changeTurn(): Switch the current player's turn, updating relevant game state data such as active board values, enemy positions, and movement directions.
4. move(): Modify the game state based on a provided move string, updating the board, changing turns, and checking for a win condition.
5. checkValidMove(): Determine if a given move is valid for the current player, considering constraints such as whether the game has already been won.
6. Capture(): The user or computer should be able to capture the opponent directly in front

**collaborations**
Ms. Alhandra Mohammed
Mr. Michael Randa
Mr. Fredrick Mwai
Mr. Samson Mubeya
Mr. Newton Kipkurui


**Requirements**
Please install Tabulate from pip to help you show the table in the terminal window


**accomplished so far**
1. Presented the board on terminal for the user to see the positions
2. Take user input
3. User can select player to move
4. player can move to the next line
5. a while loop to make the terminal not to kill or exit
6. player cannot move outise the board or outside its array
7. Computer is able to play
8. kings' crowning
9. kings' moves
10. when pressing 'Q' it should quit the game
11. In the middling of the game, if you press 's' it should output a surrender message and restart the game

**pending**
1. colors
2. 
3. 
4. 
5. 
6. an option for mandatory capture, to choose to capture or not.
