'''
Created on Nov 23, 2016

@author: Thomas Lisankie
'''

import Phoneme

class Word(object):

    def __init__(self, wordName, phonemeString):
        
        self.wordName = wordName
        self.listOfPhonemes = []
        phonemes = phonemeString.split(" ")
        phonemes.pop()
        
        
        
        for phonemeString in phonemes:
            
            if phonemeString != '' or phonemeString != ' ':
                self.listOfPhonemes.append(Phoneme.Phoneme(phonemeString))
            
    def getVowelPhonemes(self):
        
        vowelPhonemes = []
        
        for phoneme in self.listOfPhonemes:
            if phoneme.isAVowelPhoneme:
                vowelPhonemes.append(phoneme)
        return vowelPhonemes
    
    def getVowelPhonemesAsString(self):
        vowelPhonemeString = "";
        vowelPhonemes = self.getVowelPhonemes()
        
        for vowel in vowelPhonemes:
            vowelPhonemeString = vowelPhonemeString + vowel.phoneme + " "
        return vowelPhonemeString
            
    
        
        
        