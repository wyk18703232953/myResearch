from collections import defaultdict
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n - 1)]
if k % 2:
    ans = [-1] * m
    for _ in range(n):
        print(*ans)
    exit()
#G = defaultdict(lambda : 0)
G = [[] for _ in range(n * m + 1)]
for i in range(n):
    a0 = a[i]
    for j in range(m - 1):
        x = a0[j]
        G[i * m + j].append((i * m + j + 1, x))
        G[i * m + j + 1].append((i * m + j, x))
        #G[(i * m + j, i * m + j + 1)] = x
        #G[(i * m + j + 1, i * m + j)] = x
for i in range(n - 1):
    b0 = b[i]
    for j in range(m):
        x = b0[j]
        G[i * m + j].append(((i + 1) * m + j, x))
        G[(i + 1) * m + j].append((i * m + j, x))
        #G[(i * m + j, (i + 1) * m + j)] = x
        #G[((i + 1) * m + j, i * m + j)] = x
dp = [[0] * m for _ in range(n)]
dp0 = [[0] * m for _ in range(n)]
dp, dp0 = [0] * (n * m), [0] * (n * m)
v = [(1, 0), (-1, 0), (0, 1), (0, -1)]
inf = 1145141919
for i in range(n):
    for j in range(m):
        s = i * m + j
        dps = inf
        for t, x in G[s]:
            dps = min(dps, 2 * x)
        dp[s] = dps
        dp0[s] = dps
for _ in range((k - 2) // 2):
    dp1 = [0] * (n * m)
    for i in range(n):
        for j in range(m):
            s = i * m + j
            dps = dp0[s] + 2 * dp[s]
            for t, x in G[s]:
                dps = min(dps, 2 * x + dp0[t])
            dp1[s] = dps
    dp0 = dp1
for i in range(n):
    ans = dp0[(m * i):(m * (i + 1))]
    print(*ans)