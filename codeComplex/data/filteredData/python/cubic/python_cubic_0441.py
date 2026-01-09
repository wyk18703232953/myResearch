import sys
from math import inf

mod = 10 ** 9 + 7
mod2 = 998244353

def l1d(n, val=0):
    return [val for _ in range(n)]

def l2d(n, m, val=0):
    return [l1d(m, val) for _ in range(n)]

def generate_grid(n):
    # Map n to a reasonable 2D grid size and k
    # Here: n controls both dimensions and k
    if n < 2:
        n = 2
    rows = n
    cols = n
    # k must be even or odd is also allowed, algorithm handles both
    k = n

    # Deterministic weights for horizontal and vertical edges
    # hor: rows x (cols - 1)
    hor = [[(i + j + 1) % 9 + 1 for j in range(cols - 1)] for i in range(rows)]
    # ver: (rows - 1) x cols
    ver = [[(i * 2 + j + 3) % 9 + 1 for j in range(cols)] for i in range(rows - 1)]

    return rows, cols, k, hor, ver

def core_algorithm(n, m, k, hor, ver):
    if k % 2 == 1:
        ml = l2d(n, m, -1)
        return ml

    k //= 2
    dp = [l2d(n, m, 0) for _ in range(k + 1)]
    for f in range(1, k + 1):
        for i in range(n):
            for j in range(m):
                a = inf
                if i != 0:
                    a = min(a, 2 * ver[i - 1][j] + dp[f - 1][i - 1][j])
                if i != n - 1:
                    a = min(a, 2 * ver[i][j] + dp[f - 1][i + 1][j])
                if j != 0:
                    a = min(a, 2 * hor[i][j - 1] + dp[f - 1][i][j - 1])
                if j != m - 1:
                    a = min(a, 2 * hor[i][j] + dp[f - 1][i][j + 1])
                dp[f][i][j] = a
    return dp[-1]

def main(n):
    rows, cols, k, hor, ver = generate_grid(n)
    result = core_algorithm(rows, cols, k, hor, ver)
    for row in result:
        # print(*row)
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(5)