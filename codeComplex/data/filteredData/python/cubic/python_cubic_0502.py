def main(n):
    # 根据规模 n 生成测试数据
    # 这里假设 N = M = n，K 取一个与 n 相关的偶数步数（例如 2*n）
    N = n
    M = n
    K = 2 * n  # 必须偶数，否则直接输出 -1；这里保证为偶数

    # 生成 A (N x (M-1)) 和 B ((N-1) x M) 的非负权重
    # A[i][j]: (i,j) 与 (i,j+1) 之间的边权
    # B[i][j]: (i,j) 与 (i+1,j) 之间的边权
    A = [[(i + j) % 9 + 1 for j in range(M - 1)] for i in range(N)]
    B = [[(i * 2 + j) % 9 + 1 for j in range(M)] for i in range(N - 1)]

    r = range(N)
    INF = 9 ** 9
    m = min

    # 若 K 为奇数，无法回到原点，输出 -1（保持与原逻辑一致）
    if K & 1:
        for _ in r:
            print(*([-1] * M))
        return

    # DP：X[i][j] 为当前步数下，从 (i,j) 出发走指定步数后回到同一格的最小代价的一半
    X = [[0] * M for _ in r]

    for _ in range(1, K // 2 + 1):
        Y = [[INF] * M for _ in r]
        for i in r:
            for j in range(M):
                if i:  # 从上方来
                    Y[i][j] = X[i - 1][j] + 2 * B[i - 1][j]
                if i < N - 1:  # 从下方来
                    Y[i][j] = m(Y[i][j], X[i + 1][j] + 2 * B[i][j])
                if j:  # 从左侧来
                    Y[i][j] = m(Y[i][j], X[i][j - 1] + 2 * A[i][j - 1])
                if j < M - 1:  # 从右侧来
                    Y[i][j] = m(Y[i][j], X[i][j + 1] + 2 * A[i][j])
        X = Y

    for row in X:
        print(*row)


if __name__ == "__main__":
    # 示例：运行 main(3)
    main(3)