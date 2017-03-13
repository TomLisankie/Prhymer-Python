'''
Created on Nov 22, 2016

@author: Thomas Lisankie <link285@gmail.com>
'''
import math
import Word
import CartesianProduct
import OrderedPair

class RhymeFinder(object):
    '''
    classdocs
    '''

    features = {}

    def __init__(self, pathToDict, pathToFeatureSet):

        self.DEBUGGING = False
        self.dictionary = {}
        self.structureReference = {}
        self.wordList = []

        self.buildWords(pathToDict, pathToFeatureSet)

    def buildWords(self, pathToDict, pathToFeatureSet):

        linesOfDictionary = open(pathToDict, "r").read().splitlines()
        linesOfFeatureSet = open(pathToFeatureSet, "r").read().splitlines()

        l = 0

        for line in linesOfDictionary:

            components = line.split("  ")

            if len(components) != 2:
                print("The lines aren't separated by two spaces")
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

                print("The lines aren't separated by two spaces")
                break

            features = components[1].split(" ")
            featureInts = []

            for feature in features:
                if feature != "":
                    featureInts.append(int(feature))

            self.features[components[0]] = featureInts

    def findRhymePercentileForWords(self, word1, word2):

        rhymePercentile = 0.0
        longerWord = None

        'this conditional finds which word is longer and which is shorter'
        if len(word1.listOfPhonemes) < len(word2.listOfPhonemes):
            longerWord = word2
        else:
            longerWord = word1

        allRVs = []

        '1 - Find Cartesian product (shorterWord X longerWord)'
        cartesianProduct = CartesianProduct.CartesianProduct(word1, word2)

        '2 - Calculate RVs'
        echelon = 0
        while len(cartesianProduct.cartesianProductMatrix) != 0:

            echelon = len(cartesianProduct.cartesianProductMatrix) - 1

            allRVs.append(self.findBestRV(cartesianProduct, echelon, [], 0, len(cartesianProduct.cartesianProductMatrix[echelon]), len(longerWord.listOfPhonemes)))

            cartesianProduct.removeTopRow()

            '''resets rhyme values of OrderedPairs to their original value so
            that previous runthroughs of the findBestRV() method
            have no effect i.e. it makes sure it has the correct
            data to work with:'''

            cartesianProduct.resetOrderedPairRVs()
            echelon = 0

        rhymePercentile = self.findRhymePercentile(max(allRVs), longerWord)

        return rhymePercentile

    def findBestRV(self, cp, echelon, indexes, cumulative, bound, lSize):

        currentRow = cp.cartesianProductMatrix[echelon]

        for i in range(echelon, bound):
            currentRow[i].rhymeValue = currentRow[i].rhymeValue + cumulative

        bestPairForRow = None
        indexToAdd = 0
        for i in range(echelon, bound):
            if i == echelon:
                bestPairForRow = currentRow[i]
                indexToAdd = i
            else:
                if currentRow[i].rhymeValue > bestPairForRow.rhymeValue:
                    bestPairForRow = currentRow[i]
                    indexToAdd = i

        indexes.append(indexToAdd)
        #Problem is bestPairForRow is None
        if echelon == 0:
            bestPairForRow.indexes = indexes
            bestPairForRow.calculateGapPenalty(lSize)
            return bestPairForRow.rhymeValue
        else:
            echelon = echelon - 1
            return self.findBestRV(cp, echelon, indexes, bestPairForRow.rhymeValue, indexes[len(indexes) - 1], lSize)

    #Finds the rhyme value between any two given phonemes based on the intersection of their feature sets
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

                if 9 not in commonFeatures:

                    specialDifference = specialDifference + 0.1
                    commonFeaturesSize = commonFeaturesSize - 1

                if 2 in commonFeatures:

                    specialDifference = specialDifference + 1
                    commonFeaturesSize = commonFeaturesSize - 1

            difference = len(biggerList) - commonFeaturesSize

            return 2.0 - (0.15*difference) - specialDifference

        else:

            commonFeaturesSize = len(commonFeatures)
            specialDifference = 0

            if 9 not in commonFeatures:

                    specialDifference = specialDifference + 0.1
                    commonFeaturesSize = commonFeaturesSize - 1

            if 2 in commonFeatures:

                specialDifference = specialDifference + 1
                commonFeaturesSize = commonFeaturesSize - 1

            difference = len(biggerList) - commonFeaturesSize

            return (0.1*commonFeaturesSize) + specialDifference

    def findRhymePercentile(self, rhymeValue, longerWord):

        homophonicRhymeValue = 0.0
        rhymePercentile = 0.0

        weightTowardsWordEnd = 0.1

        i = 0

        for phoneme in longerWord.listOfPhonemes:

            homophonicRhymeValue = homophonicRhymeValue + self.findRVBetweenPhonemes(phoneme, phoneme, True, i * weightTowardsWordEnd)

            i = i + 1

        print(rhymeValue, homophonicRhymeValue)
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

        print(deduction)
        return deduction
