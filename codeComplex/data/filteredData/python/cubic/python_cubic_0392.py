import random

def main(n):
    # n 用作规模参数，这里设置 N = M = max(1, n)，K 为偶数步数（例如 4）
    N = max(1, n)
    M = max(1, n)
    K = 4
    # 若希望测试奇数情况，可改为 K = 3 或其他奇数

    # 生成测试数据 A, B：正权重
    # A[i][j] 表示 (i,j) 与 (i,j+1) 之间的边权
    # B[i][j] 表示 (i,j) 与 (i+1,j) 之间的边权
    random.seed(0)
    A = [[random.randint(1, 10) for _ in range(M - 1)] for _ in range(N)]
    B = [[random.randint(1, 10) for _ in range(M)] for _ in range(N - 1)]

    if K % 2:
        for _ in range(N):
            print(*[-1] * M)
        return

    X = [[0] * M for _ in range(N)]
    inf = 1 << 30

    for _ in range(1, K // 2 + 1):
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
    # 示例：n = 5
    main(5)