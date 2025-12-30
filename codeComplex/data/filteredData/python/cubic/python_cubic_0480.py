import random

M = 998244353
P = 1000000007
Inf = float('inf')


def solve(n, m, k, rt, do):
    """
    n x m grid
    rt[i][j]: cost to move from (i,j) to (i,j+1), for j in [0, m-2]
    do[i][j]: cost to move from (i,j) to (i+1,j), for i in [0, n-2]
    k: number of steps (total even; algorithm uses k//2 relaxations and doubles result)
    """
    dp = [[0] * m for _ in range(n)]

    if k % 2 == 1:
        for _ in range(n):
            print(*([-1] * m))
        return

    half_k = k // 2
    dp_next = [[P] * m for _ in range(n)]

    for _ in range(half_k):
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

    for i in range(n):
        for j in range(m):
            print(2 * dp[i][j], end=' ')
        print()


def main(n):
    """
    n: problem scale parameter; here used as both grid dimension and to derive k.
    Generates random test data and runs solve once.
    """
    # Example: make a nearly square grid with size close to n
    # and an even k proportional to n.
    if n <= 1:
        n_rows = 1
        n_cols = 1
    else:
        n_rows = max(1, n // 2)
        n_cols = max(1, n - n_rows)

    # Ensure at least a 1x1 grid
    n_rows = max(1, n_rows)
    n_cols = max(1, n_cols)

    k = max(2, 2 * (n_rows + n_cols))  # even k

    # Generate random positive weights
    # You can adjust the range as needed
    rt = [[0] * n_cols for _ in range(n_rows)]
    do = [[0] * n_cols for _ in range(max(0, n_rows - 1))]

    for i in range(n_rows):
        for j in range(n_cols - 1):
            rt[i][j] = random.randint(1, 10)

    for i in range(n_rows - 1):
        for j in range(n_cols):
            do[i][j] = random.randint(1, 10)

    solve(n_rows, n_cols, k, rt, do)


if __name__ == '__main__':
    # Example call; adjust or remove as needed.
    main(10)