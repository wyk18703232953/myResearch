a,b,c=list(map(int,input().split()))
R=list(map(int,input().split()))
G=list(map(int,input().split()))
B=list(map(int,input().split()))
dp=[[[0 for i in range(201)] for j in range(201)] for k in range(201)]
# print(dp)
R.sort()
G.sort()
B.sort()
for i in range(len(R)+1):
    for j in range(len(G)+1):
        for k in range(len(B)+1):
            if(i and j):
                dp[i][j][k]=max(dp[i][j][k],dp[i-1][j-1][k]+R[i-1]*G[j-1])
            if(j and k):
                dp[i][j][k]=max(dp[i][j][k],dp[i][j-1][k-1]+G[j-1]*B[k-1])
            if(i and k):
                dp[i][j][k]=max(dp[i][j][k],dp[i-1][j][k-1]+R[i-1]*B[k-1])
print(dp[len(R)][len(G)][len(B)])      