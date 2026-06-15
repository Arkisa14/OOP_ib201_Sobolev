import datetime

class Date:
    def __init__(self, month: int, day: int):
        self.month = month
        self.day = day

    def __sub__(self, other):
        days1 = datetime.date(year=1, month=self.month, day=self.day)
        days2 = datetime.date(year=1, month=other.month, day=other.day)
        return (days1 - days2).days