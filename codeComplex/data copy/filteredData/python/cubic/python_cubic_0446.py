def main(n):
    # Interpret n as grid size parameter
    # N = n, M = n, K = 2 * n (even, grows with n)
    N = max(1, n)
    M = max(1, n)
    K = 2 * max(1, n)

    # Deterministic generation of A (N x (M-1)) and B ((N-1) x M)
    # Original A and B come from input; here we use simple arithmetic patterns
    if M > 1:
        A = [[(i + j + 1) for j in range(M - 1)] for i in range(N)]

    else:
        A = [[0] * 0 for _ in range(N)]

    if N > 1:
        B = [[(i + j + 2) for j in range(M)] for i in range(N - 1)]

    else:
        B = [[0] * M for _ in range(0)]

    # Core algorithm logic preserved
    X = [[0] * M for _ in range(N)]
    inf = 1 << 30

    if K % 2:
        # This branch will never trigger with K = 2 * n, but kept for fidelity
        for _ in range(N):
            # print(*[-1] * M)
            pass
        return

    for _k in range(1, K // 2 + 1):
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
    main(5)