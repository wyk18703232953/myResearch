import sys
input = sys.stdin.readline

rr, gg, bb = map(int, input().split())
inf = 114514
r = list(map(int, input().split())) + [inf]
g = list(map(int, input().split())) + [inf]
b = list(map(int, input().split())) + [inf]
r.sort(reverse = True)
g.sort(reverse = True)
b.sort(reverse = True)
dp = []
for _ in range(rr + 1):
    dp.append([[0] * (bb + 1) for _ in range(gg + 1)])
ans = 0
for i in range(rr + 1):
    ri = r[i]
    for j in range(gg + 1):
        gj = g[j]
        for k in range(bb + 1):
            bk = b[k]
            if (i + j + k) % 2:
                continue
            dpijk = 0
            if i > 0 and j > 0:
                dpijk = max(dp[i - 1][j - 1][k] + ri * gj, dpijk)
            if j > 0 and k > 0:
                dpijk = max(dp[i][j - 1][k - 1] + gj * bk, dpijk)
            if k > 0 and i > 0:
                dpijk = max(dp[i - 1][j][k - 1] + bk * ri, dpijk)
            dp[i][j][k] = dpijk
            if ans < dpijk:
                ans = dpijk
print(ans)