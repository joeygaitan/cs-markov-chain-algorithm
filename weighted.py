import random
text = 'one fish two fish red fish blue fish'
word_counts = {'one': 1, 'fish': 4, 'two': 1,
               'red': 1, 'blue': 1}
               
def total(list):
    total = 0
    for element in list:
      total += element
    return total
               
def sample_by_frequency(histogram):
    random_index = random.randint(0, total(word_counts.values()) - 1)
    # TODO: select a word based on frequency
    #how can we sample words using observed frequencies?
    start = 0
    for (word, count) in word_counts.items():
      end = start + count
      if end >= random_index and random_index >= start:
        return word
      else:
        start = end
    return word
    
print(sample_by_frequency(word_counts))