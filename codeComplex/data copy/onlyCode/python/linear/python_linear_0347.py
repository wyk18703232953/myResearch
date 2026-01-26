import sys, heapq

n, m = map(int, sys.stdin.readline().split())
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
ans = [0] * n
for i in range(1, n, 2):
    ans[i] = 1
print(''.join(map(str, ans)))
