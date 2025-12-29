def main(n):
    """
    参数:
        n: 网格大小，将生成 n x n 的网格
    说明:
        原题有 n, m, k，这里为了参数化简化：
        - 使用 n 作为行数和列数: m = n
        - 令 k = 2*n（保证为偶数，且步数规模与网格规模相关）
        - 根据 n 随机/规则生成 left 和 down 矩阵的测试数据
    """

    import random

    # 派生参数
    m = n
    k = 2 * n  # 可根据需要调整规则，只要是非负整数即可

    # 生成测试数据
    # left: n x (m-1)，但原代码中 left[i] 是长度 m 的列表，其中使用到的是
    # left[i][j-1] 和 left[i][j] (j从0到m-1)，因此这里直接生成 n x m，未使用的位置无影响
    left = [[random.randint(1, 10) for _ in range(m)] for _ in range(n)]
    # down: (n-1) x m，同理保持为 n-1 行，每行 m 列
    down = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]

    # 原逻辑开始
    dp = [[(-1 if k & 1 else 0) for _ in range(m)] for _ in range(n)]
    if k & 1 == 0:
        for _ in range(k // 2):
            dp1 = [[10 ** 8 for _ in range(m)] for _ in range(n)]
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

    for row in dp:
        print(*row)


if __name__ == "__main__":
    # 示例：规模为 4 的测试
    main(4)