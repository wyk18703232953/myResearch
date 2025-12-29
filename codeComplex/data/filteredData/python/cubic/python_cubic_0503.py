def main(n):
    # 生成测试数据：根据规模 n 构造一个 N×M 网格
    # 这里简单设定 N = M = n，K = 偶数（例如 2n）
    N = n
    M = n
    K = 2 * n  # 必须为偶数，否则原逻辑整体输出 -1

    # 若需要可改为任何偶数 K
    if K % 2 == 1:
        # 原程序在 K 为奇数时全部输出 -1
        for _ in range(N):
            print(*([-1] * M))
        return

    # 生成 A (N × (M-1))，B ((N-1) × M) 的测试数据
    # A[i][j] 表示 (i,j) 与 (i,j+1) 的边权
    # B[i][j] 表示 (i,j) 与 (i+1,j) 的边权
    # 随机或构造均可，这里用简单的递增构造，数值在 1~9 之间循环
    A = []
    val = 1
    for i in range(N):
        row = []
        for j in range(M - 1):
            row.append(val)
            val = val % 9 + 1
        A.append(row)

    B = []
    for i in range(N - 1):
        row = []
        for j in range(M):
            row.append(val)
            val = val % 9 + 1
        B.append(row)

    # 以下为原算法逻辑
    r = range(N)
    m = min

    # DP：X[i][j] 表示在走了 2*(k-1) 步后，从 (i,j) 出发再走 2*(k-1) 步的最小代价
    X = [[0] * M for _ in r]

    # 每次循环 k，计算走 2k 步的最小代价
    for _k in range(1, K // 2 + 1):
        Y = [[9 ** 9] * M for _ in r]
        for i in r:
            for j in range(M):
                # 向上/下走（通过 B）
                if i:
                    Y[i][j] = X[i - 1][j] + 2 * B[i - 1][j]
                if i < N - 1:
                    Y[i][j] = m(Y[i][j], X[i + 1][j] + 2 * B[i][j])

                # 向左/右走（通过 A）
                if j:
                    Y[i][j] = m(Y[i][j], X[i][j - 1] + 2 * A[i][j - 1])
                if j < M - 1:
                    Y[i][j] = m(Y[i][j], X[i][j + 1] + 2 * A[i][j])
        X = Y

    for x in X:
        print(*x)


if __name__ == "__main__":
    # 示例：调用 main(3)
    main(3)