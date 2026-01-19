import sys
def read():
    return int(input())
def reads():
    return [int(x) for x in input().split()]
N,M=reads()
table=[reads() for i in range(N)]
A=[[0]*N for i in range(N)]
B=[[0]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        res=10**9+7
        for k in range(M):
            res=min(res,abs(table[i][k]-table[j][k]))
        A[i][j]=res
        A[j][i]=res
        res=10**9+7
        for k in range(M-1):
            res=min(res,abs(table[i][k]-table[j][k+1]))
        B[i][j]=res
#print(table)
#print(A)
#print(B)
#A=[[10**9,2,3],[2,10**9,8],[1,5,10**9]]
#B=[[10**9,2,3],[2,10**9,8],[1,5,10**9]]
dp=[[-1]*N for i in range((1<<N) )]
def calc(mask,v):
    if dp[mask][v]!=-1:
        return dp[mask][v]
    res =0
    for u in range(N):
        if (mask & 1<<u) and u!=v:
            res =max(res,min(calc(mask^(1<<v),u),A[u][v]))
    dp[mask][v]=res
    return dp[mask][v]
ans=0
for i in range(N):
    dp = [[-1] * N for i in range((1 << N))]
    for k in range(N):
        if k==i:
            dp[1<<k][k]=10**9+7
        else:
            dp[1<<k][k]=0
    for j in range(N):
        ans=max(ans,min(B[j][i],calc((1<<N)-1,j)))
    #print(dp,ans)
print(ans)