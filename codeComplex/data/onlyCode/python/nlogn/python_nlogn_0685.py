from sys import exit

n, m = map(int, input().split())
b = list(map(int, input().split()))
g = list(map(int, input().split()))
if max(b) > min(g):
    print(-1)
    exit(0)
b.sort()
res = sum(g) + sum(b[:-1]) * m
if b[-1] in g:
    print(res)
else:
    print(res + b[-1] - b[-2])
