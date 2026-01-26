import sys

mxm = sys.maxsize

def solve(p, q, r, n, m, row, col, dp):
    if p < 0 or p >= n or q < 0 or q >= m:
        return mxm

    if dp[r][p][q] != -1:
        return dp[r][p][q]

    if r == 0:
        return 0

    z = int()
    a = dp[r - 1][p][q - 1] if 0 <= q - 1 < m else mxm
    b = dp[r - 1][p][q + 1] if 0 <= q + 1 < m else mxm
    c = dp[r - 1][p - 1][q] if 0 <= p - 1 < n else mxm
    d = dp[r - 1][p + 1][q] if 0 <= p + 1 < n else mxm

    if a == -1 and 0 <= q - 1 < m:
        a = row[p][q - 1] + solve(p, q - 1, r - 1, n, m, row, col, dp)
    elif a != mxm and 0 <= q - 1 < m:
        a += row[p][q - 1]

    if b == -1 and 0 <= q + 1 < m:
        b = row[p][q] + solve(p, q + 1, r - 1, n, m, row, col, dp)
    elif b != mxm and 0 <= q + 1 < m:
        b += row[p][q]

    if c == -1 and 0 <= p - 1 < n:
        c = col[p - 1][q] + solve(p - 1, q, r - 1, n, m, row, col, dp)
    elif c != mxm and 0 <= p - 1 < n:
        c += col[p - 1][q]

    if d == -1 and 0 <= p + 1 < n:
        d = col[p][q] + solve(p + 1, q, r - 1, n, m, row, col, dp)
    elif d != mxm and 0 <= p + 1 < n:
        d += col[p][q]

    z = min(a, b, c, d)
    dp[r][p][q] = z
    return z

def generate_data(n):
    # Map n to grid size n x n and steps k = n
    if n <= 0:
        n = 1
    m = n
    k = n

    # Deterministic construction of row and col costs
    # row[i][j] is cost from (i,j) to (i,j+1)
    row = []
    for i in range(n):
        row.append([(i + j) % 7 + 1 for j in range(m)])

    # col[i][j] is cost from (i,j) to (i+1,j)
    col = []
    for i in range(n - 1):
        col.append([(i * 3 + j * 2) % 9 + 1 for j in range(m)])
    col.append([0 for _ in range(m)])

    return n, m, k, row, col

def main(n):
    n, m, k, row, col = generate_data(n)

    ans = [[-1 for _ in range(m)] for _ in range(n)]
    dp = [[[-1 for _ in range(m + 1)] for _ in range(n + 1)] for _ in range(k + 1)]

    if k % 2:
        for item in ans:
            # print(*item)
            pass
        return

    half = k // 2
    for r in range(n):
        for c in range(m):
            ans[r][c] = 2 * solve(r, c, half, n, m, row, col, dp)

    for item in ans:
        # print(*item)
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n to change input scale
    main(5)