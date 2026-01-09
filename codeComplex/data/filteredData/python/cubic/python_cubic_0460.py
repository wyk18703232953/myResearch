def main(n):
    # Map n to grid dimensions and steps
    if n <= 0:
        return
    N = max(1, n)
    M = max(1, n)
    # Ensure K is even to exercise the main logic
    K = 2 * ((n % 5) + 1)

    if K % 2:
        for _ in range(N):
            # print(*[-1] * M)
            pass
        return

    # Deterministic construction of A (N x M-1) and B (N-1 x M)
    A = [[(i * M + j) % 7 + 1 for j in range(M - 1)] for i in range(N)]
    B = [[(i * M + j * 3) % 9 + 1 for j in range(M)] for i in range(N - 1)]

    X = [[0] * M for _ in range(N)]
    inf = 1 << 30
    for _k in range(1, K // 2 + 1):
        nX = [[inf] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if i:
                    cost = X[i - 1][j] + B[i - 1][j]
                    if cost < nX[i][j]:
                        nX[i][j] = cost
                if i < N - 1:
                    cost = X[i + 1][j] + B[i][j]
                    if cost < nX[i][j]:
                        nX[i][j] = cost
                if j:
                    cost = X[i][j - 1] + A[i][j - 1]
                    if cost < nX[i][j]:
                        nX[i][j] = cost
                if j < M - 1:
                    cost = X[i][j + 1] + A[i][j]
                    if cost < nX[i][j]:
                        nX[i][j] = cost
        X = nX

    for x in X:
        # print(*[a * 2 for a in x])
        pass
if __name__ == "__main__":
    main(5)