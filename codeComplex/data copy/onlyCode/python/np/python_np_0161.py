# from math import *
from itertools import combinations
from sys import stdin
input = stdin.readline
intin = lambda: map(int, input().split())

n, l, r, x = intin()
*a, = intin()
print(sum([sum([max(j) - min(j) >= x and l <= sum(j) <= r for j in combinations(a, i)]) for i in range(2, n + 1)]))