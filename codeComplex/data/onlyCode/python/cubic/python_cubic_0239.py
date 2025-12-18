def solve(i, j, k):
    if (i < 0 and j < 0) or (j < 0 and k < 0) or (i < 0 and k < 0):
        return 0
    if dp[i][j][k] != -1:
        return dp[i][j][k]
    ans = 0
    if i >= 0 and j >= 0:
        ans = max(ans, rs[i] * gs[j] + solve(i - 1, j - 1, k))
    if i >= 0 and k >= 0:
        ans = max(ans, rs[i] * bs[k] + solve(i - 1, j, k - 1))
    if j >= 0 and k >= 0:
        ans = max(ans, bs[k] * gs[j] + solve(i, j - 1, k - 1))
    dp[i][j][k] = ans
    return ans

a, b, c = map(int, input().split())
rs = sorted(list(map(int, input().split())))
gs = sorted(list(map(int, input().split())))
bs = sorted(list(map(int, input().split())))
dp = [[[-1 for x in range(c + 1)] for y in range(b + 1)] for z in range(a + 1)]
print(solve(a - 1, b - 1, c - 1))
