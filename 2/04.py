class MinStat:
    def __init__(self):
        self.counter = 0
        self.current_min = None

    def add_number(self, number: int) -> None:
        if self.counter == 0:
            self.current_min = number
        elif number < self.current_min:
            self.current_min = number
        self.counter += 1

    def result(self):
        return self.current_min

class MaxStat:
    def __init__(self):
        self.counter = 0
        self.current_max = None

    def add_number(self, number: int) -> None:
        if self.counter == 0:
            self.current_max = number
        elif number > self.current_max:
            self.current_max = number
        self.counter += 1

    def result(self):
        return self.current_max

class AverageStat:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add_number(self, number: int) -> None:
        self.total += number
        self.count += 1

    def result(self):
        if self.count == 0:
            return None
        return self.total / self.count