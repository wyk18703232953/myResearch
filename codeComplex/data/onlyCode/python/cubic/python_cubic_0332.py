from sys import stdin, stdout
import math,sys,heapq
from itertools import permutations, combinations
from collections import defaultdict,deque,OrderedDict
from os import path
import random
import bisect as bi
def yes():print('YES')
def no():print('NO')
if (path.exists('input.txt')): 
    #------------------Sublime--------------------------------------#
    sys.stdin=open('input.txt','r');sys.stdout=open('output.txt','w');
    def I():return (int(input()))
    def In():return(map(int,input().split()))
else:
    #------------------PYPY FAst I/o--------------------------------#
    def I():return (int(stdin.readline()))
    def In():return(map(int,stdin.readline().split()))
#sys.setrecursionlimit(1500)
def dict(a):
    d={} 
    for x in a:
        if d.get(x,-1)!=-1:
            d[x]+=1
        else:
            d[x]=1
    return d
def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bi.bisect_left(a, x)
    if i != len(a):
        return i
    else:            
        return -1

def cal(r,g,b,dp,R,G,B,nr,ng,nb):
    if dp[r][g][b]!=-1:
        return dp[r][g][b]
    best=0
    if r<nr and g<ng:
        best=max(best,cal(r+1,g+1,b,dp,R,G,B,nr,ng,nb)+R[r]*G[g])
    if r<nr and b<nb:
        best=max(best,cal(r+1,g,b+1,dp,R,G,B,nr,ng,nb)+R[r]*B[b])
    if g<ng and b<nb:
        best=max(best,cal(r,g+1,b+1,dp,R,G,B,nr,ng,nb)+B[b]*G[g])
    dp[r][g][b]=best
    return dp[r][g][b]
def main():
    try:
        nr,ng,nb=In()
        dp=[[[-1 for x in range(201)]for y in range(201)] for z in range(201)]
        R=list(In())
        G=list(In())
        B=list(In())
        R.sort(reverse=True)
        G.sort(reverse=True)
        B.sort(reverse=True)
        print(cal(0,0,0,dp,R,G,B,nr,ng,nb))
    except:
        pass
        
M = 998244353
P = 1000000007
 
if __name__ == '__main__':
    # for _ in range(I()):main()
    for _ in range(1):main()