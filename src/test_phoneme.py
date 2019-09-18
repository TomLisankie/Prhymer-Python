import unittest
import rhyme_finder
import phoneme

class TestPhoneme (unittest.TestCase):
    rf = rhyme_finder.RhymeFinder ("cmudict-0.7b_modified.txt", "features.txt")

    def testPhonemeString (self):
        test_phoneme = phoneme.Phoneme ("AA1")
        self.assertEqual (test_phoneme.phoneme, "AA", "Should be 'AA'")

    def testStress (self):
        test_phoneme = phoneme.Phoneme ("AA1")
        self.assertEqual (test_phoneme.stress, 1, "Should be 1")
        self.assertEqual (test_phoneme.isAVowelPhoneme, True, "Should be True")

        test_phoneme = phoneme.Phoneme ("CH")
        self.assertEqual (test_phoneme.stress, -1, "Should be -1")

        test_phoneme = phoneme.Phoneme ("AA11")
        self.assertEqual (test_phoneme.stress, -1, "Should be -1")

    def testIsAVowel (self):
        test_phoneme = phoneme.Phoneme ("AA1")
        self.assertEqual (test_phoneme.isAVowelPhoneme, True, "Should be True")

        test_phoneme = phoneme.Phoneme ("CH")
        self.assertEqual (test_phoneme.isAVowelPhoneme, False, "Should be False")

        test_phoneme = phoneme.Phoneme ("AA11")
        self.assertEqual (test_phoneme.isAVowelPhoneme, False, "Should be False")

    def testFeatures (self):
        test_phoneme = phoneme.Phoneme ("CH")
        self.assertEqual (test_phoneme.features, [1, 4, 15, 17, 18], "Should be [1, 4, 15, 17, 18]")

if __name__ == "__main__":
    unittest.main ()
