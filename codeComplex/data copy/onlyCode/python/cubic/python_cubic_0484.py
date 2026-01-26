from sys import stdin
readline = stdin.readline
def readInt():
    return int(readline())
def readInts():
    return list(map(int,readline().split()))

n, m, k = readInts()

right = []
down = []

for i in range(n):
    row = readInts()
    right.append(row)

for i in range(n-1):
    row = readInts()
    down.append(row)

if k % 2 == 1:
    for _ in range(n):
        for _ in range(m):
            print(-1, end=" ")
        print()
    exit()

k //= 2

dp = [[[0 for _ in range(k+1)] for _ in range(m)] for _ in range(n)]

for l in range(k):
    for i in range(n):
        for j in range(m):
            dp[i][j][l+1] = float("inf")
            if i > 0:
                dp[i][j][l+1] = min(dp[i][j][l+1], dp[i-1][j][l] + down[i-1][j])
            if j > 0:
                dp[i][j][l+1] = min(dp[i][j][l+1], dp[i][j-1][l] + right[i][j-1])
            if i < n - 1:
                dp[i][j][l+1] = min(dp[i][j][l+1], dp[i+1][j][l] + down[i][j])
            if j < m - 1:
                dp[i][j][l+1] = min(dp[i][j][l+1], dp[i][j+1][l] + right[i][j])

for i in range(n):
    for j in range(m):
        print(2*dp[i][j][k], end=" ")
    print()
