'''
Created on Nov 23, 2016

@author: Thomas Lisankie
'''

import Phoneme

class Word(object):

    def __init__(self, wordName, phonemeString):
        
        self.wordName = wordName
        phonemes = phonemeString.split(" ")
        
        self.listOfPhonemes = []
        
        for phonemeString in phonemes:
            
            self.listOfPhonemes.append(Phoneme.Phoneme(phonemeString))
            
    '''def __init__(self, wordName, phonemes):
        
        self.wordName = wordName
        self.listOfPhonemes = phonemes
        '''
            
    
        
        
        