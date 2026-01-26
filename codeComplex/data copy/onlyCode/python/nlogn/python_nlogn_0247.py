
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

def Binary_Search(arr , x , n):
    l ,r = 0 , n-1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x :
            return mid+1
        elif arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return r + 1


n , q = MAP()
a = LIST()
b = LIST()
ps = list(accumulate(a))
ans = []

arrows = 0
for arrow in b :
    arrows += arrow
    if arrows >= ps[-1]:
        ans.append(n)
        arrows = 0
    else:
        res = Binary_Search(ps , arrows , n)
        ans.append(n - res)

for i in ans:
    print(i)

