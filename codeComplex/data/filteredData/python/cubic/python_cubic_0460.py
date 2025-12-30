import random


def main(n):
    # 规模参数：用 n 控制 N、M、K 的大小
    # 这里示例设定：
    #   N = n, M = n, K = 2n（偶数以触发主逻辑）
    # 你可以根据需要自行调整规则。
    N = n
    M = n
    K = 2 * n  # 必须是偶数，否则原算法直接输出 -1

    # 生成测试数据：
    # A: N x (M-1) 的水平边权，原程序读的是 N 行，每行 M-1 个数
    # B: (N-1) x M 的垂直边权，原程序读的是 N-1 行，每行 M 个数
    #
    # 原码中 A, B 的输入尺寸在题面中约定，这里按典型网格边权维度生成。
    # 若想沿用原代码的读法（A 为 N x M, B 为 N-1 x M），
    # 也可以在此稍微调整；下面给出严格对应原逻辑的尺寸生成。

    # 对应原程序的读取方式：
    # A: N x M
    # B: (N-1) x M
    # 为避免边界访问产生歧义，我们填满这些矩阵即可。
    max_weight = 10  # 边权上限，可调整
    random.seed(0)

    A = [[random.randint(1, max_weight) for _ in range(M)] for _ in range(N)]
    B = [[random.randint(1, max_weight) for _ in range(M)] for _ in range(N - 1)]

    # 主逻辑：从原程序迁移
    if K % 2:
        for _ in range(N):
            print(*[-1] * M)
        return

    X = [[0] * M for _ in range(N)]
    inf = 1 << 30

    for _step in range(1, K // 2 + 1):
        nX = [[inf] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if i:
                    nX[i][j] = min(nX[i][j], X[i - 1][j] + B[i - 1][j])
                if i < N - 1:
                    nX[i][j] = min(nX[i][j], X[i + 1][j] + B[i][j])
                if j:
                    nX[i][j] = min(nX[i][j], X[i][j - 1] + A[i][j - 1])
                if j < M - 1:
                    nX[i][j] = min(nX[i][j], X[i][j + 1] + A[i][j])
        X = nX

    for x in X:
        print(*[a * 2 for a in x])


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)