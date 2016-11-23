'''
Created on Nov 22, 2016

@author: Thomas Lisankie
'''

import RhymeFinder

if __name__ == '__main__':
    pathToDict = "cmudict-0.7b_modified.txt"
    pathToFeatureSet = "features.txt"
    finder = RhymeFinder.RhymeFinder(pathToDict, pathToFeatureSet)
    print "done"