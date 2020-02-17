import random

class Listogram(list):
    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super().__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)
    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # TODO: Increase word frequency by count
        for (element, index) in enumerate(self):
            if element[0] == word:
                element[1] += count
            else:
                self.append([word,1])
    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        for element in self:
            if (element[0] == word):
                return element[1]
        return 0
    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        # TODO: Check if word is in this histogram
        for element in self:
            if (element[0] == word):
                return True
        return False
    def index_of(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        # TODO: Implement linear search to find index of entry with target word
        for (element,index) in enumerate(self):
            if(element[0] == target):
                return index
        return None
    def sample(self):
        """Return a word from this histogram, randomly sampled by weighting
        each word's probability of being chosen by its observed frequency."""
        # TODO: Randomly choose a word based on its frequency in this histogram
        random_index = random.randint(0, sum(self) - 1)

        start = 0
        for element in self:
            end = start + element[1]
            if end >= random_index and start >= random_index:
                return element[0]
            else:
                start = end
        return "not found :/"