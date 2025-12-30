import sys
from random import randint

mxm = sys.maxsize

def solve(p, q, r, n, m, row, col, dp):
    if p < 0 or p >= n or q < 0 or q >= m:
        return mxm

    if dp[r][p][q] != -1:
        return dp[r][p][q]

    if r == 0:
        return 0

    a = dp[r - 1][p][q - 1] if 0 <= q - 1 < m else mxm
    b = dp[r - 1][p][q + 1] if 0 <= q + 1 < m else mxm
    c = dp[r - 1][p - 1][q] if 0 <= p - 1 < n else mxm
    d = dp[r - 1][p + 1][q] if 0 <= p + 1 < n else mxm

    if a == -1 and 0 <= q - 1 < m:
        a = row[p][q - 1] + solve(p, q - 1, r - 1, n, m, row, col, dp)
    elif 0 <= q - 1 < m:
        a += row[p][q - 1]

    if b == -1 and 0 <= q + 1 < m:
        b = row[p][q] + solve(p, q + 1, r - 1, n, m, row, col, dp)
    elif 0 <= q + 1 < m:
        b += row[p][q]

    if c == -1 and 0 <= p - 1 < n:
        c = col[p - 1][q] + solve(p - 1, q, r - 1, n, m, row, col, dp)
    elif 0 <= p - 1 < n:
        c += col[p - 1][q]

    if d == -1 and 0 <= p + 1 < n:
        d = col[p][q] + solve(p + 1, q, r - 1, n, m, row, col, dp)
    elif 0 <= p + 1 < n:
        d += col[p][q]

    z = min(a, b, c, d)
    dp[r][p][q] = z
    return z

def main(n):
    # Generate test data based on n as the grid dimension; set m = n
    # and choose a reasonable even k proportional to n.
    m = n
    k = 2 * n  # ensure even, typical scale

    # Generate random weights for edges:
    # row: n rows, m-1 horizontal edges each, then append 0 as in original code.
    row = []
    for _ in range(n):
        line = [randint(1, 9) for _ in range(m - 1)] + [0]
        row.append(line)

    # col: n-1 rows, m vertical edges each, then append a row of zeros.
    col = []
    for _ in range(n - 1):
        line = [randint(1, 9) for _ in range(m)]
        col.append(line)
    col.append([0 for _ in range(m)])

    ans = [[-1 for _ in range(m)] for _ in range(n)]
    dp = [[[-1 for _ in range(m + 1)] for _ in range(n + 1)] for _ in range(k + 1)]

    if k % 2:
        for item in ans:
            print(*item)
        return

    half = k // 2
    for r in range(n):
        for c in range(m):
            res = solve(r, c, half, n, m, row, col, dp)
            ans[r][c] = 2 * res if res != mxm else -1

    for item in ans:
        print(*item)

if __name__ == "__main__":
    # Example: run main with n = 5
    main(5)