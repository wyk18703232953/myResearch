inf=10000000000
n,m,k=(int(i) for i in input().split())
h=[[int(i) for i in input().split()]for i in range(n)]
z=[[int(i) for i in input().split()]for i in range(n-1)]
dh=lambda x,y:h[x][y] if 0<=x<len(h) and 0<=y<len(h[0]) else inf
dz=lambda x,y:z[x][y] if 0<=x<len(z) and 0<=y<len(z[0]) else inf
dp=[[[0 for iii in range(m)] for ii in range(n)] for i in range(2)]
ddp=lambda x,y,z:dp[x][y][z] if 0<=y<n and 0<=z<m else inf
if k%2!=0:
    for i in dp[0]:
        for j in i:
            print(-1,end=' ')
        print()
else:
    for kk in range(int(k/2)):
        for i in range(n):
            for j in range(m):
                dp[1][i][j]=min(ddp(0,i-1,j)+dz(i-1,j),ddp(0,i+1,j)+dz(i,j),ddp(0,i,j-1)+dh(i,j-1),ddp(0,i,j+1)+dh(i,j))
        dp.reverse()
    for i in dp[0]:
        for j in i:
            print(2*j,end=' ')
        print()
