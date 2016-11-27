'''
Created on Nov 26, 2016

@author: thomas
'''

class Node(object):

    def __init__(self, params):
        self.indexSets = []
        self.parentIndexSet = None
        self.bestSet = None
        
    def addIndexSet(self, set):
        self.indexSets.append(set)
        
    def findBestIndexSetAndSendItUp(self):
        bestSet = None
        
        i = 0
        for set in self.indexSets:
            
            if i == 0:
                bestSet = set
            else:
                if set.rhymeValueForSet > bestSet.rhymeValueForSet:
                    bestSet = set
            
            i = i + 1
            
        self.bestSet = bestSet
        
        if self.parentIndexSet != None:
            self.parentIndexSet.addIndexes(bestSet.indexes, bestSet.rhymeValueForSet)
        
        
        
        
        
        