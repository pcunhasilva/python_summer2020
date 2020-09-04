import string
## 1. write tests in lab03_tests.py
## 2. then code for the following functions

## Raising errors is more common when developing ------------------------

## These functions all take a single string as an argument.
## Even though your code might work for an int, or you could easily do str(),
## raise a built-in (or custom!) exception if fed an int


class StringException(Exception):
  def __init__(self, value):
    Exception.__init__(self, "%s is not text!" %value)

class MultipleWordException(Exception):
  def __init__(self, value):
    Exception.__init__(self, "%s is only one word!" %value)


## make all characters capitalized
def shout(txt):
  if not isinstance(txt, str):
    raise StringException(txt)
  return txt.upper() + "!"

## reverse all characters in string
def reverse(txt):
  if not isinstance(txt, str):
    raise StringException(txt)
  return txt[::-1]
	
## reverse word order in string
def reversewords(txt):
  if " " not in txt:
    raise MultipleWordException(txt)
  words = txt.split()
  return ' '.join(words[::-1])


## reverses letters in each word (maintain order)
def reversewordletters(txt):
  words = txt.split()
  output = []
  for w in words:
    output.append(reverse(w))
  return ' '.join(output)
		
## change text to piglatin.. google it! 
def piglatin(txt):
  try:
    vowels = ['a', 'e', 'i', 'o', 'u']
    first_vowel = [i in vowels for i in txt].index(True)
  except ValueError:
    first_vowel = [i == 'y' for i in txt].index(True)
  ordering = [i for i in range(first_vowel, len(txt))]
  ordering.extend(range(0, first_vowel))
  result = [i for i in map(txt.__getitem__, ordering)]
  result.extend('ay')
  return ''.join(result)





## Try/catch is more common when using packages, scraping, etc. -----------------------------------

## Loop over this list and apply the reverse() function.
## Should throw errors if your exceptions are being raised!
## Write a try/catch to handle this.
 
string_list = ["hi", "hello there", 5, "hope this works", 100, "will it?"]


reverse_list = []
for s in string_list:
  try:
    r = reverse(s)
  except StringException as err:
    print(err)
    r = None
  finally:
    reverse_list.append(r)




		
			
			
			
			
			
			

