class AmericanDate:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day
    
    def set_year(self, year: int):
        self.year = year
    
    def set_month(self, month: int):
        self.month = month
    
    def set_day(self, day: int):
        self.day = day
    
    def get_year(self):
        return self.year
    
    def get_month(self):
        return self.month
    
    def get_day(self):
        return self.day
    
    def format(self):
        return f'{self.month:02d}.{self.day:02d}.{self.year}'

class EuropeanDate:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day
    
    def set_year(self, year: int):
        self.year = year
    
    def set_month(self, month: int):
        self.month = month
    
    def set_day(self, day: int):
        self.day = day
    
    def get_year(self):
        return self.year
    
    def get_month(self):
        return self.month
    
    def get_day(self):
        return self.day
    
    def format(self):
        return f'{self.day:02d}.{self.month:02d}.{self.year}'
    
 