import chess

class chessGame:

    def __init__(self, humanWhite, human, ai):
        self.game = chess.Board()
        self.players = [human, ai] if humanWhite else [ai, human]
        
    def runGame(self):
        while not self.game.is_game_over():
            print(self)
            self.make_move()
        
    def make_move(self):
        move = self.players[0 if self.game.turn else 1].make_move(self.game)
        self.game.push(move)  # Make the move

    def __str__(self):
        row = "   -----------------   \n    a b c d e f g h    \n   -----------------   \n"
        board = str(self.game)
        board =  board.splitlines()
        result = row
        for i in range (8, 0, -1):
            result += "|"+str(i)+"| "+board[8 - i]+" |"+str(i)+"|\n"
        result += row
        return result
        
    
