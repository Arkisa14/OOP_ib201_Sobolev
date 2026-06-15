class Summator:
    def transform(self, n: int):
        return n

    def sum(self, N: int):
        sum = 0
        for n in range(1, N+1):
            sum += self.transform(n)
        return sum

class SquareSummator(Summator):
    def transform(self, n: int):
        return n ** 2

class CubeSummator(Summator):
    def transform(self, n: int):
        return n ** 3