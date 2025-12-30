from math import inf
import random

def main(n):
    # 随机生成规模参数
    # n: 行数
    m = max(1, n)          # 列数，这里简单取 m = n，可按需修改
    k = 2 * random.randint(1, n)  # 生成一个偶数步数，避免全 -1 情况

    # 生成测试数据 A (n x m-1) 和 B (n-1 x m)
    # 权值范围可按需调整
    max_weight = 10**3
    A = [[random.randint(1, max_weight) for _ in range(m - 1)] for _ in range(n)]
    B = [[random.randint(1, max_weight) for _ in range(m)] for _ in range(n - 1)]

    # 如果 k 为奇数，输出 -1 矩阵并结束（按原逻辑，实际这里一般不会触发）
    if k & 1:
        for _ in range(n):
            print(' '.join(['-1'] * m))
        return

    # 动态规划计算
    X = [[0] * m for _ in range(n)]
    for _ in range(k // 2):
        Y = [[inf] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i:
                    Y[i][j] = X[i - 1][j] + 2 * B[i - 1][j]
                if i < n - 1:
                    Y[i][j] = min(Y[i][j], X[i + 1][j] + 2 * B[i][j])
                if j:
                    Y[i][j] = min(Y[i][j], X[i][j - 1] + 2 * A[i][j - 1])
                if j < m - 1:
                    Y[i][j] = min(Y[i][j], X[i][j + 1] + 2 * A[i][j])
        X = Y

    for row in X:
        print(*row)


if __name__ == "__main__":
    # 示例调用：n 可自行修改
    main(5)