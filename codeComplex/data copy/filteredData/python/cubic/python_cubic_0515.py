def main(n):
    # 生成测试数据（根据规模 n 构造一个 N x M 的网格和相关权重）
    # 这里示例设定：
    #   N = n, M = n, K = 2 * n（保证为偶数）
    #   A: N x (M-1) 的水平边权重，全部设为 1
    #   B: (N-1) x M 的竖直边权重，全部设为 1
    N = n
    M = n
    K = 2 * n  # 必为偶数，便于演示（原代码对 K 为奇数时直接输出 -1）

    # 若要测试 K 为奇数的情况，可改为：K = 2 * n + 1

    # 构造 A：N 行，每行 M-1 个元素
    A = [[1] * (M - 1) for _ in range(N)] if M > 1 else [[ ] for _ in range(N)]
    # 构造 B：N-1 行，每行 M 个元素
    B = [[1] * M for _ in range(N - 1)] if N > 1 else []

    R = range
    m = min
    r = R(N)

    if K & 1:
        for _ in r:
            # print(*([-1] * M))
            pass
        return

    X = [[0] * M for _ in r]
    for _ in R(1, K // 2 + 1):
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
    # 示例调用：n = 3 时，生成 3x3 网格、K=6 的测试
    main(3)