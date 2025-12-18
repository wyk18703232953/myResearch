import math
n,m,k=map(int,input().split())
horz=[]
vert=[]
if k & 1:
    for i in range(n):
        temp=[-1 for j in range(m)]
        print(*temp)

else:
    for i in range(n):
        temp=list(map(int,input().split()))
        horz.append(temp)
    for i in range(n-1):
        temp=list(map(int,input().split()))
        vert.append(temp)
    dp=[[[0 for i in range(22)] for j in range(m)]for k in range(n)]
    for x in range(2,k+1,2):
        for i in range(n):
            for j in range(m):
                dp[i][j][x]=math.inf
                if i>0:
                     dp[i][j][x]=min(dp[i][j][x],dp[i-1][j][x-2]+2*vert[i-1][j])
                if i<n-1:
                      dp[i][j][x]=min(dp[i][j][x],dp[i+1][j][x-2]+2*vert[i][j])
                if j>0:
                     dp[i][j][x]=min(dp[i][j][x],dp[i][j-1][x-2]+2*horz[i][j-1])
                if j<m-1:
                     dp[i][j][x]=min(dp[i][j][x],dp[i][j+1][x-2]+2*horz[i][j])
    for i in range(n):
        temp=[]
        for j in range(m):
            temp.append(dp[i][j][k])
        print(*temp)