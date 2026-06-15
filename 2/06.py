class Rectangle:
    def __init__(self, x: int, y: int, w: int, h: int):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_w(self):
        return self.w
    
    def get_h(self):
        return self.h
    
    def intersection(self, other):
        left = max(self.x, other.x)
        right = min(self.x + self.w, other.x + other.w)
        bottom = max(self.y, other.y)
        top = min(self.y + self.h, other.y + other.h)
        
        width = right - left
        height = top - bottom
        
        if width <= 0 or height <= 0:
            return None
        
        return Rectangle(left, bottom, width, height)
    

