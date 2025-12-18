import math
def mint(): return map(int, input().split())
n, m, k = mint()
horizontal = [list(mint()) for i in range(n)]
vertical = [list(mint()) for i in range(n-1)]
if k%2 or max(n, m)==1:
    for i in range(n):
        print(*[-1]*m)
    exit()
dp = [[[0]*(k//2+1) for i in range(m)] for j in range(n)]
for length in range(1, k//2+1):
    for i in range(n):
        for j in range(m):
            left_path = math.inf if j==0 else horizontal[i][j-1]+dp[i][j-1][length-1]
            right_path = math.inf if j==m-1 else horizontal[i][j]+dp[i][j+1][length-1]
            top_path = math.inf if i==0 else vertical[i-1][j]+dp[i-1][j][length-1]
            bottom_path = math.inf if i==n-1 else vertical[i][j]+dp[i+1][j][length-1]
            dp[i][j][length] = min([left_path, right_path, top_path, bottom_path])
for i in range(n):
    print(*[dp[i][j][k//2]*2 for j in range(m)])
