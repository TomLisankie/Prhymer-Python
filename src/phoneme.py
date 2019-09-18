'''
Created on Nov 26, 2016

@author: Thomas Lisankie
'''
import rhyme_finder

class Phoneme(object):

    def __init__(self, phonemeString):
        self.features = []
        self.phoneme = phonemeString
        self.stress = -1
        self.isAVowelPhoneme = False
        
        if self.phoneme.endswith("0") or self.phoneme.endswith("1") or self.phoneme.endswith("2") or self.phoneme.endswith("3") or self.phoneme.endswith("4") or self.phoneme.endswith("5"):
            stressText = self.phoneme[len(self.phoneme) - 1 : len(self.phoneme)]
            
            self.phoneme = self.phoneme[0 : len(self.phoneme) - 1]
            
            self.stress = int(stressText)
            self.isAVowelPhoneme = True
        
        self.features = rhyme_finder.RhymeFinder.features[self.phoneme]
        
    def isEqualTo(self, p2):
        if self.phoneme == p2.phoneme:
            return True
        else:
            return False
