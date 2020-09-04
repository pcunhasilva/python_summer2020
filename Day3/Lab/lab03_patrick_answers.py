# Create the following functions: with exceptions, errors, and such
# Create a test for those functions

## make all characters capitalized
def shout(txt):
    if type(txt) != str:
        raise TypeError('Not a string')
    else:
        txt = txt.replace(".", "!").upper()
        if txt[-1] != "!": 
            txt = txt + "!"
        return txt
# shout(111)
# shout('dsds')

## reverse all characters in string
def reverse(txt):
    if type(txt) != str:
        raise TypeError('Not a String')
    else:
        txt = txt[::-1]
    return txt
# reverse('Hello World')
# reverse(212)


## reverse word order in string
def reversewords(txt):
    txt = str(txt)
    if len(txt.split()) == 1:
        raise RuntimeError("Please insert more than one word.")
    return " ".join(txt.split()[ : : -1])
# reversewords('Hello World')    
# reversewords('Hello')         

## reverses letters in each word
def reversewordletters(txt):
    if type(txt) != str: raise TypeError('Not a String')
    return ' '.join([reverse(i) for i in txt.split()])
# reversewordletters('Hello World') 
# reversewordletters(['Hello', 'World'])         


## change text to piglatin.. google it! 
def piglatin(txt):
    if type(txt) != str: raise TypeError('Not a String')
    if list(txt)[0] not in ['a', 'e', 'i', 'o', 'u', 'y'] and list(txt)[1] not in ['a', 'e', 'i', 'o', 'u', 'y']:
        for i in range(len(txt)):
            if list(txt)[i] in ['a', 'e', 'i', 'o', 'u',  'y']:
                return txt[(i):] + txt[0:(i)] + 'ay'
    elif list(txt)[0] not in ['a', 'e', 'i', 'o', "u", 'y']:
        return txt[1:] + list(txt)[0] + 'ay'
    else:
        for i in range(len(txt)):
            if list(txt)[i] in ['a', 'e', 'i', 'o', 'u', 'y']:
                return txt[(i):] + txt[0:(i)] + 'yay'

piglatin('eat')
piglatin('smile')
piglatin('pig')
piglatin('ultimate')

# Try/catch is more common when using
## someone else's code, scraping, etc. -----------------------------------

## Loop over this string and apply the reverse() function.
## Should throw errors if your exceptions are being raised!
## Write a try/catch to handle this.
 
string_list = ["hi", "hello there", 5, "hope this works", 100, "will it?"]

# reverse_list = []
# for i in string_list:
#     try:
#         r = reverse(i)
#     except TypeError as err:
#         print("{} is not a {}".format(i, err))
#         r = None
#     reverse_list.append(r)
# print(reverse_list)




