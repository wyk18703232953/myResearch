def main(n):
    # Map n to problem dimensions and K
    # Ensure at least 1x1 grid and even K
    N = max(1, n)
    M = max(1, n)
    K = max(2, (n // 2) * 2)

    R = range
    m = min

    r = R(N)

    if K & 1:
        for _ in r:
            # print(*([-1] * M))
            pass
        return

    # Deterministic generation of A and B based on N, M
    # A: N x M
    A = [[(i + j) % 7 + 1 for j in R(M)] for i in r]
    # B: (N-1) x M (if N == 1, B is empty list)
    if N > 1:
        B = [[(i * 3 + j * 5) % 11 + 1 for j in R(M)] for i in R(N - 1)]

    else:
        B = []

    X = [[0] * M for _ in r]

    for k in R(1, K // 2 + 1):
        Y = [[9 ** 9] * M for _ in r]
        for i in r:
            for j in R(M):
                if i:
                    Y[i][j] = X[i - 1][j] + 2 * B[i - 1][j]
                if i < N - 1:
                    Y[i][j] = m(Y[i][j], X[i + 1][j] + 2 * B[i][j])
                if j:
                    Y[i][j] = m(Y[i][j], X[i][j - 1] + 2 * A[i][j - 1])
                if j < M - 1:
                    Y[i][j] = m(Y[i][j], X[i][j + 1] + 2 * A[i][j])
        X = Y

    for x in X:
        # print(*x)
        pass
if __name__ == "__main__":
    main(5)