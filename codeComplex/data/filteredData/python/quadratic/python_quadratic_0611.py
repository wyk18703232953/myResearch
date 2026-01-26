import sys, math, queue
MOD = 998244353
sys.setrecursionlimit(1000000)

def main(n):
    # Interpret n as the length of array a
    # Set m and k as deterministic functions of n
    if n <= 0:
        return 0

    m = max(1, n // 3)
    k = max(1, n // 5)

    a = [((i * 7) % (3 * n + 1)) + 1 for i in range(n)]

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
    return ans

if __name__ == "__main__":
    main(10)