class SquareFunction:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x: int):
        return self.a * x ** 2 + self.b * x + self.c