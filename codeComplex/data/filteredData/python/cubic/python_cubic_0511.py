import random

def main(n):
    # 可根据需要修改 m、k 的生成方式
    m = n
    # 令 k 为随机的偶数步数（避免原程序中 k 为奇数时全输出 -1 的情形）
    k = 2 * random.randint(1, max(1, n))

    # 生成测试数据：yw, xw 对应原程序
    # yw: n 行，每行 m-1 个权值（左右边权）
    # xw: n-1 行，每行 m 个权值（上下边权）
    max_weight = 10  # 最大边权，可调整
    yw = [[random.randint(1, max_weight) for _ in range(m - 1)] for _ in range(n)]
    xw = [[random.randint(1, max_weight) for _ in range(m)] for _ in range(n - 1)]

    # 如果 k 为奇数，按原逻辑输出 -1
    if k % 2 == 1:
        for _ in range(n):
            print(" ".join(["-1"] * m))
        return

    inf = 10 ** 10
    steps = k // 2

    # dp[step][i][j]: 从 (i,j) 出发走 step 条边的最小总权值
    dp = [[[inf for _ in range(m)] for _ in range(n)] for _ in range(steps + 1)]

    for i in range(n):
        for j in range(m):
            dp[0][i][j] = 0

    for step in range(1, steps + 1):
        for i in range(n):
            for j in range(m):
                if i > 0:
                    dp[step][i][j] = min(dp[step][i][j],
                                         dp[step - 1][i - 1][j] + xw[i - 1][j])
                if i < n - 1:
                    dp[step][i][j] = min(dp[step][i][j],
                                         dp[step - 1][i + 1][j] + xw[i][j])
                if j > 0:
                    dp[step][i][j] = min(dp[step][i][j],
                                         dp[step - 1][i][j - 1] + yw[i][j - 1])
                if j < m - 1:
                    dp[step][i][j] = min(dp[step][i][j],
                                         dp[step - 1][i][j + 1] + yw[i][j])

    # 输出 2 * dp[steps][i][j]，与原代码保持一致
    for row in dp[-1]:
        print(" ".join(str(2 * val) for val in row))


if __name__ == "__main__":
    # 示例：运行 main(4)
    main(4)