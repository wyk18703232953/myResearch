n, m, k = map(int, input().split())
*a, = map(int, input().split())
dp = [-1] * (n + 15)
for i in range(n):
    s, mx = a[i], max(0, a[i])
    for j in range(i - 1, max(-1, i - m), -1):
        s += a[j]
        mx = max(mx, s)
    dp[i] = max(0, dp[i - m] + s - k, mx - k)
print(max(dp))