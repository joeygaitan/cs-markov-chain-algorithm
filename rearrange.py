import sys
import random  

newList = []

words = sys.argv[1:]

for i in sys.argv[1:]:
    word = random.choice(words)
    newList.append(word)
    words.remove(word)

print(newList)
    






