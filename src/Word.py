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
            print phonemes
            if phonemeString != '' or phonemeString != ' ':
                self.listOfPhonemes.append(Phoneme.Phoneme(phonemeString))
            
    '''def __init__(self, wordName, phonemes):
        
        self.wordName = wordName
        self.listOfPhonemes = phonemes
        '''
            
    
        
        
        