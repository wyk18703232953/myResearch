def main(n):
    # Interpret n as grid size: n x n grid, and set k proportional to n
    global DR, DC, w, k, m
    DR = [1, 0, -1, 0]
    DC = [0, 1, 0, -1]

    # Grid dimensions
    m = n
    # Number of steps parameter (even to avoid trivial -1 case)
    k = 2 * n

    # Deterministic weight generation:
    # Horizontal edges: n rows, m-1 edges per row
    # We'll create an (n x m) grid for ease, unused edges can stay 0
    w = [[[0] * m for _ in range(n)] for _ in range(4)]

    # Fill "right" and "left" related weights (direction 1 and 3 in original code)
    # Original: w[1][r][c] = w[3][r][c + 1] = e
    # We generate e deterministically from (r, c)
    for r in range(n):
        for c in range(m - 1):
            e = (r + 1) * (c + 2)  # simple deterministic function
            w[1][r][c] = e
            w[3][r][c + 1] = e

    # Fill "down" and "up" related weights (direction 0 and 2 in original code)
    # Original: w[0][r][c] = w[2][r + 1][c] = e
    for r in range(n - 1):
        for c in range(m):
            e = (r + 2) * (c + 1)  # another deterministic function
            w[0][r][c] = e
            w[2][r + 1][c] = e

    INF = 10 ** 9

    def solve():
        global k
        global w
        if k % 2 == 1:
            return [[-1] * m for _ in range(n)]
        half_k = k // 2
        best = [[[0] * m for _ in range(n)] for _ in range(half_k + 1)]
        for steps in range(1, half_k + 1):
            for r in range(n):
                for c in range(m):
                    cur_best = INF
                    for d in range(4):
                        r2, c2 = r + DR[d], c + DC[d]
                        if 0 <= r2 < n and 0 <= c2 < m:
                            val = 2 * w[d][r][c] + best[steps - 1][r2][c2]
                            if val < cur_best:
                                cur_best = val
                    best[steps][r][c] = cur_best
        return best[half_k]

    res = solve()
    for row in res:
        # print(*row)
        pass
if __name__ == "__main__":
    # Example call for time-complexity experiments
    main(10)