import sys, math, queue
MOD = 998244353
sys.setrecursionlimit(1000000)

def main(n):
    # Interpret n as sequence length; keep m and k derived deterministically
    if n <= 0:
        # print(0)
        pass
        return

    m = max(1, min(10, n))  # bounded window size for scalability
    k = n // 2 + 1          # deterministic penalty based on n

    # Deterministic generation of array a of length n
    # Example pattern: a[i] = (i % 7) - 3 to mix positive/negative values
    a = [(i % 7) - 3 for i in range(n)]

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

    ans = -10**20
    for i in range(n):
        row_max = dp[i][0]
        for j in range(1, m):
            if dp[i][j] > row_max:
                row_max = dp[i][j]
        if row_max > ans:
            ans = row_max
    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)