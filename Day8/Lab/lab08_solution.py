## Problem 1
## Write a function using recursion to calculate the greatest common divisor of two numbers

## Helpful link:
## https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
def gcd(a, b):
	## get remainder
	r = a % b
	## base case, no remainder
	## then that "divisor" is answer
	if r == 0:
		return b
	## otherwise, call function again with new inputs
	return gcd(b, r)
gcd(270, 192)

## Problem 2
## Write a function using recursion that returns prime numbers less than 121
def find_primes(me = 121, primes = []):
    if me == 2:
    	primes.append(2)
        return primes

    for i in range(2, me):
    	if me % i == 0:
        	break
    else:
    	primes.append(me)
    return find_primes(me-1, primes)
find_primes()

## Problem 3
## Write a function that gives a solution to Tower of Hanoi game
## https://www.mathsisfun.com/games/towerofhanoi.html

# Solution
# Source: https://www.cs.cmu.edu/~cburch/survey/recurse/hanoiimpl.html
def tower(disk, source, spare, dest):
    if disk == 1:
        print ("Move {} from {} to {}".format(disk, source, dest))
    else:
        tower(disk - 1, source, dest, spare)
        print ("Move {} from {} to {}".format(disk, source, dest)) 
        tower(disk - 1, spare, source, dest)

tower(disk = 3, source = 1, spare = 3, dest = 2)

#disk: number of disks
#source: where we start
#spare: position of the bar used to spare disk
#dest: first move




 