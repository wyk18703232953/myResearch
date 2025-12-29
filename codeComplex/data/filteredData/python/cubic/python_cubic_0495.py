import random

def main(n):
    # 规模 n 用来控制 N、M、K 的大小，这里做一个示例性设置：
    # 可根据实际需要调整生成规则
    N = n
    M = n
    # 保证 K 为偶数（原代码若 K 为奇数则全输出 -1）
    K = 2 * max(1, n // 2)

    # 生成测试数据：
    # A: N 行 M-1 列（水平边权）
    # B: N-1 行 M 列（垂直边权）
    # 为了保证非负权重，这里使用 1~9 的随机整数
    A = [[random.randint(1, 9) for _ in range(M - 1)] for _ in range(N)]
    B = [[random.randint(1, 9) for _ in range(M)] for _ in range(N - 1)]

    r = range(N)
    m = min

    # 若 K 为奇数，输出 -1 矩阵（与原逻辑一致，但此处 K 已设为偶数，仍保留逻辑）
    if K & 1:
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
    # 示例调用：n 可根据需要修改
    main(5)