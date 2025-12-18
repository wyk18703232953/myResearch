import sys
n,m,k = map(int,input().split())

if k%2:
    ans = [[-1]*m for _ in range(n)]
    for row in ans:
        print(*row)
    exit()
A = []
B = []
inf = float('inf')
for _ in range(n):
    A.append(list(map(int,input().split())))
for _ in range(n-1):
    B.append(list(map(int,input().split())))

# dp = [[[inf for _ in range(k//2+1)] for _ in range(m)] for _ in range(n)]

# new
dp = [[inf]*m for _ in range(n)]
ans = [[None]*m for _ in range(n)]

for l in range(k//2+1):
    new_dp = [[inf]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if l == 0:
                new_dp[i][j] = 0
                continue

            up = B[i-1][j]*2 + dp[i-1][j] if i-1>=0 else inf
            right = A[i][j]*2 + dp[i][j+1] if j+1<m else inf
            left = A[i][j-1]*2 + dp[i][j-1] if j-1>=0 else inf
            down = B[i][j]*2 + dp[i+1][j] if i+1<n else inf

            new_dp[i][j] = min(up,right,left,down)
            if l == k//2:
                ans[i][j] = new_dp[i][j]
    dp = new_dp
for row in ans:
    print(*row)
