from sys import stdin
import time

r,g,b = map(int,stdin.readline().split())

red = list(map(int,stdin.readline().split()))
green = list(map(int,stdin.readline().split()))
blue = list(map(int,stdin.readline().split()))
red.sort()
green.sort()
blue.sort()

dp = [[[0 for _ in range(b+1)] for _ in range(g+1)] for _ in range(r+1)]

for i in range(r+1):
    for j in range(g+1):
        for k in range(b+1):
            if i>0 and j>0:
                dp[i][j][k] = max(dp[i][j][k],dp[i-1][j-1][k]+red[i-1]*green[j-1])
            if i>0 and k>0:
                dp[i][j][k] = max(dp[i][j][k],dp[i-1][j][k-1]+red[i-1]*blue[k-1])
            if j>0 and k>0:
                dp[i][j][k] = max(dp[i][j][k],dp[i][j-1][k-1]+green[j-1]*blue[k-1])

print(dp[-1][-1][-1])                       
