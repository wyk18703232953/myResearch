n, m, k = map(int, input().split())
ea = [list(map(int, input().split()))for _ in range(n)]
eb = [list(map(int, input().split()))for _ in range(n-1)]
dp = [[[10**20]*m for __ in range(n)]for _ in range(k//2+1)]
dp[0] = [[0]*m for _ in range(n)]


def show_ans():
    for line in dp[-1]:
        print(' '.join(map(str, [d*2 for d in line])))


if k % 2:
    for i in range(n):
        print(' '.join(['-1']*m))
    exit()
for t in range(1, k//2+1):
    for i in range(n):
        for j in range(m):
            if i:
                dp[t][i][j] = min(dp[t][i][j], dp[t-1][i-1][j]+eb[i-1][j])
            if i < n-1:
                dp[t][i][j] = min(dp[t][i][j], dp[t-1][i+1][j]+eb[i][j])
            if j:
                dp[t][i][j] = min(dp[t][i][j], dp[t-1][i][j-1]+ea[i][j-1])
            if j < m-1:
                dp[t][i][j] = min(dp[t][i][j], dp[t-1][i][j+1]+ea[i][j])
show_ans()






