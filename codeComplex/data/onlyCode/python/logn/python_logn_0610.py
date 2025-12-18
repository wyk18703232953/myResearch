import io, sys, atexit, os
import math as ma
from sys import exit
from decimal import Decimal as dec
from itertools import permutations
from itertools import combinations


def li ():
	return list (map (int, input ().split ()))


def num ():
	return map (int, input ().split ())


def nu ():
	return int (input ())


def find_gcd ( x, y ):
	while (y):
		x, y = y, x % y
	return x


def lcm ( x, y ):
	gg = find_gcd (x, y)
	return (x * y // gg)


mm = 1000000007
yp = 0


def isPrime ( n ):
	# Corner cases
	if (n <= 1):
		return False
	if (n <= 3):
		return True

	# This is checked so that we can skip
	# middle five numbers in below loop
	if (n % 2 == 0 or n % 3 == 0):
		return False

	i = 5
	while (i * i <= n):
		if (n % i == 0 or n % (i + 2) == 0):
			return False
		i = i + 6

	return True



def solve ():
	t = 1
	for tt in range (t):
		n,k=num()
		d=ma.sqrt(9+8*(n+k))
		gp=(-3+d)/2
		print(int(n-gp))





if __name__ == "__main__":
	solve ()