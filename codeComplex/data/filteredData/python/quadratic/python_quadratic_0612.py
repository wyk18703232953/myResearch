import math
import queue

MOD = 998244353

def main(n):
    if n <= 0:
        # print(0)
        pass
        return

    m = max(1, n // 2)
    k = n

    a = [i % 10 - 5 for i in range(n)]

    dp = [[-10**20 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(min(m, i + 1)):
            if j == 0:
                if i == 0:
                    dp[i][j] = a[i] - k

                else:
                    dp[i][j] = max(dp[i - 1][m - 1] + a[i], a[i]) - k

            else:
                dp[i][j] = dp[i - 1][j - 1] + a[i]

    ans = 0
    for i in range(n):
        ans = max(ans, max(dp[i]))
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)