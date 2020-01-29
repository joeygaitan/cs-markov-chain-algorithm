import os
import sys

import time as t

start_time = t.time()

words = open('words.txt','r')
words = ''.join(words.readlines()).split()

word = sys.argv[1:]

def histogram(words):
    histo = {'histoCounter':0}

    for word in words:
        word = word.rstrip()
        if word in histo:
            histo[word] += 1
        else:
            histo['histoCounter'] += 1
            histo[word] = 1
    print(unique_word(histo['histoCounter']))
    return histo

def unique_word(count):
    return (f'the amount of unique words are {count}')

def frequency(word):
    histograms = histogram(words)
    
    if word in histograms:
        print(f'Word Found: {word}, Word Count: {histograms[word]}') 
    else:
        print(f'{word} not found')

end_time = t.time()
    

# print(histogram(words))

print(frequency(word[0]))

print(f"The program ran for {end_time - start_time} seconds")