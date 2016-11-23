'''
Created on Nov 22, 2016

@author: Thomas Lisankie
'''

class RhymeFinder(object):
    '''
    classdocs
    '''
    DEBUGGING = False
    dictionary = None
    structureReference = None
    wordList = None
    features = None
    
    def __init__(self, pathToDict, pathToFeatureSet):
        self.buildWords(pathToDict, pathToFeatureSet)
    def buildWords(self, pathToDict, pathToFeatureSet):
        print "Hellooooooo"
        linesOfDictionary = open("cmudict-0.7b_modified.txt", "r").read()
        print linesOfDictionary