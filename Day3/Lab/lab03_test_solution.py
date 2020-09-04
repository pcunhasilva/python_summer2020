import unittest
from lab03_solution import *

class labTests(unittest.TestCase):
  def test_shout(self):
    self.assertEqual("HELLO!", shout("hello"))
    self.assertNotEqual("Hello!", shout("hello"))
    with self.assertRaises(StringException): shout(5)
  def test_reverse(self):
    self.assertEqual("olleh", reverse("hello"))
  def test_reversewords(self):
    self.assertEqual("there Hello", reversewords("Hello there"))
    with self.assertRaises(MultipleWordException): reversewords("hello")
  def test_reversewordletters(self):
    self.assertEqual("olleh ereht", reversewordletters("hello there"))
    self.assertEqual("olleh", reversewordletters("hello"))
  def test_piglatin(self):
    self.assertEqual("enryday", piglatin("ryden"))
    self.assertEqual("obbay", piglatin("bob"))
    self.assertEqual("en and bobryday", piglatin("ryden and bob"))
    self.assertNotEqual("joe", piglatin("joe"))

if __name__ == '__main__':
  unittest.main()

