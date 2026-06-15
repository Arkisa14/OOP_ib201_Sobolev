class Table:
    def __init__(self, rows: int, cols: int):
        self.data = [[0] * cols for _ in range(rows)]
    
    def get_value(self, row: int, col: int):
        if 0 <= row < len(self.data) and 0 <= col < len(self.data[0]):
            return self.data[row][col]
        return None
    
    def set_value(self, row: int, col: int, value: int):
        self.data[row][col] = value
    
    def n_rows(self):
        return len(self.data)
    
    def n_cols(self):
        return len(self.data[0]) if self.data else 0
    
    def delete_row(self, row: int):
        del self.data[row]
    
    def delete_col(self, col: int):
        for row in self.data:
            del row[col]
    
    def add_row(self, row: int):
        cols = self.n_cols()
        self.data.insert(row, [0] * cols)
    
    def add_col(self, col: int):
        for row in self.data:
            row.insert(col, 0)

