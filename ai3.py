import chess
from human import human
import random
import time
from table import table
from item import item

# Same as ai, but make move within method
class ai3:
    def __init__(self):
        self.max_depth = 2
        self.time_limit = 5
        self.rand = [round(random.random()*10000000000000000) for i in range(768)]
        # Pawns 0 & 6
        # Knight 1 & 7
        # Bishop 2 & 8
        # Rook 3 & 9
        # Queen 4 & 10
        # King 5 & 11
        
    def make_move(self, game):
        start = time.time()
        self.distance = 1
        self.max_q = 11
        hash = self.get_hashkey(game)
        self.table = table()
        self.count = game.fullmove_number
        while time.time() < start + self.time_limit:
            move = self.iterative_root(game, start + self.time_limit, hash)
            self.distance += 1
            self.max_q += 1
        return move
        
        
    def iterative_root(self, game, time, hash):
        moves = list(game.legal_moves)
        max = [-10000, 0]
        for i in range(len(moves)):
            value = self.move_value(game, -10000, 10000, 1, moves[i], hash)
            if value > max[0]:
                max[0] = value
                max[1] = moves[i]
        return max[1]
        
        
    def move_value(self, game, alpha, beta, depth, move, hash):
        value = 0
        hash_new = self.mod_hashkey(hash, move, game)
        last = self.table.get(hash_new)
        if last is not None:
            if last.depth >= depth:
                return last.eval
        
        #if depth > self.max_q:
            #value = self.eval(game)
        if depth > self.max_depth and not game.gives_check(move) and not game.is_capture(move) and not game.is_check():
                value = self.eval(game)
        else:
            game.push(move)
            if game.is_game_over():
                if game.is_checkmate():
                    value = 9999 if game.turn else -9999
            elif game.turn:
                value = self.min_val(game, alpha, beta, depth, move, hash_new)
            else:
                value = self.max_val(game, alpha, beta, depth, move, hash_new)
            game.pop()
        board = item(value, depth, self.count)
        self.table.add(hash_new, board)
        return value
        
    def min_val(self, game, alpha, beta, depth, move, hash):
        min_val = 10000
        moves = list(game.legal_moves)
        for i in range(len(moves)):
            val = self.move_value(game, alpha, beta, depth + 1, moves[i], hash)
            min_val = min(val, min_val)
            beta = min(val, beta)
            if beta <= alpha:
                break
        return min_val


    def max_val(self, game, alpha, beta, depth, move, hash):
        max_val = -10000
        moves = list(game.legal_moves)
        for i in range(len(moves)):
            val = self.move_value(game, alpha, beta, depth + 1, moves[i], hash)
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
        
    def get_hashkey(self, board):
        key = 0
        for i in range(2):
            for j in range(1,7):
                pos = list(board.pieces(j, True if i == 0 else False))
                for k in pos:
                    key ^= self.rand[k + 64 * ((j - 1) + (0 if i == 0 else 6))]
        return key
        
    def mod_hashkey(self, hash, move, board):
        # Modifies the hash key to include the move that has not been made yet
        #m = chess.Move.from_uci(move)
        hash ^= self.rand[move.from_square + 64 * ((board.piece_type_at(move.from_square) - 1) + (0 if board.color_at(move.from_square) == 0 else 6))]
        hash ^= self.rand[move.to_square + 64 * ((board.piece_type_at(move.from_square) - 1) + (0 if board.color_at(move.from_square) == 0 else 6))]
        if board.piece_type_at(move.to_square) is not None:
            hash ^= self.rand[move.to_square + 64 * ((board.piece_type_at(move.to_square) - 1) + (0 if board.color_at(move.to_square) == 0 else 6))]
        return hash
