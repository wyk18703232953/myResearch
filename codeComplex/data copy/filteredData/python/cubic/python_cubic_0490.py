from math import inf

def main(n):
    # Interpret n as grid size n x n, and k as an even value derived from n
    if n <= 1:
        n = 2
    m = n
    k = (n // 2) * 2  # ensure k is even and scales with n
    if k == 0:
        k = 2

    # Deterministic generation of A (n x m) and B (n-1 x m)
    # A[i][j] and B[i][j] are positive integers depending on indices
    A = [[(i + j + 1) for j in range(m)] for i in range(n)]
    B = [[(i + j + 2) for j in range(m)] for i in range(n - 1)]

    # Core logic from original code
    if k & 1:
        for _ in range(n):
            # print('-1 ' * m)
            pass
        return

    X = [[0] * m for _ in range(n)]
    for _ in range(k // 2):
        Y = [[inf] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i:
                    Y[i][j] = X[i - 1][j] + 2 * B[i - 1][j]
                if i < n - 1:
                    Y[i][j] = min(Y[i][j], X[i + 1][j] + 2 * B[i][j])
                if j:
                    Y[i][j] = min(Y[i][j], X[i][j - 1] + 2 * A[i][j - 1])
                if j < m - 1:
                    Y[i][j] = min(Y[i][j], X[i][j + 1] + 2 * A[i][j])
        X = Y

    for row in X:
        # print(*row)
        pass
if __name__ == "__main__":
    main(5)