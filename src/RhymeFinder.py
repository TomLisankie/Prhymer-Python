'''
Created on Nov 22, 2016

@author: Thomas Lisankie
'''

class RhymeFinder(object):
    '''
    classdocs
    '''
    
    def __init__(self, pathToDict, pathToFeatureSet):
        
        self.DEBUGGING = False
        self.dictionary = {}
        self.structureReference = {}
        self.wordList = []
        self.features = {}
        
        self.buildWords(pathToDict, pathToFeatureSet)
        
    def buildWords(self, pathToDict, pathToFeatureSet):
        
        linesOfDictionary = open(pathToDict, "r").read().splitlines()
        linesOfFeatureSet = open(pathToFeatureSet, "r").read().splitlines()
        
        l = 0
        
        for line in linesOfDictionary:
            
            components = line.split("  ")
            
            if len(components) != 2:
                print "The lines aren't separated by two spaces"
                break
            
            if components[0] == "#":
                self.structureReference[components[1]] = l - len(self.structureReference)
            else:
                lowerCaseWord = components[0].lower()
                self.wordList.append(lowerCaseWord)
                self.dictionary[lowerCaseWord] = components[1]
            
            
            l = l + 1
            
        l = 0
            
        for feature in linesOfFeatureSet:
            
            components = feature.split("  ")
            
            if len(components) != 2:
                
                print "The lines aren't separated by two spaces"
                break
            
            features = components[1].split(" ")
            featureInts = []
            
            for feature in features:
                if feature != "":
                    featureInts.append(int(feature))
                
            self.features[components[0]] = featureInts
            
    def findRhymeValueAndPercentileForWords(self, anchor, satellite):
        
        rhymePercentile = 0.0
        
        if len(anchor.listOfPhonemes) == len(satellite.listOfPhonemes):
            
            rhymePercentile = self.regularRhymeValue(anchor, satellite)
            
        else:
            
            rhymePercentile = self.idealRhymeValue(anchor, satellite)
            
        return rhymePercentile
    
    def regularRhymeValue(self, anchor, satellite):
        
        foundConsonantCluster = False
        anchorOrSatellite = False
        
        rhymeValue = 0.0
        
        newWord = None
        
        weightTowardsWordEnd = 0.1
        
        if anchor.listOfPhonemes[0].isAVowelPhoneme == False and anchor.listOfVowelPhonemes[0].isAVowelPhoneme == False and (anchor.listOfPhonemes[0].isEqualTo(satellite.listOfPhonemes[0] == False) and anchor.listOfPhonemes[1].isEqualTo(satellite.listOfPhonemes[1]) == False):
            
            foundConsonantCluster = True
            
            shortenedListOfPhonemes = anchor.listOfPhonemes[1:len(anchor.listOfPhonemes)]
            
            newWord = Word.Word(anchor.wordName, shortenedListOfPhonemes)
            
            anchorOrSatellite = True
            
        elif satellite.listOfPhonemes[0].isAVowelPhoneme == False and satellite.listOfVowelPhonemes[0].isAVowelPhoneme == False and (anchor.listOfPhonemes[0].isEqualTo(satellite.listOfPhonemes[0] == False) and anchor.listOfPhonemes[1].isEqualTo(satellite.listOfPhonemes[1]) == False):
            
            foundConsonantCluster = True
            
            shortenedListOfPhonemes = satellite.listOfPhonemes[1:len(anchor.listOfPhonemes)]
            
            newWord = Word.Word(satellite.wordName, shortenedListOfPhonemes)
            
            anchorOrSatellite = False
            
        if foundConsonantCluster == False:
            
            s = 0
            for phoneme in anchor.listOfPhonemes:
                
                rhymeValue = rhymeValue + self.findRVBetweenPhonemes(phoneme, satellite.listOfPhonemes[s], True, s*weightTowardsWordEnd)
                
                s = s + 1
        #No else because it's gonna be handled in the next if statement
        
        if foundConsonantCluster == False:
            
            return findRhymePercentile(rhymeValue, anchor)
        
        else:
            
            if anchorOrSatellite == True:
                
                return self.idealRhymeValue(newWord, satellite)
            
            else:
                
                return self.idealRhymeValue(anchor, newWord)
        
    def idealRhymeValue(self, anchor, satellite):
        print ""
        
    def findRVBetweenPhonemes(self, p1, p2, addWeight, weight):
        
        print ""        















