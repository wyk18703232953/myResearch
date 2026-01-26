'''
    Auther: ghoshashis545 Ashis Ghosh
    College: jalpaiguri Govt Enggineering College

'''
from os import path
import sys
from heapq import heappush,heappop
from functools import cmp_to_key as ctk
from collections import deque,defaultdict as dd
from bisect import bisect,bisect_left,bisect_right,insort,insort_left,insort_right
from itertools import permutations
from datetime import datetime
from math import ceil,sqrt,log,gcd
def ii():return int(input())
def si():return input().rstrip()
def mi():return map(int,input().split())
def li():return list(mi())
abc='abcdefghijklmnopqrstuvwxyz'
# mod=1000000007
mod=998244353
inf = float("inf")
vow=['a','e','i','o','u']
dx,dy=[-1,1,0,0],[0,0,1,-1]

def bo(i):
    return ord(i)-ord('a')


    
def sod(n):
    s = 0 
    while n:
        s += (n%10)
        n //= 10
    return s

    
def solve():



    n,s = mi()

    def fun(mid):
        return mid - sod(mid) >= s
    
    l = 0
    r = n
    ans = -1
    while l <= r:
        m = l+(r-l)//2
        if fun(m):
            ans = m
            r = m-1
        else:
            l = m+1
    if ans == -1:
        ans = n+1
    print(n-ans+1)







    








        
if __name__ =="__main__":

    
    if path.exists('input.txt'):
        sys.stdin=open('input.txt', 'r')
        sys.stdout=open('output.txt','w')
    else:
        input=sys.stdin.readline
    solve()