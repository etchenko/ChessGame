import chess
from human import human
import random
import time
from table import table
from hash_entry import hash_entry
import math

# Combination of all different implementations of AI
class totalai:
    def __init__(self):
        self.time_limit = 5  # The limit in seconds of calculations
        # The piece table for Zobrist Hashing
        self.rand = [round(random.random()*10000000000000000) for i in range(768)]
        
    def make_move(self, game):
        self.game = game # Set game to be global game for this move
        start = time.time()
        self.distance = 2
        #self.max_q = 4
        self.max_time = start + self.time_limit
        self.time_ended = False
        self.hash = self.get_hashkey()
        self.table = table()
        self.moves = game.fullmove_number
        
        while not self.time_ended:
            print(self.distance)
            move = self.iterative_root()
            self.distance += 1
            #self.max_q += 1
        return move
        
    def iterative_root(self):
        moves = list(self.game.legal_moves)
        max = [math.inf, 0]
        for i in moves:
            if time.time() > self.max_time:
                self.time_ended = True
            value = self.move_value(-math.inf, math.inf, i, 0)
            if value < max[0]:
                max[0] = value
                max[1] = i
        return max[1]
    
    def move_value(self, alpha, beta, move, depth):
       # print(move)
        value = 0
        self.mod_hashkey(move)
        hashed_game = self.table.get(self.hash)
        if hashed_game is not None:
            if hashed_game.depth >= depth: # Make sure this was calculated to enough depth
                return hashed_game.eval
        
        # Make sure game isn't in bad position before evaluating
        #if depth >= self.max_q:
            #value = self.eval()
        elif depth >= self.distance: #and not self.game.gives_check(move) and not self.game.is_capture(move) and not self.game.is_check():
            value = self.eval()
        else:
            self.game.push(move)
            if self.game.is_game_over():
                if self.game.is_checkmate():
                    value = math.inf if not self.game.turn else -math.inf
            elif not self.game.turn:
                value = self.min_val(alpha, beta, depth)
            else:
                value = self.max_val(alpha, beta, depth)
            self.game.pop()
        board = hash_entry(value, depth, self.moves)
        self.table.add(self.hash, board)
        self.mod_hashkey(move)
        return value
        
    def min_val(self, alpha, beta, depth):
        moves = list(self.game.legal_moves)
        for i in moves:
            beta = min(beta, self.move_value(alpha, beta, i, depth + 1))
            if beta <= alpha:
                return beta
        return beta
    
    def max_val(self, alpha, beta, depth):
        moves = list(self.game.legal_moves)
        for i in moves:
            alpha = max(alpha, self.move_value(alpha, beta, i, depth + 1))
            if beta <= alpha:
                return alpha
        return alpha
        
    def eval(self):
        # Evalutes the current game state, from -9999 to 9999
        eval = random.random()
        for (piece, value) in [(chess.PAWN, 1),
                               (chess.BISHOP, 3),
                               (chess.KING, 0),
                               (chess.QUEEN, 9),
                               (chess.KNIGHT, 3),
                               (chess.ROOK, 5)]:
            eval -= len(self.game.pieces(piece, False)) * value
            eval += len(self.game.pieces(piece, True)) * value
            # can also check things about the pieces position here
        return eval
    
    def min(one, two):
        return one if one < two else two
        
    def max(one, two):
        return one if one > two else two
        
    def get_hashkey(self):
        key = 0
        for i in range(2):
            for j in range(1,7):
                pos = list(self.game.pieces(j, True if i == 0 else False))
                for k in pos:
                    key ^= self.rand[k + 64 * ((j - 1) + (0 if i == 0 else 6))]
        return key
        
    def mod_hashkey(self, move):
        # Modifies the hash key to include the move that has not been made yet
        #m = chess.Move.from_uci(move)
        self.hash ^= self.rand[move.from_square + 64 * ((self.game.piece_type_at(move.from_square) - 1) + (0 if self.game.color_at(move.from_square) == 0 else 6))]
        self.hash ^= self.rand[move.to_square + 64 * ((self.game.piece_type_at(move.from_square) - 1) + (0 if self.game.color_at(move.from_square) == 0 else 6))]
        if self.game.piece_type_at(move.to_square) is not None:
            self.hash ^= self.rand[move.to_square + 64 * ((self.game.piece_type_at(move.to_square) - 1) + (0 if self.game.color_at(move.to_square) == 0 else 6))]
    
