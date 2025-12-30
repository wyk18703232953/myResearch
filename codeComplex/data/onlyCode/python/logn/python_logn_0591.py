from sys import stdin, stdout
from math import floor, gcd, fabs, factorial, fmod, sqrt, inf, log
from collections import defaultdict as dd, deque
from heapq import merge, heapify, heappop, heappush, nsmallest
from bisect import bisect_left as bl, bisect_right as br, bisect
        
mod = pow(10, 9) + 7
mod2 = 998244353
        
def inp(): return stdin.readline().strip()
def mp(): return map(int, inp().split())
 
a, b = mp()
c = 0
x = 0
while not (c>=b and c-b+x==a):
    x += 1
    c += x
print(a-x)