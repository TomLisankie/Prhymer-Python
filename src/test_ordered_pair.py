import unittest
import rhyme_finder
import ordered_pair
import phoneme

class TestOrderedPair (unittest.TestCase):

    rf = rhyme_finder.RhymeFinder ("cmudict-0.7b_modified.txt", "features.txt")
    
    def testHomophoneRhymeValues (self):
       testPair = ordered_pair.OrderedPair (phoneme.Phoneme ("AH1"), phoneme.Phoneme ("AH1"), 0)
       self.assertEqual (testPair.originalRhymeValue, 5.0, "Should be 5.0")

       testPair = ordered_pair.OrderedPair (phoneme.Phoneme ("CH"), phoneme.Phoneme ("CH"), 0)
       self.assertEqual (testPair.originalRhymeValue, 2.0, "Should be 2.0")

    def testSameVowelsWithDifferentStress (self):
        testPair = ordered_pair.OrderedPair (phoneme.Phoneme ("AH2"), phoneme.Phoneme ("AH1"), 0)
        self.assertEqual (testPair.originalRhymeValue, 4.0, "Should be 4.0")

    def testCalculateGapPenalty (self):
        testPair = ordered_pair.OrderedPair (phoneme.Phoneme ("AH1"), phoneme.Phoneme ("AH1"), 0)
        self.assertEqual (testPair.calculateGapPenalty (0), 4.25, "Should be 4.25")
        
if __name__ == "__main__":
    unittest.main ()
