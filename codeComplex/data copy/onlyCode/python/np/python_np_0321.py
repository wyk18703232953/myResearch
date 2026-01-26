import sys
import math
from collections import defaultdict,deque
import heapq
n,k=map(int,sys.stdin.readline().split())

mod=998244353
dp=[[0,0,0,0] for x in range(k+3)]
dp[1][0]=1
dp[1][1]=1
dp[2][2]=1
dp[2][3]=1
newdp=[[0,0,0,0] for x in range(k+3)]
for i in range(n-1):
    
    for j in range(k+1):
        newdp[j+1][1]+=dp[j][0]
        newdp[j+1][3]+=dp[j][0]
        newdp[j+1][2]+=dp[j][0]
        newdp[j][0]+=dp[j][0]
        newdp[j][1]+=dp[j][1]
        newdp[j+1][3]+=dp[j][1]
        newdp[j+1][2]+=dp[j][1]
        newdp[j+1][0]+=dp[j][1]
        newdp[j][1]+=dp[j][2]
        newdp[j+2][3]+=dp[j][2]
        newdp[j][2]+=dp[j][2]
        newdp[j][0]+=dp[j][2]
        newdp[j][1]+=dp[j][3]
        newdp[j][3]+=dp[j][3]
        newdp[j+2][2]+=dp[j][3]
        newdp[j][0]+=dp[j][3]
        '''dp[i+1][j][0]+=dp[i][j][0]
        dp[i+1][j][1]+=dp[i][j][1]
        dp[i+1][j][2]+=dp[i][j][2]
        dp[i+1][j][3]+=dp[i][j][3]
        dp[i+1][j+1][0]+=dp[i][j][2]+dp[i][j][3]
        dp[i+1][j+1][1]+=dp[i][j][2]+dp[i][j][3]
        dp[i+1][j+1][2]+=dp[i][j][0]+dp[i][j][1]
        dp[i+1][j+1][3]+=dp[i][j][0]+dp[i][j][1]
        dp[i+1][j+2][2]+=dp[i][j][3]
        dp[i+1][j+2][3]+=dp[i][j][2]'''
        for a in range(3):
            for b in range(4):
                newdp[a+j][b]%=mod
    for a in range(k+3):
        for b in range(4):
            dp[a][b]=newdp[a][b]
            newdp[a][b]=0
#print(dp,'dp')
'''for i in range(n):
    print(dp[i])'''
#ans=0
#print(dp,'dp')
ans=sum(dp[k])
ans%=mod
print(ans)
                
            
            
                              
