def main(n):
    # 生成测试数据：
    # N = n, M = n, K 为不超过 2n 的偶数（若 2n 为奇则用 2n-1 再减 1，确保偶数）
    N = n
    M = n
    K = 2 * n
    if K % 2 == 1:  # 若仍是奇数则减 1
        K -= 1
    if K <= 0:
        K = 2  # 至少为 2，保证有意义的计算

    # A: N x (M-1) 水平边权
    # B: (N-1) x M 垂直边权
    # 简单生成：权值为 (i+j+1)，可根据需要自行调整
    A = [[i + j + 1 for j in range(M - 1)] for i in range(N)] if M > 1 else [[] for _ in range(N)]
    B = [[i + j + 1 for j in range(M)] for i in range(N - 1)] if N > 1 else []

    r = range(N)
    m = min

    if K & 1:
        # 若K为奇数，输出全-1
        for _ in r:
            print(*([-1] * M))
        return

    X = [[0] * M for _ in r]
    for _ in range(1, K // 2 + 1):
        Y = [[9 ** 9] * M for _ in r]
        for i in r:
            for j in range(M):
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
        print(*x)


if __name__ == "__main__":
    # 示例：规模 n = 4
    main(4)