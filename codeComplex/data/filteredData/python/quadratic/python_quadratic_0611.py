import sys, math, queue
MOD = 998244353
sys.setrecursionlimit(1000000)

def main(n):
    # Interpret n as both length of array and m; set k relative to n
    m = max(1, n)
    k = max(1, n // 2)
    # Deterministically generate array a of length n
    a = [(i * 3 + 1) % 1000 - 500 for i in range(n)]

    dp = [[-10**20 for _ in range(m)] for _ in range(n)]
    dp[0][0] = a[0] - k

    for i in range(1, n):
        for j in range(m):
            if j == 0:
                dp[i][j] = max(dp[i-1][m-1] + a[i], a[i]) - k

            else:
                dp[i][j] = dp[i-1][j-1] + a[i]

    ans = 0
    for i in range(n):
        ans = max(ans, max(dp[i]))
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)