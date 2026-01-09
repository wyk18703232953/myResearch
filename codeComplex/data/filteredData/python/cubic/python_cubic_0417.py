def main(n):
    # Interpret n as grid size; ensure at least 1
    if n < 1:
        n = 1
    N = n
    M = n
    # Choose k as an even number proportional to n to exercise the loop
    k = 2 * n

    INF = 10**20 + 1

    # Deterministic generation of horizontal edge weights (N rows, M-1 edges each, plus INF sentinel)
    hor = []
    for i in range(N):
        row = []
        for j in range(M - 1):
            # Simple deterministic weight based on indices
            w = (i + 1) * (j + 2)
            row.append(w)
        row.append(INF)
        hor.append(row)

    # Deterministic generation of vertical edge weights (N-1 rows, M edges each, plus last row of INF)
    ver = []
    for i in range(N - 1):
        row = []
        for j in range(M):
            w = (i + 2) * (j + 1)
            row.append(w)
        ver.append(row)
    ver.append([INF] * M)

    # If k is odd, original logic prints -1 grid and exits
    if k & 1:
        for _ in range(N):
            # print(*([-1] * M))
            pass
        return

    dp = [[0] * M for _ in range(N)]
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

    for _ in range(k // 2):
        dp1 = [[10**20] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                for kk in range(4):
                    x1, y1 = i + dx[kk], j + dy[kk]
                    if 0 <= x1 < N and 0 <= y1 < M:
                        if kk < 2:
                            ed = hor[i][j - (kk == 1)]

                        else:
                            ed = ver[i - (kk == 3)][j]
                        if ed != INF:
                            val = 2 * ed + dp[x1][y1]
                            if val < dp1[i][j]:
                                dp1[i][j] = val
        dp = dp1

    for row in dp:
        # print(*row)
        pass
if __name__ == "__main__":
    # Example: run with n = 5
    main(5)