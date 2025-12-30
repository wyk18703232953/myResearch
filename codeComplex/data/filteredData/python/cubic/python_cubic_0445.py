from array import array
import random

def main(n):
    # 生成规模参数：
    # n: 行数
    # m: 列数（这里设为 n，形成 n x n 网格）
    # k: 步数（设为 2*n，保证是偶数，便于原算法发挥作用）
    m = n
    k = 2 * n

    # 生成测试数据：
    # left[i][j] 表示从 (i,j) 向右走到 (i,j+1) 的代价，大小为 n x (m-1)
    # down[i][j] 表示从 (i,j) 向下走到 (i+1,j) 的代价，大小为 (n-1) x m
    # 为了避免 0 权重，使用 [1, 10] 的随机整数
    left = [array("i", [random.randint(1, 10) for _ in range(m - 1)]) for _ in range(n)]
    down = [array("i", [random.randint(1, 10) for _ in range(m)]) for _ in range(n - 1)]

    # 原始逻辑
    dp = [array("i", [(-1 if k & 1 else 0) for _ in range(m)]) for _ in range(n)]
    if k & 1 == 0:
        for _ in range(k // 2):
            dp1 = [array("i", [10**8 for _ in range(m)]) for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    if j > 0:
                        dp1[i][j] = min(dp1[i][j], dp[i][j - 1] + 2 * left[i][j - 1])
                    if j < m - 1:
                        dp1[i][j] = min(dp1[i][j], dp[i][j + 1] + 2 * left[i][j])
                    if i > 0:
                        dp1[i][j] = min(dp1[i][j], dp[i - 1][j] + 2 * down[i - 1][j])
                    if i < n - 1:
                        dp1[i][j] = min(dp1[i][j], dp[i + 1][j] + 2 * down[i][j])
            dp = dp1

    # 输出结果
    for row in dp:
        print(*row)


if __name__ == "__main__":
    # 示例：调用 main(3) 生成一个 3x3 的测试
    main(3)