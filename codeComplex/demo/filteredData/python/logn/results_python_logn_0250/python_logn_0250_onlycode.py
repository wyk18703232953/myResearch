from itertools import combinations_with_replacement 
import sys
from sys import stdin
import math
import bisect
#Find Set LSB = (x&(-x)), isPowerOfTwo = (x & (x-1))
# 1<<x =2^x
#x^=1<<pos  flip the bit at pos

def BinarySearch(a, x):
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1
def iinput():
    return int(input())
def minput():
    return map(int,input().split())
def linput():
    return list(map(int,input().split()))

def fiinput():
    return int(stdin.readline())
def fminput():
    return map(int,stdin.readline().strip().split())
def flinput():
    return list(map(int,stdin.readline().strip().split()))

x,k=minput()

if(x==0):
    print(0)
else:
    mod=(10**9)+7
    a=pow(2,k,mod)
    b=((2*x)%mod-1)%mod
    ans=((a*b)%mod+1)%mod
    print(ans)