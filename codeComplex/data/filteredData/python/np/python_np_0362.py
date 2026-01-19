def main(n):
    # n controls problem size deterministically
    T = max(1, n // 5)
    base_N = max(1, n)
    base_M = max(1, (n // 2) + 1)

    results = []
    for case in range(T):
        N = base_N + case
        M = max(1, base_M - case if base_M > case else 1)

        X = [[(i * M + j + case) % 100 for j in range(M)] for i in range(N)]
        Y = [[X[i][j] for i in range(N)] for j in range(M)]

        ma = 0
        for t in range(99):
            for i in range(M):
                a = (t + i + case) % N
                Y[i] = [Y[i][(j - a) % N] for j in range(N)]
            current = 0
            for j in range(N):
                col_max = Y[0][j]
                for i in range(1, M):
                    if Y[i][j] > col_max:
                        col_max = Y[i][j]
                current += col_max
            if current > ma:
                ma = current
        results.append(ma)

    for v in results:
        print(v)


if __name__ == "__main__":
    main(10)