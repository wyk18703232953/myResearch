import sys
sys.setrecursionlimit(50000)
for _ in range(1):
    n,m,k = map(int,input().split())
    s = [[[-1,-1,-1,-1] for _ in range(m)] for _ in range(n)]
    for i in range(n):
        d = [int(x) for x in input().split()]
        for j in range(m-1):
            s[i][j][1] = d[j]
            s[i][j+1][3] = d[j]
    for i in range(n-1):
        d = [int(x) for x in input().split()]
        for j in range(m):
            s[i][j][2] = d[j]
            s[i+1][j][0] = d[j]
    if k%2==1:
        for i in range(n):
            print(*[-1 for _ in range(m)])
        continue
    dp = [[[9999999 for _ in range(k//2+1)] for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            dp[i][j][0] = 0
    for q in range(1,k//2+1):
        for i in range(n):
            for j in range(m):
                cands = []
                if i > 0:
                    cands.append(dp[i-1][j][q-1] + s[i-1][j][2])
                if j > 0:
                    cands.append(dp[i][j-1][q-1] + s[i][j-1][1])
                if i < n - 1:
                    cands.append(dp[i+1][j][q-1] + s[i+1][j][0])
                if j < m - 1:
                    cands.append(dp[i][j+1][q-1] + s[i][j+1][3])
                dp[i][j][q] = min(cands)
    for i in range(n):
        for j in range(m):
            print(2*dp[i][j][k//2],end=' ')
        print()