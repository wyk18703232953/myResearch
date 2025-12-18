n, m, k =map(int, input().split())
horizontal = [list(map(int, input().split())) for i in range(n)]
vertical = [list(map(int, input().split())) for i in range(n-1)]
if k%2 or max(n, m)==1:print(*[" ".join(['-1']*m) for i in range(n)], sep='\n');exit()
dp = [[[0]*(k//2+1) for i in range(m)] for j in range(n)]
for length in range(1, k//2+1):
    for i in range(n):
        for j in range(m):
            left_path = 10e7 if j==0 else horizontal[i][j-1]+dp[i][j-1][length-1]
            right_path = 10e7 if j==m-1 else horizontal[i][j]+dp[i][j+1][length-1]
            top_path = 10e7 if i==0 else vertical[i-1][j]+dp[i-1][j][length-1]
            bottom_path = 10e7 if i==n-1 else vertical[i][j]+dp[i+1][j][length-1]
            dp[i][j][length] = min([left_path, right_path, top_path, bottom_path])
for i in range(n):print(*[dp[i][j][k//2]*2 for j in range(m)])
