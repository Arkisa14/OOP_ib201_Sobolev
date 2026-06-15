class BigBell:
    def __init__(self):
        self.counter = 0

    def sound(self):
        if self.counter % 2 == 0:
            print("ding")
        else:
            print("dong")
        self.counter += 1