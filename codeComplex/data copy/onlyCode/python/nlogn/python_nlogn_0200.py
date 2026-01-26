from collections import deque
import heapq
import sys


def input():
    return sys.stdin.readline().rstrip()


n, T = map(int, input().split())
problems = [tuple(map(int, input().split())) for i in range(n)]


def possible(K):
    d = []
    for a, t in problems:
        if a >= K:
            d.append(t)
    d.sort()
    if len(d) < K:
        return False
    else:
        return sum(d[:K]) <= T


l = 0
r = n + 1
while r - l > 1:
    med = (r + l)//2
    if possible(med):
        l = med
    else:
        r = med
print(l)
print(l)
d = []
for i, (a, t) in enumerate(problems):
    if a >= l:
        d.append((t, i+1))
d.sort(key=lambda x: x[0])
ans = [v[1] for v in d[:l]]
print(*ans)
