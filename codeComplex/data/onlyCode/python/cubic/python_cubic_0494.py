from sys import stdin
input=stdin.readline
def answer():
    dp=[[[1e9 for i in range(k//2 + 1)] for j in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            dp[i][j][0]=0
    
    for x in range(1,k//2 + 1):

        for i in range(n):
            for j in range(m):

                if(i > 0):
                    dp[i][j][x]=min(dp[i][j][x],dp[i-1][j][x-1] + c[i-1][j])
                if(j > 0):
                    dp[i][j][x]=min(dp[i][j][x],dp[i][j-1][x-1] + r[i][j-1])
                if(i + 1 < n):
                    dp[i][j][x]=min(dp[i][j][x],dp[i+1][j][x-1] + c[i][j])
                if(j + 1 < m):
                    dp[i][j][x]=min(dp[i][j][x],dp[i][j+1][x-1] + r[i][j])

    for i in range(n):
        for j in range(m):
            print(2*dp[i][j][-1],end=' ')

        print()



n,m,k=map(int,input().split())

r=[list(map(int,input().split())) for i in range(n)]
c=[list(map(int,input().split())) for i in range(n-1)]

if(k & 1):
    for i in range(n):
        for j in range(m):
            print(-1,end=' ')
    
else:answer()
