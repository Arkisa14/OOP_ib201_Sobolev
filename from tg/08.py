class User:
    _counter = 0
    
    def __init__(self, name):
        self.name = name
        self.id = None
    
    @classmethod
    def create(cls, name):
        cls._counter += 1
        user = cls(name)
        user.id = cls._counter
        return user
    
    @classmethod
    def count(cls):
        return cls._counter