'''
Created on Nov 22, 2016

@author: Thomas Lisankie
'''

import RhymeFinder
import Word

if __name__ == '__main__':
    pathToDict = "cmudict-0.7b_modified.txt"
    pathToFeatureSet = "features.txt"
    TESTING = 0
    finder = RhymeFinder.RhymeFinder(pathToDict, pathToFeatureSet)
    
    if TESTING == 0:
        print "Enter first word: "
        firstWordSpelling = raw_input()
        
        print "Enter second word: "
        secondWordSpelling = raw_input()
        
        firstWordComponents = firstWordSpelling.split()
        secondWordComponents = secondWordSpelling.split()
        
        firstWordPhonemeString = ""
        secondWordPhonemeString = ""
        
        for component in firstWordComponents:
            firstWordPhonemeString = firstWordPhonemeString + finder.dictionary[component.lower()] + " "
            
        for component in secondWordComponents:
            secondWordPhonemeString = secondWordPhonemeString + finder.dictionary[component.lower()] + " "
            
        firstWord = Word.Word(firstWordSpelling, firstWordPhonemeString)
        secondWord = Word.Word(secondWordSpelling, secondWordPhonemeString)
        
        print finder.findRhymeValueAndPercentileForWords(firstWord, secondWord) * 100 + "%"
        
    elif TESTING == 1:
        print 1    

