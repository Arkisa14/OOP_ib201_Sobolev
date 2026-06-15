class Queue:
    def __init__(self, *values):
        self.data = list(values)
    
    def append(self, *values):
        self.data.extend(values)
    
    def copy(self):
        return Queue(*self.data)
    
    def pop(self):
        if not self.data:
            return None
        return self.data.pop(0)
    
    def extend(self, queue):
        self.data.extend(queue.data)
    
    def next(self):
        return Queue(*self.data[1:])
    
    def __add__(self, other):
        return Queue(*(self.data + other.data))
    
    def __iadd__(self, other):
        self.data.extend(other.data)
        return self
    
    def __eq__(self, other):
        return self.data == other.data
    
    def __rshift__(self, n):
        return Queue(*self.data[n:])
    
    def __str__(self):
        return '[' + ' -> '.join(str(x) for x in self.data) + ']'
    
    def __next__(self):
        return self.next()
    
