import random

class Dictogram(dict):
    def __init__(self, word_list=None):
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any

        

        super().__init__()
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # TODO: Increase word frequency by count
        if word in self:
            self[word] += count
            self.tokens += count
        else:
            self.tokens += count
            self.types += 1
            self[word] = count

        
    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        if word in self:
            return self[word]
        else:
            return 0

    def sample(self):
        """Return a word from this histogram, randomly sampled by weighting
        each word's probability of being chosen by its observed frequency."""
        # TODO: Randomly choose a word based on its frequency in this histogram
        random_index = random.randint(0, sum(self.values()) - 1)
        start = 0
        for (word, count) in self.items():
            end = start + count
            if end >= random_index and start >= random_index:
                return word
            else:
                start = end

    def dictogram_samples(self,count):
        string = self.sample()
        
        for _ in range(count - 1):
            string += " " + self.sample()
        return string
