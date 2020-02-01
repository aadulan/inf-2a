import unittest
from pos_tagging import *

class Test(unittest.TestCase):

    def test_unchanging_plurals(self):
        m = unchanging_plurals()
        self.assertListEqual(['sheep', 'moose', 'police', 'series', 'fish', 'multimedia', 'deer', 'headquarters', 'marijuana', 'salmon', 'cannabis', 'bison', 'swine', 'dna', 'buffalo', 'species', 'trout'], m)

    def test_noun_stem(self):
        m1 = noun_stem("sheep")
        m2 = noun_stem("buffalo")

        self.assertEqual(m1, "sheep")
        self.assertEqual(m2, "buffalo")

        m3 = noun_stem("men")
        m4 = noun_stem("women")
        m5 = noun_stem("policemen")

        self.assertEqual(m3, "man")
        self.assertEqual(m4, "woman")
        self.assertEqual(m5, "policeman")

        m6 = noun_stem("dogs")
        m7 = noun_stem("countries")
        m8 = noun_stem("ashes")

        self.assertEqual(m6, "dog")
        self.assertEqual(m7, "country")
        self.assertEqual(m8, "ash")

    # def test_tag_word(self):
    #
    #     self.assertEqual()

if __name__ == '__main__':
    unittest.main()
