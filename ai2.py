import chess
from human import human
import random

# Same as ai, but make move within method
class ai2:
    def __init__(self):
        self.max_depth = 2
        self.max_q = 5
        
    def make_move(self, game):
        moves = list(game.legal_moves)
        max = [-10000,0]
        
        for i in range(len(moves)):
            value = self.move_value(game, -10000, 10000, 1, moves[i])
            
            if value > max[0]:
                max[0] = value
                max[1] = moves[i]
        
        return max[1]
    
    def move_value(self, game, alpha, beta, depth, move):
        value = 0
        
        if depth > self.max_q:
            value = self.eval(game)
        elif depth > self.max_depth and not game.gives_check(move) and not game.is_capture(move):
            value = self.eval(game)
        else:
            game.push(move)
            
            if game.is_game_over():
                if game.is_checkmate():
                    value = 9999 if game.turn else -9999
            elif game.turn:
                # White to play
                min_val = 10000
                moves = list(game.legal_moves)
                for i in range(len(moves)):
                    value_next = self.move_value(game, alpha, beta, depth + 1, moves[i])
                    min_val = min(value_next, min_val)
                    beta = min(value_next, beta)
#                    if value_next < min:
#                        min = value_next
#                    if value_next < beta:
#                        beta = value_next
                    if beta <= alpha:
                        break
                value = min_val
            else:
                # Black to play
                max_val = -10000
                moves = list(game.legal_moves)
                for i in range(len(moves)):
                    value_next = self.move_value(game, alpha, beta, depth + 1, moves[i])
                    max_val = max(max_val, value_next)
                    alpha = max(alpha, value_next)
#                    if value_next > max:
#                        max = value_next
#                    if value_next > alpha:
#                        alpha = value_next
                    if beta <= alpha:
                        break
                value = max_val
            game.pop()
        return value
    
    def eval(self, game):
        # Evalutes the current game state, from -9999 to 9999
        eval = random.random()
        for  (piece, value) in [(chess.PAWN, 1),
                               (chess.BISHOP, 4),
                               (chess.KING, 0),
                               (chess.QUEEN, 10),
                               (chess.KNIGHT, 5),
                               (chess.ROOK, 3)]:
            eval += len(game.pieces(piece, False)) * value
            eval -= len(game.pieces(piece, True)) * value
            # can also check things about the pieces position here
        return eval
        
    def min(one, two):
        return one if one < two else two
        
    def max(one, two):
        return one if one > two else two
