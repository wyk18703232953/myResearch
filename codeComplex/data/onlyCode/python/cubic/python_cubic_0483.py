from sys import stdin
readline = stdin.readline
def readInt():
    return int(readline())
def readInts():
    return list(map(int,readline().split()))

U, D, L, R = 0, 1, 2, 3
DIR = [(-1,0), (1,0), (0,-1), (0,1)]

n, m, k = readInts()

moves = [[[-1 for _ in range(4)] for _ in range(m)] for _ in range(n)]

right = []
down = []

for i in range(n):
    row = readInts()
    right.append(row)
    # for j in range(m-1):
    #     e = row[j]
    #     moves[i][j][R] = e
    #     moves[i][j+1][L] = e

for i in range(n-1):
    row = readInts()
    down.append(row)
    # for j in range(m):
    #     e = row[j]
    #     moves[i][j][D] = e
    #     moves[i+1][j][U] = e

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
            # for d, (di, dj) in enumerate(DIR):
            #     if moves[i][j][d] != -1:
            #         dp[i][j][l+1] = min(dp[i][j][l+1], dp[i+di][j+dj][l] + moves[i][j][d])
for i in range(n):
    for j in range(m):
        print(2*dp[i][j][k], end=" ")
    print()
