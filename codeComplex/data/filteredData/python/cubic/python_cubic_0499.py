import random

def main(n):
    # 规模参数：使用 n 作为 N，M，K 则由 n 派生或固定
    N = n
    M = n
    # 这里给出一个示例：令 K = 2 * n （保证为偶数）
    # 如需其他策略，可按需修改
    K = 2 * n

    # 生成测试数据 A, B
    # A: N x (M-1) 的非负权重
    # B: (N-1) x M 的非负权重
    # 可以根据需要调整随机范围
    A = [[random.randint(1, 9) for _ in range(M - 1)] for _ in range(N)]
    B = [[random.randint(1, 9) for _ in range(M)] for _ in range(N - 1)]

    # 若 K 为奇数，输出 -1 矩阵（按原逻辑）
    if K & 1:
        for _ in range(N):
            print(*([-1] * M))
        return

    R = range
    m = min

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
        print(*x)


if __name__ == "__main__":
    # 示例调用：n=4
    main(4)