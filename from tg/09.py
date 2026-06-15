class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    
    @classmethod
    def from_string(cls, s):
        x, y = s.split(',')
        return cls(float(x.strip()), float(y.strip()))
    
    @classmethod
    def from_dict(cls, d):
        return cls(d['x'], d['y'])
    
    @staticmethod
    def distance(a, b):
        return round(((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5, 2)