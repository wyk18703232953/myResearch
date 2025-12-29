import random

def main(n):
    # 规模 n 用来控制 N, M, K 的大小，这里做一个简单的设定：
    # N, M ~ n，K 为不超过 n 的偶数（若 n 为奇数则用 n-1；n=1 时 K=0）
    if n <= 1:
        N = M = 1
        K = 0
    else:
        N = n
        M = n
        K = n if n % 2 == 0 else n - 1

    # 生成测试数据：
    # A: N x (M-1) 的权值（左右边）
    # B: (N-1) x M 的权值（上下边）
    # 这里使用 1~9 的随机整数作为边权
    A = [[random.randint(1, 9) for _ in range(M - 1)] for _ in range(N)]
    B = [[random.randint(1, 9) for _ in range(M)] for _ in range(N - 1)]

    # 如果 K 为奇数，程序原逻辑是输出全 -1；这里同样保持逻辑
    if K & 1:
        for _ in range(N):
            print(*([-1] * M))
        return

    r = range(N)
    X = [[0] * M for _ in r]
    INF = 9 ** 9

    for _ in range(1, K // 2 + 1):
        Y = [[INF] * M for _ in r]
        for i in r:
            for j in range(M):
                if i:
                    Y[i][j] = X[i - 1][j] + 2 * B[i - 1][j]
                if i < N - 1:
                    Y[i][j] = min(Y[i][j], X[i + 1][j] + 2 * B[i][j])
                if j:
                    Y[i][j] = min(Y[i][j], X[i][j - 1] + 2 * A[i][j - 1])
                if j < M - 1:
                    Y[i][j] = min(Y[i][j], X[i][j + 1] + 2 * A[i][j])
        X = Y

    for x in X:
        print(*x)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)