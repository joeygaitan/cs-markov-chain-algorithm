import os
import sys
import random
import time as t

start_time = t.time()

words = open('words.txt','r')
words = ''.join(words.readlines()).split()

word = sys.argv[1:]

def list_histogram(words):
    histo = []

    for word in words:
        word = word.rstrip()
        if len(histo) == 0:
            histo.append([word,1])
        else:
            for element in histo:
                if element[0] == word:
                    element[1] += 1
                else:
                    histo.append([word,1])

def dict_histogram(words):
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
    histograms = dict_histogram(words)
    
    if word in histograms:
        print(f'Word Found: {word}, Word Count: {histograms[word]}') 
    else:
        print(f'{word} not found')

end_time = t.time()
    
print(f"The program ran for {end_time - start_time} seconds")

# print(histogram(words))

print(frequency(word[0]))
