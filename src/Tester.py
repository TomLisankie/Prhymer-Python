'''
Created on Nov 22, 2016

@author: Thomas Lisankie
'''

import RhymeFinder

if __name__ == '__main__':
    pathToDict = "cmudict-0.7b_modified.txt"
    pathToFeatureSet = "features.txt"
    TESTING = 0
    finder = RhymeFinder.RhymeFinder(pathToDict, pathToFeatureSet)
    
    if TESTING == 0:
        print 0
        
    elif TESTING == 1:
        print 1    

