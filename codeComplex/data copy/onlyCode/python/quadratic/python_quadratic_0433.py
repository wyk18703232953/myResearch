
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

def solve(x , arr ):

    n = len(arr)
    flag = True
    k = []
    i = 0
    while flag:
        sm = 0
        while n > 0 and sm < x :
            sm += int(arr[i])
            i +=1
            n -=1
            if n <= 0 :
                flag = False
                break
        if sm>0:
            k.append(sm)

    return k

n = INT()
s = STR()

if len(set(s)) == 1 :
    print('YES');exit(0)

l = []
t = 0
for i in range(n-1):
    t += int(s[i])
    l.append(t)

#print(l)

v = []
for i in l :
    if i > 0 :
        r = solve(i , s)
        if len(r) > 1 and len(set(r)) == 1 :
            print('YES')
            break
else:
    print('NO')


