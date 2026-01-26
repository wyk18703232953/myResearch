def solve(rn,gn,bn,r,g,b):
    r = sorted(r,reverse=True)
    g = sorted(g, reverse=True)
    b = sorted(b, reverse=True)

    dp = [[[0 for k in range(bn+1)] for j in range(gn+1)] for i in range(rn+1)]


    ans = 0
    for i in range(rn+1):
        for j in range(gn+1):
            for k in range(bn+1):
                if i < rn and j < gn:
                    dp[i+1][j+1][k] = max(dp[i+1][j+1][k], dp[i][j][k] + r[i]*g[j])
                if i < rn and k < bn:
                    dp[i+1][j][k+1] = max(dp[i+1][j][k+1], dp[i][j][k] + r[i]*b[k])
                if j < gn and k <bn:
                    dp[i][j+1][k+1] = max(dp[i][j+1][k+1], dp[i][j][k] + g[j]*b[k])

                ans = max(ans,dp[i][j][k])

    print(ans)






if __name__ == '__main__':
    rn, gn, bn = map(int,input().split())

    r = list(map(int,input().split()))
    g = list(map(int, input().split()))
    b = list(map(int, input().split()))

    solve(rn,gn,bn,r,g,b)