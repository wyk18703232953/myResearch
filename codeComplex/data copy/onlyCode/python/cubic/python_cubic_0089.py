from collections import Counter

n, k = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
f = [int(x) for x in input().split()]
h = [0] + [int(x) for x in input().split()]

cnt_all = Counter(c)
cnt_fav = Counter(f)

ans = 0
for fi in cnt_fav:
    if fi not in cnt_all:
        continue
    m = cnt_fav[fi]
    t = min(cnt_all[fi], m * k)
    dp = [[0] * (t + 1) for _ in range(m + 1)]
    for x in range(1, m + 1):
        for s in range(0, t + 1):
            for ki in range(0, k + 1):
                if ki + s > t:
                    break
                dp[x][ki + s] = max(dp[x][ki + s], dp[x - 1][s] + h[ki])
    ans += dp[m][t]
print(ans)