def main(n):
    # Map n to grid and steps in a deterministic way
    if n < 1:
        n = 1
    N = n
    M = n
    # Ensure K is even to avoid the trivial -1 output; tie to n for scaling
    K = 2 * ((n % 5) + 1)

    R = range
    m = min

    if K & 1:
        for _ in R(N):
            # print(*[-1] * M)
            pass
        return

    # Deterministic generation of A (N x (M-1)) and B ((N-1) x M)
    # Use simple arithmetic so values are reproducible
    A = [[(i * M + j + 1) % 7 + 1 for j in R(M - 1)] for i in R(N)]
    B = [[(i * M + j + 2) % 9 + 1 for j in R(M)] for i in R(N - 1)]

    X = [[0] * M for _ in R(N)]
    for _ in R(1, K // 2 + 1):
        Y = [[9 ** 9] * M for _ in R(N)]
        for i in R(N):
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