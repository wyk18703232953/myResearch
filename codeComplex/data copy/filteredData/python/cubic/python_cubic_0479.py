import math

M = 998244353
P = 1000000007
Inf = float('inf')


def find_gt(a, x):
    i = 0
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1

        else:
            hi = mid
    i = lo
    if i != len(a):
        return i

    else:
        return len(a)


def solve(n, m, k, rt, do):
    dp = [[0] * m for _ in range(n)]
    if k % 2 == 1:
        res = []
        for _ in range(n):
            res.append([-1] * m)
        return res
    k //= 2
    for _ in range(k):
        dp_next = [[P] * m for _ in range(n)]
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
        dp = dp_next
    res = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(2 * dp[i][j])
        res.append(row)
    return res


def main(n):
    # Interpret n as grid dimension; keep it at least 2 for edges to exist
    if n < 2:
        n = 2
    # Use a simple deterministic mapping from n to (rows, cols, k)
    # Here: n x n grid, k = n (evened if needed)
    rows = n
    cols = n
    k = n
    if k % 2 == 1:
        k += 1

    # Deterministic generation of rt (n x m) and do ((n-1) x m)
    # rt[i][j]: horizontal edge cost from (i,j) to (i,j+1), j in [0, m-2]
    # do[i][j]: vertical edge cost from (i,j) to (i+1,j), i in [0, n-2]
    rt = [[0] * cols for _ in range(rows)]
    do = [[0] * cols for _ in range(rows - 1)]

    for i in range(rows):
        for j in range(cols - 1):
            # simple positive cost depending on i,j
            rt[i][j] = (i + 1) * (j + 2)

    for i in range(rows - 1):
        for j in range(cols):
            do[i][j] = (i + 2) * (j + 1)

    result = solve(rows, cols, k, rt, do)

    for row in result:
        # print(*row)
        pass
if __name__ == "__main__":
    main(5)