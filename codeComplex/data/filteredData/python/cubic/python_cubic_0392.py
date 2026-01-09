def main(n):
    # Interpret n as grid size parameter: N = M = n, K = 2*n (even)
    N = n
    M = n
    K = 2 * n if 2 * n > 0 else 2  # ensure K >= 2 and even

    # Since we control K, it will always be even; no need for the odd-K early exit logic

    # Deterministically generate A (N x M) and B (N-1 x M)
    # Example pattern: A[i][j] = (i + j) % 9 + 1, B[i][j] = (i * 2 + j) % 9 + 1
    A = [[(i + j) % 9 + 1 for j in range(M)] for i in range(N)]
    if N > 1:
        B = [[(i * 2 + j) % 9 + 1 for j in range(M)] for i in range(N - 1)]

    else:
        B = []

    X = [[0] * M for _ in range(N)]
    inf = 1 << 30

    for _ in range(1, K // 2 + 1):
        nX = [[inf] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if i:
                    nX[i][j] = min(nX[i][j], X[i - 1][j] + B[i - 1][j])
                if i < N - 1:
                    nX[i][j] = min(nX[i][j], X[i + 1][j] + B[i][j])
                if j:
                    nX[i][j] = min(nX[i][j], X[i][j - 1] + A[i][j - 1])
                if j < M - 1:
                    nX[i][j] = min(nX[i][j], X[i][j + 1] + A[i][j])
        X = nX

    for x in X:
        # print(*[a * 2 for a in x])
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n to change input scale
    main(5)