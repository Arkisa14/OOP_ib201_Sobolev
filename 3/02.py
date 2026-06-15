class ReversedList:
    def __init__(self, _list: list):
        self.reversed_list = _list[::-1]

    def __len__(self):
        return len(self.reversed_list)
    
    def __getitem__(self, key):
        return self.reversed_list[key]