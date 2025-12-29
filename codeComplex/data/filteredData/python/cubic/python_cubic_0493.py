from math import inf
import random

def main(n):
    # 生成规模参数
    # 为了可控，这里令 m 与 n 相同，k 为偶数（否则答案全为 -1）
    m = n
    k = 2 * n  # 可以根据需要调整为其他偶数，比如 2, 4, 6, ...

    # 生成测试数据：水平和垂直边的权值（正整数）
    # horizontal: n 行，每行 m-1 个数
    # vertical:   n-1 行，每行 m 个数
    random.seed(0)
    horizontal = [[random.randint(1, 10) for _ in range(m - 1)] for _ in range(n)]
    vertical = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]

    if k & 1:
        ans = ["-1"] * m
        for _ in range(n):
            print(*ans)
    else:
        grid = [[0 for _ in range(m)] for _ in range(n)]
        for _ in range(k // 2):
            X = [[inf for _ in range(m)] for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    if i >= 1:
                        X[i][j] = min(2 * vertical[i - 1][j] + grid[i - 1][j], X[i][j])
                    if i < n - 1:
                        X[i][j] = min(2 * vertical[i][j] + grid[i + 1][j], X[i][j])
                    if j >= 1:
                        X[i][j] = min(2 * horizontal[i][j - 1] + grid[i][j - 1], X[i][j])
                    if j < m - 1:
                        X[i][j] = min(2 * horizontal[i][j] + grid[i][j + 1], X[i][j])
            grid = X
        for i in range(n):
            print(*grid[i])


# 示例调用
if __name__ == "__main__":
    main(4)