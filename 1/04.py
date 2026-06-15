class OddEvenSeparator:
    def __init__(self):
        self.numbers = []

    def add_number(self, number: int):
        self.numbers.append(number)
    
    def even(self):
        return [num for num in self.numbers if num % 2 == 0]
    
    def odd(self):
        return [num for num in self.numbers if num % 2 != 0]
    