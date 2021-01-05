import chess
import time

class chessGame:

    def __init__(self, humanWhite, human, ai):
        self.game = chess.Board()
        self.humanWhite = humanWhite
        self.players = [human, ai] if humanWhite else [ai, human]
        self.times = [0, 0]
        
    def runGame(self):
        while not self.game.is_game_over():
            print(self)
            print(self.times)
            self.make_move()
        print(self.game.turn)
        
    def make_move(self):
        time1 = time.time()
        move = self.players[0 if self.game.turn else 1].make_move(self.game)
        time2 = time.time() - time1
        self.times[0 if self.game.turn else 1] += time2
        if self.game.turn != self.humanWhite:
            print("Computer chose " + str(move))
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
        
    
