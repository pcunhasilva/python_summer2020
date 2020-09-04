import unittest
from day03_exercise_sol import *

class Test_count_vowels(unittest.TestCase):
	
	def test_equal(self): 
		self.assertEqual(count_vowels('FOO'), 2)
	
	def test_not_string(self):
		with self.assertRaises(TypeError): 
			count_vowels(5)
		

if __name__ == '__main__': 
	unittest.main()