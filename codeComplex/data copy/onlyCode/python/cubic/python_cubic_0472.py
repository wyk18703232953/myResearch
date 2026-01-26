from sys import stdin, stdout, maxsize
from math import inf

R = lambda : stdin.readline().strip()
RL = lambda f=None: list(map(f, R().split(' '))) if f else list(R().split(' '))

output = lambda x: stdout.write(str(x) + '\n')
output_list = lambda x: output(' '.join(map(str, x)))


n, m, K = RL(int)

if K%2:
    for i in range(n):
        print( *(m*[-1]) )
    exit()

hor = [ RL(int) +[inf] for i in range(n) ]
vert = [ RL(int) for i in range(n-1) ] + [ m*[inf] ]

K = K//2
dp = [ [m*[inf] for i in range(n)] for j in range(0, K+1)]

dp[0] = [m*[0] for i in range(n)]

def valid(i, j):
    if -1 < i < n and  -1 < j < m:
        return True
    return False

for k in range(1, K+1):
    for i in range(n):
        for j in range(m):
            if valid(i, j+1):
                dp[k][i][j] = min(dp[k][i][j], dp[k-1][i][j+1] + 2*hor[i][j])
            if valid(i+1, j):
                dp[k][i][j] = min(dp[k][i][j], dp[k-1][i+1][j] + 2*vert[i][j])
            if valid(i-1, j):
                dp[k][i][j] = min(dp[k][i][j], dp[k-1][i-1][j] + 2*vert[i-1][j])
            if valid(i, j-1):
                dp[k][i][j] = min(dp[k][i][j], dp[k-1][i][j-1] + 2*hor[i][j-1])

for i in dp[-1]:
    print(*i)
