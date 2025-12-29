import random

def main(n):
    # 规模约定：n 决定 N, M, K
    # 你可以根据需要调整下面的生成规则
    N = n
    M = n
    # 保证为偶数，且至少为 2
    K = max(2, (n // 2) * 2)

    # 生成测试数据：正权重
    # A: N x (M-1)
    # B: (N-1) x M
    max_w = 10
    A = [[random.randint(1, max_w) for _ in range(M - 1)] for _ in range(N)]
    B = [[random.randint(1, max_w) for _ in range(M)] for _ in range(N - 1)]

    if K % 2:
        for _ in range(N):
            print(*[-1] * M)
        return

    X = [[0] * M for _ in range(N)]
    inf = 1 << 60
    for _ in range(1, K // 2 + 1):
        nX = [[inf] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if i:  # move up
                    nX[i][j] = min(nX[i][j], X[i - 1][j] + B[i - 1][j])
                if i < N - 1:  # move down
                    nX[i][j] = min(nX[i][j], X[i + 1][j] + B[i][j])
                if j:  # move left
                    nX[i][j] = min(nX[i][j], X[i][j - 1] + A[i][j - 1])
                if j < M - 1:  # move right
                    nX[i][j] = min(nX[i][j], X[i][j + 1] + A[i][j])
        X = nX

    for x in X:
        print(*[a * 2 for a in x])


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)