class table(object):
    def __init__(self, length = 10000000):
        self.array = [None] * length
        
    def hash(self, key):
        # Get the index of the item
        length = len(self.array)
        return hash(key) % length
        
    def add(self, key, value):
        # Add the item to the hashtable if not already present
        index = self.hash(key)
        if self.array[index] is not None:
            for i in range(len(self.array[index])):
                if self.array[index][i][0] == key:
                    self.array[index][i][1] = value
                    break
            else:
                self.array[index].append([key, value])
        else:
            self.array[index] = []
            self.array[index].append([key, value])
            
    def get(self, key):
        # Get the item from the hashtable
        index = self.hash(key)
        if self.array[index] is None:
            return None
        else:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]
            
            return None
