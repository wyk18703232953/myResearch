import sys,os,io
from math import log, gcd
from collections import defaultdict, deque
from heapq import heappush, heappop


# Iterative Python3 program 
# to compute modular power 

# Iterative Function to calculate 
# (x^y)%p in O(log y) 
def power(x, y, p) : 
	res = 1
	x = x % p 
	if (x == 0) : 
		return 0
	while (y > 0) : 
		if ((y & 1) == 1) : 
			res = (res * x) % p 
		y = y >> 1	 # y = y/2 
		x = (x * x) % p 		
	return res 


def si():
    return input()

# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def prefix_sum(arr):
    r = [0] * (len(arr)+1)
    for i, el in enumerate(arr):
        r[i+1] = r[i] + el
    return r

def divideCeil(n,x):
    if (n%x==0):
        return n//x
    return n//x+1

def ii():
    return int(input())

def li():
    return list(map(int,input().split()))



# t = int(input())
t = 1
for _ in range(t):
    n = ii()
    l = li()
    l1 = l[:]
    l1.sort()
    pos = []
    for i in range(n):
        if (l1[i]!=l[i]):
            pos.append(i)
    if (len(pos)==0) or (len(pos)==2 and l[pos[0]]==l1[pos[1]] and l[pos[1]]==l1[pos[0]]):
        print("YES")
    else:
        print("NO")



 