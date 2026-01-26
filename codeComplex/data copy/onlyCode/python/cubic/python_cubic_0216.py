# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

n = list(map(int, input().split()))
u = []
u.append(list(map(int, input().split())))
u.append(list(map(int, input().split())))
u.append(list(map(int, input().split())))
u[0].sort(reverse=True)
u[1].sort(reverse=True)
u[2].sort(reverse=True)
res = 0
dp = [[[0]*(n[2]+1) for _ in range(n[1]+1)] for _ in range(n[0]+1)]
for i in range(n[0]+1):
    for j in range(n[1]+1):
        for k in range(n[2]+1):
            x0 = (dp[i-1][j-1][k] + u[0][i-1]*u[1][j-1]) if i and j else 0
            x1 = (dp[i][j-1][k-1] + u[1][j-1]*u[2][k-1]) if j and k else 0
            x2 = (dp[i-1][j][k-1] + u[0][i-1]*u[2][k-1]) if i and k else 0
            dp[i][j][k] = max(x0, x1, x2)
            res = max(res, dp[i][j][k])
print(res)