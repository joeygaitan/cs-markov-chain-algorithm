from listogram import Listogram
from dictogram import Dictogram

class Histogram:
    def __init__(self):
        self.words = open('../../text_fileswords.txt','r')
        self.words = ''.join(self.words.readlines()).split()

        self.Listogram = Listogram(self.words)
        self.Dictogram = Dictogram(self.words)
    
    def listogram_samples(self, count):
        string = ""

        for _ in range(count):
            string += " " + self.Listogram.sample()
        return string

    def dictogram_samples(self,count):
        string = ""
        
        for _ in range(count):
            string += " " + self.Dictogram.sample()
        return string