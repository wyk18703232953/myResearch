n = int(input())
p = [(-(10**6), 0)] + sorted([tuple(map(int, input().split())) for i in range(n)])
dp = [0] * (n + 1)
for i in range(1, n + 1):
    l, r = 0, i
    while r - l > 1:
        mid = (l + r) >> 1
        if p[i][0] - p[i][1] <= p[mid][0]: r = mid
        else: l = mid
    dp[i] = i - r + dp[r - 1]
ans = min(dp[i] + (n - i) for i in range(1, n + 1))
print(ans)