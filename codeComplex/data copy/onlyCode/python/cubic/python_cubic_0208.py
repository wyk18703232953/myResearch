R, G, B = map(int, input().split())
r = list(map(int, input().split()))
g = list(map(int, input().split()))
b = list(map(int, input().split()))

r.sort(reverse=True)
g.sort(reverse=True)
b.sort(reverse=True)

dp = [[[0 for ___ in range(B+1)] for __ in range(G+1)] for _ in range(R+1)]
mx = 0

for i in range(R+1):
    for j in range(G+1):
        for k in range(B+1):
            if i < R and j < G:
                dp[i+1][j+1][k] = max(dp[i+1][j+1][k], dp[i][j][k] + r[i] * g[j])
            if i < R and k < B:
                dp[i+1][j][k+1] = max(dp[i+1][j][k+1], dp[i][j][k] + r[i] * b[k])
            if j < G and k < B:
                dp[i][j+1][k+1] = max(dp[i][j+1][k+1], dp[i][j][k] + g[j] * b[k])
            mx = max(mx, dp[i][j][k])

print(mx)