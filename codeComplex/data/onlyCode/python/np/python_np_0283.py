'''
    Auther: ghoshashis545 Ashis Ghosh
    College: jalpaiguri Govt Enggineering College

'''
from os import path
import sys
from heapq import heappush,heappop,heapify
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
mod=1000000007
# mod=998244353
inf = float("inf")
vow=['a','e','i','o','u']
dx,dy=[-1,1,0,0],[0,0,1,-1]

def bo(i):
    return ord(i)-ord('a')

file=1


def solve():

    # for t in range(ii()):

    n,q=mi()

    x=int(log(n+1,2))
    root=1<<(x-1)
    for i in range(q):
        u=ii()
        s=si()
        pos='U'
        if(u<root):
            pos='L'
        if(u>root):
            pos='R'

        s1=bin(u)[2:]
        s1='0'*(x-len(s1))+s1
        s1=list(s1)
        for j in s:
            for k in range(x-1,-1,-1):
                if s1[k]=='1':
                    f=k
                    break
            if j=='L':
                if(f==x-1):
                    continue
                s1[f]='0'
                s1[f+1]='1'
            elif(j=='R'):
                if(f==x-1):
                    continue
                s1[f+1]='1'
            else:
                if f==0:
                    continue
                if s1[f-1]=='1':
                    s1[f]='0'
                else:
                    s1[f-1]='1'
                    s1[f]='0'
            # print(s1)
        s1="".join(s1)
        print(int(s1,2))
    
    
    
    
    
    
    
    
        

        



    










        
if __name__ =="__main__":

    if(file):

        if path.exists('input.txt'):
            sys.stdin=open('input.txt', 'r')
            sys.stdout=open('output.txt','w')
        else:
            input=sys.stdin.readline
    solve()