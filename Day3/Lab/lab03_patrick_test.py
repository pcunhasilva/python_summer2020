import unittest
from lab03_patrick_answers import *

class lab3Code(unittest.TestCase):

    def setUp(self):
        self.txt_string_long = "Say hi."
        self.txt_string = "Say"
        self.txt_number = 234
        self.txt_piglatin = 'ultimate'

    # Test shout:

    def sadsadasd(self):
        self.assertEqual(shout(self.txt_string_long), "SAY HI!")

    def test_shout_string(self):
        self.assertEqual(shout(self.txt_string), "SAY!")

    def test_shout_string2(self):
        self.assertEqual(shout("blah"), "BLAH!")


    # Test reverse:
    def test_reverse_string(self):
        self.assertEqual(reverse(self.txt_string), "yaS")

    # Test reversewords:
    def test_reversewords_string(self):
        self.assertEqual(reversewords(self.txt_string_long), "hi. Say")

    # Test reversewordletters:
    def test_reversewordletters_string(self):
        self.assertEqual(reversewordletters(self.txt_string_long), "yaS .ih")

    def test_piglatin(self):
        self.assertEqual(piglatin(self.txt_string), "aySay")        
        self.assertEqual(piglatin(self.txt_piglatin), "ultimateyay")        

if __name__ == '__main__':
  unittest.main()