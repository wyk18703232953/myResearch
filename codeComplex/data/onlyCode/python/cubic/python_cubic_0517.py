n, m, K=map(int, input().split())
edgesh=[[0 for i in range(m-1)] for k in range(n)]
#edgesh[i][j] is the weight of the edge between i, j and i, j+1
edgesv=[[0 for i in range(m)] for k in range(n-1)]
#edgesv[i][j] is the weight of the edge between i, j and i+1, j
for mm in range(n):
    edgesh[mm]=list(map(int, input().split(" ")))
for mm in range(n-1):
    edgesv[mm]=list(map(int, input().split(" ")))
dp=[[[10**10 for tro in range(K+1)] for i in range(m)] for mm in range(n)]
for k in range(0, K+1, 2):
 for i in range(n):
  for j in range(m):
    if(k==0):
      dp[i][j][k]=0
    elif(i==0 and j==0):
      dp[i][j][k]=min(2*edgesh[i][j]+dp[i][j+1][k-2], 2*edgesv[i][j]+dp[i+1][j][k-2])
    elif(i==0 and j==m-1):
      dp[i][j][k]=min(2*edgesh[i][j-1]+dp[i][j-1][k-2], 2*edgesv[i][j]+dp[i+1][j][k-2])
    elif(i==0):
      dp[i][j][k]=min(2*edgesh[i][j]+dp[i][j+1][k-2], 2*edgesv[i][j]+dp[i+1][j][k-2], 2*edgesh[i][j-1]+dp[i][j-1][k-2])
    elif(j==0 and i==n-1):
      dp[i][j][k]=min(2*edgesh[i][j]+dp[i][j+1][k-2], 2*edgesv[i-1][j]+dp[i-1][j][k-2])
    elif(j==0):
      dp[i][j][k]=min(2*edgesh[i][j]+dp[i][j+1][k-2], 2*edgesv[i-1][j]+dp[i-1][j][k-2], 2*edgesv[i][j]+dp[i+1][j][k-2])
    elif(i==n-1 and j==m-1):
      dp[i][j][k]=min(2*edgesh[i][j-1]+dp[i][j-1][k-2], 2*edgesv[i-1][j]+dp[i-1][j][k-2])
    elif(i==n-1):
      dp[i][j][k]=min(2*edgesh[i][j]+dp[i][j+1][k-2], 2*edgesv[i-1][j]+dp[i-1][j][k-2], 2*edgesh[i][j-1]+dp[i][j-1][k-2])
    elif(j==m-1):
      dp[i][j][k]=min(2*edgesh[i][j-1]+dp[i][j-1][k-2], 2*edgesv[i-1][j]+dp[i-1][j][k-2], 2*edgesv[i][j]+dp[i+1][j][k-2])
    else:
      dp[i][j][k]=min(2*edgesh[i][j]+dp[i][j+1][k-2], 2*edgesv[i-1][j]+dp[i-1][j][k-2], 2*edgesv[i][j]+dp[i+1][j][k-2], 2*edgesh[i][j-1]+dp[i][j-1][k-2])
for i in range(n):
  for j in range(m):
   if(dp[i][j][K]>=10**10):
    print(-1, end=" ")
   else:
    print(dp[i][j][K], end=" ")
  print()