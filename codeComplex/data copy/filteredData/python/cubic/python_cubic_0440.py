import math

mod = 10**9 + 7
mod2 = 998244353
inf = math.inf

def l1d(n, val=0):
    return [val for _ in range(n)]

def l2d(n, m, val=0):
    return [l1d(m, val) for _ in range(n)]

def main(n):
    # Map n to grid size and k (path length / 2)
    # Choose n as total scale; let rows = cols ≈ sqrt(n), k ≈ sqrt(n)
    if n < 4:
        n = 4
    side = int(n**0.5)
    if side < 2:
        side = 2
    rows = side
    cols = side
    k = side * 2  # even k to avoid immediate -1 case, scales with n

    # Deterministic generation of hor and ver edge weights
    # hor: rows x (cols-1)
    # ver: (rows-1) x cols
    hor = []
    for i in range(rows):
        row = []
        for j in range(cols - 1):
            # simple deterministic function of (i, j)
            val = (i + 1) * (j + 2)
            row.append(val)
        hor.append(row)

    ver = []
    for i in range(rows - 1):
        row = []
        for j in range(cols):
            # simple deterministic function of (i, j)
            val = (i + 2) * (j + 1)
            row.append(val)
        ver.append(row)

    if k % 2 == 1:
        ml = l2d(rows, cols, -1)
        for row in ml:
            # print(*row)
            pass
        return

    k //= 2
    dp = [l2d(rows, cols) for _ in range(k + 1)]

    for f in range(1, k + 1):
        for i in range(rows):
            for j in range(cols):
                a = inf
                if i != 0:
                    a = min(a, 2 * ver[i - 1][j] + dp[f - 1][i - 1][j])
                if i != rows - 1:
                    a = min(a, 2 * ver[i][j] + dp[f - 1][i + 1][j])
                if j != 0:
                    a = min(a, 2 * hor[i][j - 1] + dp[f - 1][i][j - 1])
                if j != cols - 1:
                    a = min(a, 2 * hor[i][j] + dp[f - 1][i][j + 1])
                dp[f][i][j] = a

    for row in dp[-1]:
        # print(*row)
        pass
if __name__ == "__main__":
    main(1000)