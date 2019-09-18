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

        cutOff = 0
        for char in phonemeString:
            if char.isdigit():
                break
            cutOff += 1

        stressText = self.phoneme[cutOff : len(self.phoneme)]

        if stressText.isdigit ():
            self.stress = int (stressText)
        
        if self.stress >= 0 and self.stress <= 5:
            self.isAVowelPhoneme = True
        else:
            self.stress = -1
            
        self.phoneme = self.phoneme[0 : cutOff]
        
        self.features = rhyme_finder.RhymeFinder.features[self.phoneme]
        
    def isEqualTo(self, p2):
        if self.phoneme == p2.phoneme:
            return True
        else:
            return False
