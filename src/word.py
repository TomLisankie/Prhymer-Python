'''
Created on Nov 23, 2016

@author: Thomas Lisankie
'''

import phoneme

class Word(object):

    def __init__(self, wordName, phonemeString):
        
        self.wordName = wordName
        self.listOfPhonemes = []
        phonemes = phonemeString.split(" ")
        
        for phonemeString in phonemes:
            if phonemeString != "" and phonemeString != " ":
                self.listOfPhonemes.append(phoneme.Phoneme(phonemeString))
            
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
            
    
        
        
        
