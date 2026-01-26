import sys,os,io
from sys import stdin
from math import log, gcd, ceil
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
from bisect import bisect_left , bisect_right
import math 
def ii():
    return int(input())
def li():
    return list(map(int,input().split()))
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def solve():
    n = ii()
    d = defaultdict(lambda:0)
    d1 = defaultdict(lambda:0)
    for i in range(n):
        x,y = li()
        d[x-1]-=1
        d[y]+=1
    
    x = list(d.keys())
    x.sort()
    r = x[-1]
    # print(x)
    # print(d)
    c=d[r]
    temp=1
    for i in range(len(x)-2,-1,-1):
        l = x[i]+1
        d1[c]+=r-l+temp
        # print(c,r-l+1)
        c+=d[x[i]]
        r=l
        temp=0
        
    for i in range(1,n+1):
        print(d1[i],end=" ")
    print()

        


t = 1
# t = int(input())
for _ in range(t):
    solve()
    
