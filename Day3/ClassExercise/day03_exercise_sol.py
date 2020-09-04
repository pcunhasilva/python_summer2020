## Write a function that counts how many vowels are in a word
## Raise a TypeError with an informative message if 'word' is passed as an integer or float
## When done, run the test file in the terminal and see your results.
def count_vowels(word):
	if type(word) in [int, float]: 
			raise TypeError("This is an int or float. Input should be a str.")
	else:
		vowels = ['a', 'e', 'i', 'o', 'u']
		r = 0
		for i in word.lower():
			if i in vowels:
				r += 1
	return r
# count_vowels('dasrfe')
# count_vowels(1)