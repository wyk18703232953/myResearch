import math
import random


def solve_instance(n, m, k, horizontal, vertical):
    # Original solve() logic, but parameterized instead of using input()
    if k % 2 or max(n, m) == 1:
        # Return a matrix of -1s
        return [[-1] * m for _ in range(n)]

    dp = [[[0] * (k // 2 + 1) for _ in range(m)] for _ in range(n)]
    for length in range(1, k // 2 + 1):
        for i in range(n):
            for j in range(m):
                left_path = math.inf if j == 0 else horizontal[i][j - 1] + dp[i][j - 1][length - 1]
                right_path = math.inf if j == m - 1 else horizontal[i][j] + dp[i][j + 1][length - 1]
                top_path = math.inf if i == 0 else vertical[i - 1][j] + dp[i - 1][j][length - 1]
                bottom_path = math.inf if i == n - 1 else vertical[i][j] + dp[i + 1][j][length - 1]
                dp[i][j][length] = min(left_path, right_path, top_path, bottom_path)

    res = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(dp[i][j][k // 2] * 2)
        res.append(row)
    return res


def main(n):
    """
    n: problem scale parameter.
       We will generate:
         - grid dimensions: n x n
         - k as an even number related to n
         - random weights for edges.
    """
    # You can adjust how m and k depend on n.
    # Here we choose a square grid n x n and k = 2 * min(n, n) (any even number is fine).
    m = n
    # Ensure k is even and not too small; choose something proportional to grid size
    k = 2 * max(1, n)

    # Generate test data
    # horizontal[i][j] : cost between (i,j) and (i,j+1), shape n x (m-1)
    horizontal = [[random.randint(1, 10) for _ in range(m - 1)] for _ in range(n)]
    # vertical[i][j]   : cost between (i,j) and (i+1,j), shape (n-1) x m
    vertical = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]

    ans = solve_instance(n, m, k, horizontal, vertical)

    # Output in the same format as original: n lines, each with m integers
    for i in range(n):
        print(*ans[i])


if __name__ == "__main__":
    # Example: run with n = 4
    main(4)