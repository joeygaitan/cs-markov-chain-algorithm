words = open('words.txt','r')
words = ''.join(words.readlines()).split()

def histogram(words):
    histo = {}

    for word in words:
        word = word.rstrip()
        if word in histo:
            print(f'word {word}, value{histo[word]}')
            histo[word] += 1
        else:
            histo[word] = 1
        print(f'word {word}, value {histo[word]}')
    return histo

print(histogram(words))
