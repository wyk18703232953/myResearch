def main(n):
    MOD = 1000000000007
    MAX = 1000000000

    # Map n to grid size and K (path length parameter)
    # Choose N = M = max(1, n), K = 2 * max(1, n) to ensure K is even
    N = max(1, n)
    M = max(1, n)
    K = 2 * max(1, n)

    # Deterministic weight generation instead of input
    # W[i][j] = [L, R, U, D]
    W = [[[MAX, MAX, MAX, MAX] for _ in range(M)] for _ in range(N)]

    # Horizontal edges: for each row i, edges between (i,j) and (i,j+1)
    # weight is (i + j + 1) % 17 + 1 (any simple deterministic formula)
    for i in range(N):
        # l length = M - 1
        l = [((i + j + 1) % 17) + 1 for j in range(M - 1)]
        for j in range(M - 1):
            W[i][j][1] = l[j]       # R from (i,j) to (i,j+1)
            W[i][j + 1][0] = l[j]   # L from (i,j+1) to (i,j)

    # Vertical edges: for each column j, edges between (i,j) and (i+1,j)
    # weight is (i*7 + j*3 + 2) % 19 + 1
    for i in range(N - 1):
        l = [((i * 7 + j * 3 + 2) % 19) + 1 for j in range(M)]
        for j in range(M):
            W[i][j][3] = l[j]       # D from (i,j) to (i+1,j)
            W[i + 1][j][2] = l[j]   # U from (i+1,j) to (i,j)

    # Core logic from original program
    if K % 2 == 1:
        for _ in range(N):
            ans = ["-1"] * M
            # print(" ".join(ans))
            pass

    else:
        K_half = K // 2
        dp = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(K_half + 1)]
        dl = ((0, -1), (0, 1), (-1, 0), (1, 0))  # L, R, U, D

        for kt in range(1, K_half + 1):
            for i in range(N):
                for j in range(M):
                    best = MAX
                    for t, (di, dj) in enumerate(dl):
                        ni = i + di
                        nj = j + dj
                        if 0 <= ni < N and 0 <= nj < M:
                            val = dp[kt - 1][ni][nj] + W[i][j][t] * 2
                            if val < best:
                                best = val
                    dp[kt][i][j] = best

        for i in range(N):
            ans = [str(dp[K_half][i][j]) for j in range(M)]
            # print(" ".join(ans))
            pass
if __name__ == "__main__":
    main(5)