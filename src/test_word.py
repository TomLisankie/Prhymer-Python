import unittest
import rhyme_finder
import word

class TestWord (unittest.TestCase):

    rf = rhyme_finder.RhymeFinder ("cmudict-0.7b_modified.txt", "features.txt")
    
    def testWordName (self):
        testWord = word.Word ("kindness", "K AY1 N D N AH0 S")
        self.assertEqual (testWord.wordName, "kindness", "Should be 'kindness'")

    def testPhonemeList (self):
        testWord = word.Word ("kindness", "K AY1 N D N AH0 S")
        self.assertEqual (len (testWord.listOfPhonemes), 7, "Should be 7")

    def testGetVowels (self):
        testWord = word.Word ("kindness", "K AY1 N D N AH0 S")
        vowelPhonemeList = testWord.getVowelPhonemes ()
        self.assertEqual (len (vowelPhonemeList), 2, "Should be 2")

    def testGetVowelString (self):
        testWord = word.Word ("kindness", "K AY1 N D N AH0 S")
        self.assertEqual (testWord.getVowelPhonemesAsString (), "AY AH ")

if __name__ == "__main__":
    unittest.main ()
