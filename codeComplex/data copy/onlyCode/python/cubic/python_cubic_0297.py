R, G, B = list(map(int, input().split()))
r = sorted(list(map(int, input().split())), reverse=True)
g = sorted(list(map(int, input().split())), reverse=True)
b = sorted(list(map(int, input().split())), reverse=True)

ans = 0
dp = [[[0 for i in range(B+1)] for j in range(G+1)] for k in range(R+1)]
for i in range(R+1):
    for j in range(G+1):
        for k in range(B+1):
            if i<R and j<G:
                dp[i+1][j+1][k] = max(dp[i+1][j+1][k], dp[i][j][k] + r[i]*g[j])
            if j<G and k<B:
                dp[i][j+1][k+1] = max(dp[i][j+1][k+1], dp[i][j][k] + g[j]*b[k])
            if i<R and k<B:
                dp[i+1][j][k+1] = max(dp[i+1][j][k+1], dp[i][j][k] + r[i]*b[k])
            ans = max(ans, dp[i][j][k])
print(ans)
