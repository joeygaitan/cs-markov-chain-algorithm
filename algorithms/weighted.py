import random
text = 'one fish two fish red fish blue fish'
word_counts = {'one': 1, 'fish': 4, 'two': 1,
               'red': 1, 'blue': 1}
               
def total(list):
    total = 0
    for element in list:
      total += element
    return total
               
def sample_by_frequency(word_counts):
    random_index = random.randint(0, total(word_counts.values()) - 1)
    # TODO: select a word based on frequency
    #how can we sample words using observed frequencies?
    start = 0
    for (word, count) in word_counts.items():
      end = start + count
      if end >= random_index and random_index >= start:
        print(weight(word, word_counts))
        return word
      else:
        start = end
    print(weight(word, word_counts))
    return word

def weight(word, histogram):
    mass = histogram[word] / total(word_counts.values())
    return f'{word} => {mass}'
    
print(sample_by_frequency(word_counts))