import sys
import random

import time as t

start_time = t.time()

def randomwords():

    number = sys.argv[1:]

    words = list()
    outPutList = list()

    words = open('words.txt','r')
    words = ''.join(words.readlines()).split()
    


    for i in range(int(number[0])):
        randomNumber = random.randint(0,len(words))
        outPutList.append(words[randomNumber])
        words.remove(words[randomNumber])

    print(' '.join(outPutList))

randomwords()
    
end_time = t.time()

print(f"The program ran for {end_time - start_time} seconds")







