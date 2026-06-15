class MinMaxWordFinder:
    def __init__(self):
        self.words = []

    def add_sentence(self, sentence: str):
        self.words += sentence.split()

    def shortest_words(self):
        if not self.words:
            return []
        min_length = len(min(self.words, key=len))
        return sorted([word for word in self.words if len(word) == min_length])

    def longest_words(self):
        if not self.words:
            return []
        max_length = len(max(self.words, key=len))
        return sorted(set([word for word in self.words if len(word) == max_length]))
