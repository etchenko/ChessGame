class table(object):
    def __init__(self, length = 10):
        self.array = [None] * length
        
    def hash(self, key):
        length = len(self.array)
        return hash(key) % length
        
    def add(self, key, value):
        index = self.hash(key)
        if self.array[index] is not None:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    kvp[1] = value
                    break
            else:
                self.array[index].append([key, value])
        else:
            self.array[index] = []
            self.array[index].append([key, value])
            
    def get(self, key):
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]
            
            raise KeyError()
    
class item:
    def __init__(self, eval, depth):
        self.eval = eval
        self.depth = depth
        
    def getdepth(self):
        return self.depth
    
    def geteval(self):
        return self.eval
