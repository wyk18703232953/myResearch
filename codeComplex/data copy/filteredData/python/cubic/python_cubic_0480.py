import math

M = 998244353
P = 1000000007
Inf = float('inf')

def solve(n_rows, n_cols, k_steps):
    n, m, k = n_rows, n_cols, k_steps
    rt = [[0] * m for _ in range(n)]
    do = [[0] * m for _ in range(n - 1)]

    # Deterministic edge weights generation based on indices
    for i in range(n):
        for j in range(m - 1):
            rt[i][j] = (i + j + 1) % 10 + 1
    for i in range(n - 1):
        for j in range(m):
            do[i][j] = (i * 2 + j + 3) % 10 + 1

    dp = [[0] * m for _ in range(n)]
    if k % 2 == 1:
        res = [[-1] * m for _ in range(n)]
        return res

    k //= 2
    dp_next = [[P] * m for _ in range(n)]
    for _ in range(k):
        for i in range(n):
            for j in range(m):
                ans = Inf
                if i != 0:
                    ans = min(ans, dp[i - 1][j] + do[i - 1][j])
                if j != 0:
                    ans = min(ans, dp[i][j - 1] + rt[i][j - 1])
                if i != n - 1:
                    ans = min(ans, dp[i + 1][j] + do[i][j])
                if j != m - 1:
                    ans = min(ans, dp[i][j + 1] + rt[i][j])
                dp_next[i][j] = ans

        for i in range(n):
            for j in range(m):
                dp[i][j] = dp_next[i][j]

    res = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            res[i][j] = 2 * dp[i][j]
    return res


def main(n):
    # Map single scale parameter n to grid n x n and k = n
    n_rows = n
    n_cols = n
    k_steps = n
    result = solve(n_rows, n_cols, k_steps)
    for row in result:
        # print(*row)
        pass
if __name__ == "__main__":
    main(5)