import chess

class human:
    def __init__(self):
        self.get_side()
        
    def get_side(self):
        self.white = None
        while self.white is None:
            print("Do you wish to play as white ? (y or n)")
            answer = input()
            
            if answer == "y":
                self.white = True
            elif answer == "n":
                self.white = False
            else:
                print("Please enter 'y' or 'n'")
                
    def make_move(self, game):
        
        move = None
        
        while move is None:
            print("Please enter your move")
            move = input()
            
            try:
                move = chess.Move.from_uci(move)
            except:
                move = None
            if not move in game.legal_moves:
                print("You need to enter a legal move")
                move = None
                
        return move
                
            
