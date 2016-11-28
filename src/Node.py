'''
Created on Nov 26, 2016

@author: thomas
'''

class Node(object):

    def __init__(self):
        self.indexSets = []
        self.parentIndexSet = None
        self.bestSet = None
        
    def addIndexSet(self, set):
        self.indexSets.append(set)
        
    def findBestIndexSetAndSendItUp(self):
        best = None
        
        i = 0
        for set in self.indexSets:
            
            if i == 0:
                best = set
            else:
                if set.rhymeValueForSet > best.rhymeValueForSet:
                    best = set
            
            print i
            i = i + 1
           
        self.bestSet = best
        
        if self.parentIndexSet != None:
            self.parentIndexSet.addIndexes(best.indexes, best.rhymeValueForSet)
        
        
        
        
        
        