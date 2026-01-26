def main(n):
    # Interpret n as grid size n x n; set k as an even function of n
    if n <= 0:
        return
    m = n
    k = 2 * n  # even, scales with n

    # Deterministic construction of YOKO and TATE based on indices
    YOKO = [[(i + j + 1) for j in range(m - 1)] + [0] for i in range(n)]
    TATE = [[(i + j + 2) for j in range(m)] for i in range(n - 1)]

    if k % 2 == 1:
        for _ in range(n):
            # print(*([-1] * m))
            pass
        return

    DP = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            MIN = 1 << 30

            if j - 1 >= 0:
                MIN = min(MIN, YOKO[i][j - 1] * 2)
            if j < m - 1:
                MIN = min(MIN, YOKO[i][j] * 2)

            if i - 1 >= 0:
                MIN = min(MIN, TATE[i - 1][j] * 2)
            if i < n - 1:
                MIN = min(MIN, TATE[i][j] * 2)

            DP[i][j] = MIN

    DP0 = [row[:] for row in DP]

    for _ in range(k // 2 - 1):
        NDP = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                MIN = DP[i][j] + DP0[i][j]

                if 0 <= i + 1 < n:
                    MIN = min(MIN, TATE[i][j] * 2 + DP[i + 1][j])

                if 0 <= i - 1 < n:
                    MIN = min(MIN, TATE[i - 1][j] * 2 + DP[i - 1][j])

                if 0 <= j + 1 < m:
                    MIN = min(MIN, YOKO[i][j] * 2 + DP[i][j + 1])

                if 0 <= j - 1 < m:
                    MIN = min(MIN, YOKO[i][j - 1] * 2 + DP[i][j - 1])

                NDP[i][j] = MIN
        DP = NDP

    for dp in DP:
        # print(*dp)
        pass
if __name__ == "__main__":
    main(5)