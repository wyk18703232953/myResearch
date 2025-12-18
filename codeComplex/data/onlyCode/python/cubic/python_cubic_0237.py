from sys import stdin, gettrace

if gettrace():
    inputi = input
else:
    def input():
        return next(stdin)[:-1]


    def inputi():
        return stdin.buffer.readline()


def main():
    r, g, b = map(int, inputi().split())
    rr = list(sorted(int(a) for a in inputi().split()))
    gg = list(sorted(int(a) for a in inputi().split()))
    bb = list(sorted(int(a) for a in inputi().split()))
    dp = [[[0]*(b+1) for _ in range(g+1)] for _ in range(r+1)]
    res = 0
    for i in range(r, -1, -1):
        for j in range(g, -1, -1):
            for k in range(b, -1, -1):
                if i > 0 and j > 0:
                    dp[i-1][j-1][k] = max(dp[i-1][j-1][k], dp[i][j][k] + rr[i-1]*gg[j-1])
                if i > 0 and k > 0:
                    dp[i-1][j][k-1] = max(dp[i-1][j][k-1], dp[i][j][k] + rr[i-1]*bb[k-1])
                if j > 0 and k > 0:
                    dp[i][j-1][k-1] = max(dp[i][j-1][k-1], dp[i][j][k] + gg[j-1]*bb[k-1])
                res = max(res, dp[i-1][j-1][k], dp[i-1][j][k-1] , dp[i][j-1][k-1])
    print(res)


if __name__ == "__main__":
    main()
