import sys
input = sys.stdin.readline
def main():
    n,m,k = map(int,input().split())
    if k%2==1:
        for i in range(n):
            for j in  range(m):
                print(-1,end=" ")
            print()
        return 0
    kk=k
    maps= [[[0 for i in range(4)] for j in range(m)] for ii in range(n)]
    #0表示横向右，1表示横向左，2表示纵向下,3表示纵向上，
    dp=[[[1e9 for i in range(k//2+1)] for j in range(m)] for ii in range(n)]
    for i in range(n):
            for j in range(m):
                dp[i][j][0]=0
    for i in range(n):
        s=list(map(int,input().split()))
        for j in range(m-1):
            maps[i][j][0]=s[j]
            maps[i][j+1][1]=s[j]
    for i in range(n-1):
        s=list(map(int,input().split()))
        for j in range(m):
            maps[i][j][2]=s[j]
            maps[i+1][j][3]=s[j]
    for k in range(1,kk//2+1):
        for i in range(n):
            for j in range(m):
                if j<m-1:
                    dp[i][j+1][k]=min(dp[i][j+1][k],dp[i][j][k-1]+maps[i][j][0])
                if i<n-1:
                    dp[i+1][j][k]=min(dp[i+1][j][k],dp[i][j][k-1]+maps[i][j][2])
                if i>0:
                    dp[i-1][j][k]=min(dp[i-1][j][k],dp[i][j][k-1]+maps[i][j][3])
                if j>0:
                    dp[i][j-1][k]=min(dp[i][j-1][k],dp[i][j][k-1]+maps[i][j][1])
    for i in range(n):
        for j in range(m):
            print(dp[i][j][k]*2,end=" ")
        print()
main()

