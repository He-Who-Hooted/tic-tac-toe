class Game:  
    def __init__(self):
        print("Welcome to tic-tac-toe!")
        self.board = [[' ' for _ in range(3)] for _ in range(3)] # initialise the blank board
    
    def __str__(self):
        flat_board = [cell for row in self.board for cell in row]
        board_image = """
   |   |   
 {} | {} | {} 
___|___|___
   |   |   
 {} | {} | {} 
___|___|___
   |   |   
 {} | {} | {} 
   |   |   
    """.format(*flat_board)
        return board_image
    
game = Game()
print(game)