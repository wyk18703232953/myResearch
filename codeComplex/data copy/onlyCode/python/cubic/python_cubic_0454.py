import sys
input=sys.stdin.readline

#t=int(input())
t=1
for i in range(t):
    #n=int(input())
    n,m,k = map(int,input().split())
    b=[]
    horizontal_edges=[]
    vertical_edges=[]
    for i in range(n):
        temp=[int(x) for x in input().split()]
        horizontal_edges.append(temp)
    for i in range(n-1):
        temp=[int(x) for x in input().split()]
        vertical_edges.append(temp)

    if k%2==1:
        for i in range(n):
            for j in range(m):
                print(-1,end=' ')
            print()
        continue

    dp=[[[10**9 for x in range(k+1)] for x in range(m)] for x in range(n)]

    for i in range(n):
        for j in range(m):
            dp[i][j][0]=0

    for z in range(2,k+1,2):
        for i in range(n):
            for j in range(m):
                    if i>0:
                        if i<n-1:
                            dp[i][j][z]=min(dp[i-1][j][z-2]+2*vertical_edges[i-1][j],dp[i+1][j][z-2]+2*vertical_edges[i][j])
                        else:
                            dp[i][j][z]=dp[i-1][j][z-2]+2*vertical_edges[i-1][j]
                    else:
                        dp[i][j][z]=dp[i+1][j][z-2]+2*vertical_edges[i][j]
                    if j>0:
                        if j<m-1:
                            dp[i][j][z]=min(dp[i][j][z],dp[i][j-1][z-2]+2*horizontal_edges[i][j-1],dp[i][j+1][z-2]+2*horizontal_edges[i][j])
                        else:
                            dp[i][j][z]=min(dp[i][j][z],dp[i][j-1][z-2]+2*horizontal_edges[i][j-1])
                    else:
                        dp[i][j][z]=min(dp[i][j][z],dp[i][j+1][z-2]+2*horizontal_edges[i][j])

    for i in range(n):
            for j in range(m):
                print(dp[i][j][k],end=' ')
            print()