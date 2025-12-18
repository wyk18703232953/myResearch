import sys
input = sys.stdin.readline

MAXN = 202

def main():
    R, G, B = list(map(int, input().split()))
    r = list(map(int, input().split()))
    g = list(map(int, input().split()))
    b = list(map(int, input().split()))
    r.sort()
    g.sort()
    b.sort()
    dp = [[[0]*MAXN for _ in range(MAXN)] for _ in range(MAXN)]
    for i in range(1, R+1):
        for j in range(1, G+1):
            dp[i][j][0] = r[i-1]*g[j-1]+dp[i-1][j-1][0]
    for i in range(1, R+1):
        for k in range(1, B+1):
            dp[i][0][k] = r[i-1]*b[k-1]+dp[i-1][0][k-1]
    for j in range(1, G+1):
        for k in range(1, B+1):
            dp[0][j][k] = g[j-1]*b[k-1]+dp[0][j-1][k-1]
    for i in range(1, R+1):
        for j in range(1, G+1):
            for k in range(1, B+1):
                dp[i][j][k] = max(r[i-1]*g[j-1]+dp[i-1][j-1][k], r[i-1]*b[k-1]+dp[i-1][j][k-1], g[j-1]*b[k-1]+dp[i][j-1][k-1])
    print(dp[R][G][B])

main()
