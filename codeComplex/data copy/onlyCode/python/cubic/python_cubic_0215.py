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
            if i<n[0] and j<n[1]:
                dp[i+1][j+1][k] = max(dp[i+1][j+1][k], dp[i][j][k] + u[0][i]*u[1][j])
            if j<n[1] and k<n[2]:
                dp[i][j+1][k+1] = max(dp[i][j+1][k+1], dp[i][j][k] + u[1][j]*u[2][k])
            if i<n[0] and k<n[2]:
                dp[i+1][j][k+1] = max(dp[i+1][j][k+1], dp[i][j][k] + u[0][i]*u[2][k])
res = max(x for u1 in dp for u2 in u1 for x in u2)
print(res)