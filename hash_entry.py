class hash_entry:
    def __init__(self, eval, depth, moves):
        self.eval = eval
        self.depth = depth
        self.moves = moves
        
    def get_depth(self):
        return self.depth

    def get_eval(self):
        return self.eval
