# Author: S Mahesh Raju
# Username: maheshraju2020
# Date: 29/07/2020

from sys import stdin,stdout
from math import gcd, ceil, sqrt
from itertools import combinations
from collections import Counter
from bisect import bisect_left, bisect_right
ii1 = lambda: int(stdin.readline().strip())
is1 = lambda: stdin.readline().strip()
iia = lambda: list(map(int, stdin.readline().strip().split()))
isa = lambda: stdin.readline().strip().split()
mod = 1000000007

n, l, r, x = iia()
arr = iia()
count = 0
for i in range(2, n + 1):
    t = combinations(arr, i)
    for j in t:
        if sum(j) >= l and sum(j) <= r \
            and max(j) - min(j) >= x:
            count += 1
print(count)
    