# cook your dish here
n,m,k = map(int,input().split())
wh=[]
#for left to right connections
for j in range(n):
    l=list(map(int,input().split()))
    wh.append(l)
    
wv=[]
#for top to bottom connections
for j in range(n-1):
    l=list(map(int,input().split()))
    wv.append(l)
    
if(k%2!=0):
    ans = [[-1 for _ in range(m)]for j in range(n)]
    for res in ans:
        print(*res)
else:
    dp = [[[0 for i in range(25)]for j in range(505)]for q in range(505)]
    for x in range(1,21):
        for i in range(1,n+1):
            for j in range(1,m+1):
                dp[i][j][x]=1234567890
                if(i!=n):
                    dp[i][j][x]=min(dp[i][j][x],dp[i+1][j][x-1]+wv[i-1][j-1])
                if(i!=1):
                    dp[i][j][x]=min(dp[i][j][x],dp[i-1][j][x-1]+wv[i-2][j-1])
                if(j!=m):
                    dp[i][j][x]=min(dp[i][j][x],dp[i][j+1][x-1]+wh[i-1][j-1])
                if(j!=1):
                    dp[i][j][x]=min(dp[i][j][x],dp[i][j-1][x-1]+wh[i-1][j-2])
    for i in range(1,n+1):
        for j in range(1,m+1):
            ans = 1234567890
            for x in range(1,k+1):
                if(k%x==0 and (k//x)%2==0 ):
                    ans = min(ans,dp[i][j][x]*(k//x))
            print(ans,end=" ")
        print()