class BoundingRectangle:
    def __init__(self):
        self.points = []
    
    def add_point(self, x: int, y: int):
        self.points.append((x, y))

    def width(self):
        return max(self.points)[0] - min(self.points)[0]
    
    def height(self):
        max_y = max(point[1] for point in self.points)
        min_y = min(point[1] for point in self.points)
        return max_y - min_y
    
    def bottom_y(self):
        return min(point[1] for point in self.points)
    
    def top_y(self):
        return max(point[1] for point in self.points)
    
    def left_x(self):
        return min(self.points)[0]
    
    def right_x(self):
        return max(self.points)[0]
    
