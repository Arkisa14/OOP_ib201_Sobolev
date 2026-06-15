class SparseArray:
    def __init__(self):
        self.data = {}
    
    def __setitem__(self, index, value):
        if value != 0:
            self.data[index] = value
        elif index in self.data:
            del self.data[index]
    
    def __getitem__(self, index):
        return self.data.get(index, 0)