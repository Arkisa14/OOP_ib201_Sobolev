class GameSettings:
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not GameSettings._initialized:
            self.volume = 50
            self.difficulty = 'Normal'
            GameSettings._initialized = True
    
    @classmethod
    def get_instance(cls):
        return cls()