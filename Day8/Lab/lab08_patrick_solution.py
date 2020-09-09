#Exercise 1
#Write a function to calculate the greatest common divisor of two numbers
def gcd(num1, num2):
    if min(num1, num2) == 0: return max(num1, num2)
    if max(num1, num2) % min(num1, num2) == 0: return min(num1, num2)
    return gcd(min(num1, num2), max(num1, num2) % min(num1, num2))
gcd(192, 270)
gcd(270, 192)

#Exercise 2
#Write a function that returns prime numbers less than 121
def findprime(num, prime = []):
    if num == 1: return None
    i = 1
    remainder = []
    if num == 2: 
        prime.append(2)
        prime.reverse()
        return prime
    while i <= num:
        remainder.append(num % i)
        i += 1
    # num % 1 and num % num are the only instances of remainder = 0        
    if remainder.count(0) < 3: prime.append(num)
    return findprime(num - 1)

def findprime2(num):
    if 'prime' not in globals():
        global prime
        prime = []
    if num == 2:
        prime.append(num)
        prime.reverse()
        result = prime
        del globals()['prime']
        return result
    i = 1
    remainder = []
    while i <= num:
        remainder.append(num % i)
        i += 1
    # num % 1 and num % num are the only instances of remainder = 0
    if remainder.count(0) < 3: prime.append(num)
    return findprime2(num - 1)

# This is the one that only prints
findprime(121)
# This is the one that stores
findprime2(121)

# Exercise 3
# Write a function that gives a solution to Tower of Hanoi game
# https://www.mathsisfun.com/games/towerofhanoi.html

# Solution:
# Source: https://www.cs.cmu.edu/~cburch/survey/recurse/hanoiimpl.html
def tower(disk, source, spare, dest):
    if disk == 1:
        print ("Move {} from {} to {}".format(disk, source, dest))
    else:
        tower(disk - 1, source, dest, spare)
        print ("Move {} from {} to {}".format(disk, source, dest)) 
        tower(disk - 1, spare, source, dest)

tower(disk = 5, source = 1, spare = 3, dest = 2)

# disk: number of disks
# source: where we start
# spare: position of the bar used to spare disk
# dest: first move


