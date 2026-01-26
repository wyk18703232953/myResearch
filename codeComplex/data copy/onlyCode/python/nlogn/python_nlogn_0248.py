
def STR(): return list(input())
def INT(): return int(input())
def MAP(): return map(int, input().split())
def MAP2():return map(float,input().split())
def LIST(): return list(map(int, input().split()))
def STRING(): return input()
from heapq import heappop , heappush
from bisect import *
from collections import deque , Counter
from math import *
from itertools import permutations , accumulate
dx = [-1 , 1 , 0 , 0  ]
dy = [0 , 0  , 1  , - 1]
#visited = [[False for i in range(m)] for j in range(n)]
#for tt in range(INT()):


def Binary_Search(arr , n , x):
    l , r = 0 , n-1
    while l <= r :
        mid = l + (r - l )//2
        if arr[mid] == x :
            return mid+1
        elif arr[mid] > x :
            r = mid - 1
        else:
            l = mid + 1
    return r + 1


n , q = MAP()
a = LIST()
b = LIST()
ps = list(accumulate(a))
res = []
sm = 0
for i in range(q):
    sm += b[i]
    if sm >= ps[-1]:
        res.append(n)
        sm = 0
    else:
        z = (Binary_Search(ps , n , sm))
        res.append(n - z)
for i in res:
    print(i)


