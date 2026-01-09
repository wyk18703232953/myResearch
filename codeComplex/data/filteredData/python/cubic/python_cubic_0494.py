def main(n):
    """
    n: 规模参数，用于生成 n x n 的网格测试数据并运行原逻辑。
       这里约定:
         - 网格大小为 n x n，即 m = n
         - 步数 k = 4（为偶数，便于触发 DP 计算逻辑）
         - r[i][j], c[i][j] 为简单的测试数据：都设为 1
    """

    # 生成测试数据
    m = n          # 方形网格
    k = 4          # 固定为一个小的偶数，便于测试和保证可行解
    r = [[1 for _ in range(m - 1)] for _ in range(n)]       # n 行，每行 m-1 条横边
    c = [[1 for _ in range(m)] for _ in range(n - 1)]       # n-1 行，每行 m 条竖边

    # 如果 k 为奇数，则按原逻辑输出 -1
    if k & 1:
        for i in range(n):
            row = ["-1"] * m
            # print(" ".join(row))
            pass
        return

    # 否则执行原 answer() 的逻辑
    INF = 10**18
    dp = [[[INF for _ in range(k // 2 + 1)] for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            dp[i][j][0] = 0

    for x in range(1, k // 2 + 1):
        for i in range(n):
            for j in range(m):
                # 上
                if i > 0:
                    dp[i][j][x] = min(dp[i][j][x], dp[i - 1][j][x - 1] + c[i - 1][j])
                # 左
                if j > 0:
                    dp[i][j][x] = min(dp[i][j][x], dp[i][j - 1][x - 1] + r[i][j - 1])
                # 下
                if i + 1 < n:
                    dp[i][j][x] = min(dp[i][j][x], dp[i + 1][j][x - 1] + c[i][j])
                # 右
                if j + 1 < m:
                    dp[i][j][x] = min(dp[i][j][x], dp[i][j + 1][x - 1] + r[i][j])

    for i in range(n):
        row = [str(2 * dp[i][j][-1]) for j in range(m)]
        # print(" ".join(row))
        pass
if __name__ == "__main__":
    # 示例: 运行规模 n=3
    main(3)