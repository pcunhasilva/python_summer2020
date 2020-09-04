# Fibonacci sequence
# X_[i] = X_[i-1] + X_[i-2], where X_1 = 1, X_2 = 1
# 1,1,2,3,5,8,....

# Write a for loop, while loop, or function (or all three!) to create a
# list of the first 10 numbers of the fibonacci sequence

def fibonacci(n):
	fin = []
	for i in range(0, n):
		if i == 0 or i == 1 :
			fin.append(1)
		else:
			# fin.append(fin[len(fin) - 1] + fin[len(fin) - 2])
			fin.append(fin[-1] + fin[-2])
	return fin	
fibonacci(0)
fibonacci(4)

"""return true if there is no e in 'word', else false"""
def has_no_e(word):
	if "e" not in word: 
		return True
	else:
		return False
has_no_e("me")
has_no_e("you")

"""return true if there is e in 'word', else false"""
def has_e(word):
	return not has_no_e(word)
has_e("me")
has_e("you")


"""return true if word1 contains only letters from word2, else false"""
def uses_only(word1, word2):
    word2_letters = [i for i in word2]
    word1_letters = [i for i in word1]
    if False in [i in word2_letters for i in word1_letters]:
    	return False
    else :
    	return True

uses_only(word1 = 'adb', word2 = 'ab')
uses_only('adb', 'abdc')

"""return true if word1 uses all the letters in word2, else false"""
def uses_all(word1, word2):
	word2_letters = [i for i in word2]
    word1_letters = [i for i in word1]
    if False in [i in word1_letters for i in word2_letters]:
    	return False
    else :
    	return True
uses_all('adb', 'ab')
uses_all('adb', 'abdc')

"""true/false is the word in alphabetical order?"""
def is_abecedarian(word):
	word_letters = [i for i in word]
	return sorted(word_letters) == word_letters

is_abecedarian('abdc')
is_abecedarian('kfga')
is_abecedarian('abde')