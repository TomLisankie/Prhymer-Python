'''
Created on Nov 26, 2016

@author: Thomas Lisankie
'''
import RhymeFinder

class Phoneme(object):

    def __init__(self, phonemeString):
        self.features = []
        self.phoneme = phonemeString
        self.stress = -1
        self.isAVowelPhoneme = False
        print self.phoneme
        
        if self.phoneme.endswith("0") or self.phoneme.endswith("1") or self.phoneme.endswith("2") or self.phoneme.endswith("3") or self.phoneme.endswith("4") or self.phoneme.endswith("5"):
            stressText = self.phoneme[len(self.phoneme) - 1 : len(self.phoneme)]
            print stressText
            self.phoneme = self.phoneme[0 : len(self.phoneme) - 1]
            print self.phoneme
            self.stress = int(stressText)
            self.isAVowelPhoneme = True
        
        self.features = RhymeFinder.RhymeFinder.features[self.phoneme]
        print "finished"
        
    def isEqualTo(self, p2):
        if self.phoneme == p2.phoneme:
            return True
        else:
            return False