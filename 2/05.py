class Table:
    def __init__(self, row: int, col: int):
        self.rows = row
        self.cols = col
        self.data = [[0] * col for _ in range(row)]
    
    def get_value(self, row: int, col: int):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        return None
    
    def set_value(self, row: int, col: int, value: int):
        self.data[row][col] = value
    
    def n_rows(self):
        return self.rows
    
    def n_cols(self):
        return self.cols
    
