#dt = {} for i in x: dt[i] = dt.get(i,0)+1
import sys;input = sys.stdin.readline
inp,ip = lambda :int(input()),lambda :[int(w) for w in input().split()]

r,g,b = ip()
R = [0]+ip()
G = [0]+ip()
B = [0]+ip()
R.sort()
G.sort()
B.sort()
dp = [[[0]*201 for i in range(201)] for j in range(201)]
for i in range(r+1):
    for j in range(g+1):
        for k in range(b+1):
            x = dp[i-1][j-1][k] + R[i]*G[j] if i*j else 0
            y = dp[i][j-1][k-1] + G[j]*B[k] if j*k else 0
            z = dp[i-1][j][k-1] + R[i]*B[k] if i*k else 0
            dp[i][j][k] = max(dp[i][j][k],x,y,z)
print(dp[r][g][b])
#print(dp)
    
    
