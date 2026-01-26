
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
from collections import deque , Counter
from math import *
from itertools import permutations , accumulate
dx = [-1 , 1 , 0 , 0  ]
dy = [0 , 0  , 1  , - 1]
#visited = [[False for i in range(m)] for j in range(n)]
#sys.stdin = open(r'input.txt' , 'r')
#sys.stdout = open(r'output.txt' , 'w')
#for tt in range(INT()):

s = STR()

if len(set(s)) == len(s):
    print('0')
    exit(0)

d = []

for i in range(len(s)):
    for j in range(i+1 , len(s)):
        x = ''
        for k in range(i , j+1):
            x += s[k]

        d.append(x)

v = {}
for i in range(len(s)):
    if s[i] not in v :
        v[s[i]] = 1
    else:
        v[s[i]] +=1


for i in d :
    if i not in v :
        v[i] = 1
    else:
        v[i]+=1

#print(v)
mx = -1
ans = ''

for i in v :
    if v[i] >= 2 :
        if len(i) > mx :
            mx = max(mx , len(i))

print(mx)

