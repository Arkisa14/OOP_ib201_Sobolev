class Counter:
    def __init__(self, start=0):
        self._value = start
    
    def inc(self):
        self._value += 1
    
    def dec(self):
        self._value -= 1
    
    def value(self):
        return self._value

class LimitedCounter(Counter):
    def __init__(self, min_value, max_value, start=0):
        super().__init__(start)
        self.min_value = min_value
        self.max_value = max_value
    
    def inc(self):
        if self._value < self.max_value:
            super().inc()
    
    def dec(self):
        if self._value > self.min_value:
            super().dec()