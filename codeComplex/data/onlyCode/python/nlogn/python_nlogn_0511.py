#########################################################################################################\
#########################################################################################################
###################################The_Apurv_Rathore#####################################################
#########################################################################################################
#########################################################################################################

import sys,os,io
from math import log, gcd, ceil
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
from sys import stdin

import math 



def ncr(n, r, p):  #using fermat's little theorem
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den,
                      p - 2, p)) % p

  
def primeFactors(n): 
    l = []
    while n % 2 == 0: 
        l.append(2)
        n = n / 2
          
    for i in range(3,int(math.sqrt(n))+1,2): 
          

        while n % i== 0: 
            l.append(int(i))
            n = n / i 
    if n > 2: 
        l.append(n)
    return list(set(l))
    
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

def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")


input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

t = int(input())
for _ in range(t):
    n = ii()
    l = li()
    l1 = l[:]
    arr = defaultdict(lambda:0)
    for i in l:
        arr[i]+=1
    l = []
    graterthan4 = 0
    isgraterthan4 = False
    for i in list(arr.keys()):
        if (arr[i]>=4):
            isgraterthan4 = True
            graterthan4 = i
        if (arr[i]>=2):
            l.append(i)
    n = len(l)
    l.sort()
    m = 1000000000000
    mi = []
    # print(l)
    for i in range(n-1):
        a = l[i]
        b = l[i+1]
        # print(a/b+b/a)
        if (a/b+b/a<m):
            m = a/b+b/a
            # print("m",m)
            mi = [a,b]
    if (isgraterthan4==True):
        print(graterthan4,graterthan4,graterthan4,graterthan4)
    else:
        a,b = mi
        print(a,a,b,b)
    

    