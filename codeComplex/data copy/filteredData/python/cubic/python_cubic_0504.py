def main(n):
    # 生成规模为 n 的测试数据：
    # N 行，M 列（这里取 M = n），K 为偶数且与规模相关（这里取 K = 2 * n 或至少为 2）
    N = n
    M = n
    K = 2 * max(1, n)  # 保证为正偶数

    r = range(N)
    m = min

    # 如果 K 为奇数，按题意全部输出 -1（这里保证 K 为偶数，一般不会触发）
    if K & 1:
        for _ in r:
            # print(*([-1] * M))
            pass
        return

    # 生成测试网格数据：
    # A: N 行，每行 M-1 个，表示左右方向边权重
    # B: N-1 行，每行 M 个，表示上下方向边权重
    # 为了有一定规律，使用简单的函数生成：A[i][j] = i+j+1, B[i][j] = i+j+1
    A = [[i + j + 1 for j in range(M - 1)] for i in range(N)]
    B = [[i + j + 1 for j in range(M)] for i in range(N - 1)]

    # 动态规划逻辑与原程序保持一致
    X = [[0] * M for _ in r]
    for _k in range(1, K // 2 + 1):
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
        # print(*x)
        pass
if __name__ == "__main__":
    # 示例：调用 main(3)
    main(3)