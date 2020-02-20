from listogram import Listogram
from dictogram import Dictogram

class Histogram:
    def __init__(self):
        self.words = open('./text_files/words.txt','r')
        self.words = ''.join(self.words.readlines()).split()

        self.Listogram = Listogram(self.words)
        self.Dictogram = Dictogram(self.words)
    
    



new = Histogram()

print(new.listogram_samples(3))