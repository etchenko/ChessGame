import chess
from human import human
import random

# Push and pop all the moves on the same board not to create more
# Implement simple minimax algorithm at first
# Create an arbitrary cutoff for depth searched
# Figure out an evaluation function

class ai:
    def __init__(self):
        self.max_depth = 3
        
        
        
    def make_move(self, game):
        # Initialize
        moves = list(game.legal_moves)
        max = [-10000,0]
        
        # Go through possible moves and find their value
        for i in range(len(moves)):
            game.push(moves[i])
            values = self.move_value(game, 1)
            game.pop()
            # If move is the best, remember
            if values > max[0]:
                max[0] = values
                max[1] = moves[i]
        
        # Return best move
        return max[1]
        
        
        
    def move_value(self, game, depth):
        # Finds the inherent value of the move just played
        value = 0

        if game.is_game_over():
            value =  9999 if game.turn else -9999
        elif depth == self.max_depth:
            value = self.evaluation(game)
        elif game.turn:
            # White to play
            min = 10000
            moves = list(game.legal_moves)
            for i in range(len(moves)):
                game.push(moves[i])
                value_next = self.move_value(game, depth + 1)
                game.pop()
                if value_next < min:
                    min = value_next
            value = min
        else:
            # Black to play
            max = -10000
            moves = list(game.legal_moves)
            for i in range(len(moves)):
                game.push(moves[i])
                value_next = self.move_value(game, depth + 1)
                game.pop()
                if value_next > max:
                    max = value_next
            value = max
            
        return value
            
    def evaluation(self, game):
        # Evaluates the current game state, from -9999 to 9999
        eval = random.random()
        for (piece, value) in [(chess.PAWN, 1),
                               (chess.BISHOP, 4),
                               (chess.KING, 0),
                               (chess.QUEEN, 10),
                               (chess.KNIGHT, 5),
                               (chess.ROOK, 3)]:
            eval += len(game.pieces(piece, False)) * value
            eval -= len(game.pieces(piece, True)) * value
            # can also check things about the pieces position here
        return eval
