words = open('words.txt','r')
words = ''.join(words.readlines()).split()

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

def frequency():
    

print(histogram(words))
