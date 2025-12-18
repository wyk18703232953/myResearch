from os import path;import sys,time
mod = int(1e9 + 7)
from math import ceil, floor,gcd,log,log2 ,factorial,sqrt
from collections import defaultdict ,Counter , OrderedDict , deque;from itertools import combinations,permutations
from string import ascii_lowercase ,ascii_uppercase
from bisect import *;from functools import reduce;from operator import mul;maxx = float('inf')
I = lambda :int(sys.stdin.buffer.readline())
lint = lambda :[int(x) for x in sys.stdin.buffer.readline().split()]
S = lambda: sys.stdin.readline().strip('\n')
grid = lambda  r :[lint() for i in range(r)]
localsys = 0
start_time = time.time()
#left shift --- num*(2**k) --(k - shift)
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
def ceill(n,x):
    return (n+x -1 )//x
T =0

def solve():
	arr = list(map(int , S()))
	d ,s, ans  = {0} , 0 , 0
	for i in arr:
		s+=i
		s%=3
		if s in d :
			ans+=1
			s =0
			d = {0}
		d.add(s)
	print(ans)















	# n = I()
	# a = lint()
	# l , r ,ans = [1]*n , [1]*n , 1
	# for i in range(1 , n):
	# 	if a[i] > a[i-1]:
	# 		l[i] = l[i-1] + 1 #from left sort of prefix 
	# 	ans = max(ans , l[i]) 

	# for i in range(n-2 ,-1 ,-1 ):
	# 	if a[i+1] > a[i]:
	# 		r[i] =r[i+1] +1
	# 	ans = max(ans , r[i])

	# for i in range(1 , n - 1):
	# 	if a[i-1] < a[i+1]: #skipping one element
	# 		ans = max(ans , l[i-1] + r[i+1])
	# print(ans)

















def run():
    if (path.exists('input.txt')):
        sys.stdin=open('input.txt','r')
        sys.stdout=open('output.txt','w')


run()
T = I() if T else 1
for _ in range(T):
    solve()


if localsys:
    print("\n\nTime Elased :",time.time() - start_time,"seconds")


