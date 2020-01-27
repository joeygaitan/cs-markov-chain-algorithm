import sys
import random

number = sys.argv[1:]

words = list()
outPutList = list()

with open('words.txt','r') as f:
    for line in f:
        for word in line.split():
           word = word.rstrip()
           words.append(word)


for i in range(int(number[0])):
    randomNumber = random.randint(0,len(words))
    outPutList.append(words[randomNumber])
    words.remove(words[randomNumber])

print(' '.join(outPutList))





