import chess

class chessGame:

    def __init__(self, humanWhite, human, ai):
        self.game = chess.Board()
        self.players = [human, ai] if humanWhite else [ai, human]
        
    def runGame(self):
        while not self.game.is_game_over():
            print(self.game)
            self.make_move()
        
        
        
        
        
        
    def make_move(self):
        move = self.players[0 if self.game.turn else 1].make_move(self.game)
        self.game.push(move)  # Make the move

    def is_game_over(self):
        return self.game.is_game_over()
