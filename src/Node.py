'''
Created on Nov 26, 2016

@author: thomas
'''

class Node(object):

    def __init__(self):
        self.indexSets = []
        self.parentIndexSet = None
        self.bestSet = None
        
    def addIndexSet(self, theSet):
        self.indexSets.append(theSet)
        
    def findBestIndexSetAndSendItUp(self):
        best = None
        
        i = 0
        for theSet in self.indexSets:
            
            if i == 0:
                best = theSet
            else:
                if theSet.rhymeValueForSet > best.rhymeValueForSet:
                    best = theSet
            
            print i
            i = i + 1
           
        self.bestSet = best
        
        if self.parentIndexSet != None:
            self.parentIndexSet.addIndexes(best.indexes, best.rhymeValueForSet)
        
        
        
        
        
        