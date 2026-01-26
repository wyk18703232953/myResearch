
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
#  primes = [2,11,101,1009,10007,100003,1000003,10000019,102345689]
#sys.stdin = open(r'input.txt' , 'r')
#sys.stdout = open(r'output.txt' , 'w')
#for tt in range(INT()):
#arr.sort(key=lambda x: (-d[x], x)) Sort with Freq

#Code

n = INT()
arr = LIST()
mx = max(arr)
x = -1
if mx == 1 :
    x = 2
else:
    x = 1

arr.remove(mx)
arr.append(x)
arr.sort()
print(*arr)


