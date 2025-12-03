import random

class Game:  
    def __init__(self):
        print("Welcome to tic-tac-toe!")
        self.board = [[' ' for _ in range(3)] for _ in range(3)] # initialise the blank board
        self.player1 = input("Player 1 name?\t") # player 1 name
        self.player2 = input("Player 2 name?\t") # player 2 name
        self.player_x = random.choice([self.player1, self.player2]) # decide randomly who is 'x'
        self.player_o = self.player2 if self.player_x == self.player1 else self.player1
        self.currentPlayer = self.player_x
        self.currentSign = 'x'
        
        # game has a maximum of nine turns
        for turn in range(9):
            self.get_move()
            
            winner = self.check_winner()
            if winner == 'x':
                print(self) # render the board
                print("{winner} wins the game!".format(winner=self.player_x))
                break
            elif winner == 'o':
                print(self) # render the board
                print("{winner} wins the game!".format(winner=self.player_o))
                break
            elif turn == 8:
                print(self) # render the board
                print("It's a tie!")
                break

        
        
    def check_winner(self):
        # check for winning across
        for row in range(3):
            if self.board[row][0] == self.board[row][1] and self.board[row][1] == self.board[row][2]:
                if not self.board[row][0] == '':
                    return self.board[row][0] # if not blank return the sign
    
        # check for winning down
            for col in range(3):
                if self.board[0][col] == self.board[1][col] and self.board[1][col] == self.board[2][col]:
                    if not self.board[0][col] == '':
                        return self.board[0][col] # if not blank return the sign
                    
        # check for winning diagonally
        if self.board[0][0] == self.board [1][1] and self.board[1][1] == self.board[2][2]:
            if not self.board[1][1] == '':
                return self.board[1][1]
            
        # check for winning diagonally
        if self.board[0][2] == self.board [1][1] and self.board[1][1] == self.board[2][0]:
            if not self.board[1][1] == '':
                return self.board[1][1]
        
        return '' # return blank if all else fails
                    

    
    def __str__(self):
        flat_board = [cell for row in self.board for cell in row]
        board_image = """
    A   B   C
   ___________
  |   |   |   |
1 | {} | {} | {} | 
  |___|___|___|
  |   |   |   |
2 | {} | {} | {} |
  |___|___|___|
  |   |   |   |
3 | {} | {} | {} |
  |___|___|___|
    """.format(*flat_board)
        return board_image
   
    def get_move(self):

        # render the board
        print(self)
        print("{player} it is your turn to place a '{sign}'.".format(player=self.currentPlayer, sign=self.currentSign))

        while True:
            move = input("Your move (e.g., A1): ").strip().upper()
            
            if len(move) != 2:
                print("Enter 2 characters like 'A1'")
                continue
                
            col_char, row_char = move[0], move[1]
            
            # Convert A,B,C to 0,1,2
            if col_char in 'ABC':
                col = ord(col_char) - ord('A')
            else:
                print("Column must be A, B, or C")
                continue
                
            # Convert 1,2,3 to 0,1,2
            if row_char in '123':
                row = int(row_char) - 1
            else:
                print("Row must be 1, 2, or 3")
                continue
                
            if self.board[row][col] != ' ':
                print("That spot is already taken!")
                continue

            # update the board and switch player
            self.board[row][col] = self.currentSign
            if self.currentSign == 'x':
                self.currentSign = 'o'
                self.currentPlayer = self.player_o
            else:
                self.currentSign = 'x'
                self.currentPlayer = self.player_x
            return


game = Game() # creating a game object will take care of everything for us