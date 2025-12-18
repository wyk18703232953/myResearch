import sys
from math import gcd, sqrt
from typing import Deque

sys.setrecursionlimit(10 ** 5)


inf = float("inf")
en = lambda x: list(enumerate(x))

ii = lambda: int(input())
r = lambda: map(int, input().split())
rr = lambda: list(r())


n = ii()
arr = rr()
arr = en(arr)

arr.sort(key=lambda x: x[1])

i = 0
brr = []

for j in input():
    if j == "0":
        brr.append(arr[i])
        print(arr[i][0] + 1, end=" ")
        i += 1
    else:
        x = brr.pop()
        print(x[0] + 1, end=" ")
