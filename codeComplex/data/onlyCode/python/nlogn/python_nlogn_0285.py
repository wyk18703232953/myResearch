
def STR(): return list(input())
def INT(): return int(input())
def MAP(): return map(int, input().split())
def MAP2():return map(float,input().split())
def LIST(): return list(map(int, input().split()))
def STRING(): return input()
import string
import sys
from heapq import heappop , heappush
from bisect import *
from collections import deque , Counter , defaultdict
from math import *
from itertools import permutations , accumulate
dx = [-1 , 1 , 0 , 0  ]
dy = [0 , 0  , 1  , - 1]
#visited = [[False for i in range(m)] for j in range(n)]
#sys.stdin = open(r'input.txt' , 'r')
#sys.stdout = open(r'output.txt' , 'w')
#for tt in range(INT()):


#CODE

n = INT()
d = {}
sm = 0

for i in range(n):
    indx , y = MAP()
    d[indx] = [1 , [y]]

#print(d)

m = INT()
for i in range(m):
    indx , y = MAP()
    if indx in d :
        d[indx][0] += 1
        d[indx][1].append(y)
    else:
        d[indx] = [1 , [y]]


for i in d :
    if d[i][0] == 1 :
        sm += d[i][1][0]
    else:
        sm += max(d[i][1])

print(sm)

