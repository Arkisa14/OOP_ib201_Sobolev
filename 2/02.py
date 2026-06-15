class LeftParagraph:
    def __init__(self, width: int):
        self.field_width = width
        self.text = ['']
    
    def add_word(self, word: str):
        if len(self.text[-1] + ' ' + word) <= self.field_width:
            self.text[-1] += ' ' + word if self.text[-1] else word
        else:
            self.text.append(word)

    def end(self):
        print('\n'.join(self.text))

class RightParagraph:
    def __init__(self, width: int):
        self.field_width = width
        self.text = ['']
    
    def add_word(self, word: str):
        if len(self.text[-1] + ' ' + word) <= self.field_width:
            self.text[-1] += ' ' + word if self.text[-1] else word
        else:
            self.text.append(word)

    def end(self):
        for i in range(len(self.text)):
            self.text[i] = self.text[i].rjust(self.field_width)
        print('\n'.join(self.text))


