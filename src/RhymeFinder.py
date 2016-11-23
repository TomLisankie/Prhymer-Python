'''
Created on Nov 22, 2016

@author: Thomas Lisankie
'''
import math

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
            
            return self.findRhymePercentile(rhymeValue, anchor)
        
        else:
            
            if anchorOrSatellite == True:
                
                return self.idealRhymeValue(newWord, satellite)
            
            else:
                
                return self.idealRhymeValue(anchor, newWord)
        
    def idealRhymeValue(self, anchor, satellite):
        
        shorterWord = None
        longerWord = None
        
        if len(anchor.listOfPhonemes) < len(satellite.listOfPhonemes):
            
            shorterWord = anchor
            longerWord = satellite
            
        else:
            shorterWord = satellite
            longerWord = anchor
        
        idealRhymeValue = 0.0
        
        firstSearch = True
        foundStartingIndex = False
        layers = []
        nodesForThisLayer = []
        
        pastLayerNum = 0
        
        s = 0
        
        for shorterWordPhoneme in shorterWord.listOfPhonemes:
            
            weightTowardsWordEnd = 0.1
            
            #first search
            if firstSearch == True:
                
                startNode = Node.Node()
                
                l = 0
                
                for longerWordPhoneme in longerWord.listOfPhonemes:
                    
                    RVBetweenPhonemes = self.findRVBetweenPhonemes(shorterWordPhoneme, longerWordPhoneme, True, l * weightTowardsWordEnd)
                    
                    if RVBetweenPhonemes > 1:
                        
                        foundStartingIndex = True
                        
                        indexSet = RVIndexPair.RVIndexPair(l, RVBetweenPhonemes)
                        
                        startNode.addIndexSet(indexSet)
                    
                    l = l + 1
            
                if foundStartingIndex == True:
                    
                    nodesForThisLayer.append(startNode)
                    layers.append(Layer.Layer(nodesForThisLayer))
                    firstSearch = False
                
                nodesForThisLayer = []
            
            else:
                
                n = 0
                
                for node in layers[pastLayerNum].nodes:
                    
                    nodeBeingExamined = layers[0].nodes[n]
                    
                    i = 0
                    
                    for indexSet in nodeBeingExamined.indexSets:
                        
                        setBeingExamined = nodeBeingExamined.indexSets[i]
                        childNode = Node.Node()
                        indexToStartAt = setBeingExamined.indexes[0]
                        
                        if indexToStartAt + 1 == len(longerWord.listOfPhonemes):
                            print ""
                        else:
                            
                            l = indexToStartAt + 1
                            
                            for x in range(l, len(longerWord.listOfPhonemes)):
                                
                                RVBetweenPhonemes = self.findRVBetweenPhonemes(shorterWordPhoneme, longerWord.listOfPhonemes[x], True, l * weightTowardsWordEnd)
                                
                                if RVBetweenPhonemes > 1:
                                    
                                    indexSet = RVIndexPair.RVIndexPair(x, RVBetweenPhonemes)
                                    childNode.addIndexSet(indexSet)
                            
                            setBeingExamined.attachChildNode(childNode)
                            nodesForThisLayer.append(childNode)
                            
                        i = i + 1
                    
                    n = n + 1
            
                layers.append(Layer.Layer(nodesForThisLayer))
                nodesForThisLayer = []
                
                pastLayerNum = pastLayerNum + 1
            
            s = s + 1
        
        #find best path
        
        bestSet = None
        nodeBeingExamined = None
        
        l = len(layers)
        
        for x in range(l, 0):
            
            for node in layers[x].nodes:
                
                nodeBeingExamined = layers[x].nodes[n]
                
                if len(nodeBeingExamined.indexSets) > 0:
                    
                    nodeBeingExamined.findBestIndexSetAndSendItUp()
        
            if x == 0 and len(layers[x].nodes) == 1:
                
                bestSet = nodeBeingExamined.bestSet
        
        idealRhymeValue = bestSet.getRhymeValueForSet()
        
        rhymeValue = idealRhymeValue - self.findDeductionForIndexSet(bestSet, longerWord)
        
        return self.findRhymePercentile(rhymeValue, longerWord)
                
    def findRVBetweenPhonemes(self, p1, p2, addWeight, weight):
        
        p1Features = p1.features
        p2Features = p2.features
        biggerList = None
        
        if len(p1Features) >= len(p2Features):
            
            biggerList = p1Features
            
        else:
            
            biggerList = p2Features
            
        commonFeatures = list(set(p1Features).intersection(p2Features))
        
        difference = len(biggerList) - len(commonFeatures)
        
        if p1.isAVowelPhoneme and p2.isAVowelPhoneme:
            
            stressDifference = math.fabs(p1.stress - p2.stress)
            return 5.0 - difference - stressDifference
        
        elif p1.isAVowelPhoneme == False and p2.isAVowelPhoneme == False:
            
            commonFeaturesSize = len(commonFeatures)
            specialDifference = 0
            
            if p1.phoneme != p2.phoneme:
                
                if 9 in commonFeatures == False:
                    
                    specialDifference = specialDifference + 0.1
                    commonFeaturesSize = commonFeaturesSize - 1
                    
                if 2 in commonFeatures == False:
                    
                    specialDifference = specialDifference + 1
                    commonFeaturesSize = commonFeaturesSize - 1
                    
            difference = len(biggerList) - commonFeaturesSize
            
            return 2.0 - (0.15*difference) - specialDifference
        
        else:
            
            commonFeaturesSize = len(commonFeatures)
            specialDifference = 0
            
            if 9 in commonFeatures == False:
                    
                    specialDifference = specialDifference + 0.1
                    commonFeaturesSize = commonFeaturesSize - 1
                    
            if 2 in commonFeatures == False:
                    
                specialDifference = specialDifference + 1
                commonFeaturesSize = commonFeaturesSize - 1
                
            difference = len(biggerList) - commonFeaturesSize
            
            return 0.1*commonFeaturesSize + specialDifference
        
    def findRhymePercentile(self, rhymeValue, longerWord):
        
        homophonicRhymeValue = 0.0
        rhymePercentile = 0.0
        
        weightTowardsWordEnd = 0.1
        
        i = 0
        
        for phoneme in longerWord.listOfPhonemes:
            
            homophonicRhymeValue = homophonicRhymeValue + self.findRVBetweenPhonemes(phoneme, phoneme, True, i * weightTowardsWordEnd)
            
        rhymePercentile = rhymeValue / homophonicRhymeValue
        
        if(rhymePercentile < 0):
            
            rhymePercentile = 0.0
        
        return rhymePercentile
        
    def findDeductionForIndexSet(self, bestSet, longerWord):
        
        deduction = 0.0
        
        if bestSet.indexes[0] > 0:
            
            if bestSet.indexes[0] > 1:
                
                deduction = deduction + math.log10(bestSet.indexes[0])
                
            else:
                
                deduction = deduction + 0.25
        
        if len(longerWord.listOfPhonemes) - 1 - bestSet.indexes[len(bestSet.indexes) - 1] > 0:
            
            deduction = deduction + math.log10(len(longerWord.listOfPhonemes) - 1 - bestSet.indexes[len(bestSet.indexes) - 1])
            
        for i in range(0, len(bestSet.indexes) - 1):
            
            index1 = bestSet.indexes[i]
            index2 = bestSet.indexes[i + 1]
            
            deduction = deduction + (0.25 * (index2 - index1 - 1))
            
        return deduction        















