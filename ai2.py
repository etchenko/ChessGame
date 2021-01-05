import chess
from human import human
import random

# Same as ai, but make move within method
class ai2:
    def __init__(self, color):
        self.max_depth = 2
        self.max_q = 5
        self.color = color
        
    def make_move(self, game):
        moves = list(game.legal_moves)
        max = [-10000 if self.color == 1 else 10000,0]
        for i in range(len(moves)):
            value = self.move_value(game, -10000, 10000, 1, moves[i])
            if (self.color == 1 and value > max[0]) or (self.color == 0 and value < max[0]):
                max[0] = value
                max[1] = moves[i]
        return max[1]
        
    
    def move_value(self, game, alpha, beta, depth, move):
        value = 0
        if depth > self.max_q:
            value = self.eval(game)
        elif depth > self.max_depth and not game.gives_check(move) and not game.is_capture(move) and not game.is_check():
            value = self.eval(game)
        else:
            game.push(move)
            
            if game.is_game_over():
                if game.is_checkmate():
                    value = 9999 if game.turn else -9999
            elif game.turn:
                value = self.min_val(game, alpha, beta, depth, move)
            else:
                value = self.max_val(game, alpha, beta, depth, move)
            game.pop()
        return value
        
    def min_val(self, game, alpha, beta, depth, move):
        min_val = 10000
        moves = list(game.legal_moves)
        for i in range(len(moves)):
            val = self.move_value(game, alpha, beta, depth + 1, moves[i])
            min_val = min(val, min_val)
            beta = min(val, beta)
            if beta <= alpha:
                break
        return min_val
        
    
    def max_val(self, game, alpha, beta, depth, move):
        max_val = -10000
        moves = list(game.legal_moves)
        for i in range(len(moves)):
            val = self.move_value(game, alpha, beta, depth + 1, moves[i])
            max_val = max(max_val, val)
            alpha = max(alpha, val)
            if beta <= alpha:
                break
        return max_val
    
    def eval(self, game):
        # Evalutes the current game state, from -9999 to 9999
        eval = random.random()
        for  (piece, value) in [(chess.PAWN, 1),
                               (chess.BISHOP, 3),
                               (chess.KING, 0),
                               (chess.QUEEN, 9),
                               (chess.KNIGHT, 3),
                               (chess.ROOK, 5)]:
            eval += len(game.pieces(piece, False)) * value
            eval -= len(game.pieces(piece, True)) * value
            # can also check things about the pieces position here
            
        return eval
        
    def min(one, two):
        return one if one < two else two
        
    def max(one, two):
        return one if one > two else two
