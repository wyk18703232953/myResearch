
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

#Code

n = INT()
arr = LIST()

i = 0
p = []
while 2**i <= 10**18:
    p.append(2**i)
    i = i+1

d = {}
s1= set()
for i in arr:
    s1.add(i)
    if i not in d :
        d[i] = 1
    else:
        d[i]+=1

s2 = set()
for i in s1 :
    flag = False
    for j in p :
        x = j - i
        k = -1
        try:
            k = d[x]
        except :
            k = -1
        if k != -1:
            if x == i and d[i] == 1 :
                continue
            else:
                flag = True
                break
    if flag == False:
        s2.add(i)

res = 0
for i in s2 :
    res+=d[i]
print(res)



