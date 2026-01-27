from sys import stdin
a, b, c, n = map(int, stdin.readline().split())
if c > a or c > b:
    print(-1)
else:
    val = n - ((a - c) + (b - c)) - c
    print(val if val <= n and val > 0 else -1)