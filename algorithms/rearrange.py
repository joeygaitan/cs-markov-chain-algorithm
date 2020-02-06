import sys
import random  


def rearrange():
    newList = []

    words = sys.argv[1:]

    for i in sys.argv[1:]:
        word = random.choice(words)
        newList.append(word)
        words.remove(word)

    print(' '.join(newList))
    






