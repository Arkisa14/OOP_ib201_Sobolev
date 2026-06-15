class Selector:
    def __init__(self, values: list[int]):
        self.numbers = values

    def get_odds(self):
        return [num for num in self.numbers if num % 2 != 0]
    
    def get_evens(self):
        return [num for num in self.numbers if num % 2 == 0]

