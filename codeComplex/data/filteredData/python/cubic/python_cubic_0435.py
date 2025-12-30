import random

def main(n):
    # 生成规模参数
    # n: 行数
    m = n                # 列数，简单设为 n
    # k 必须为偶数才有意义，这里设为不大于 2n 的最大偶数
    k = max(2, (2 * n) if (2 * n) % 2 == 0 else (2 * n - 1))

    # 生成测试数据：y_axis 为 n x m，x_axis 为 (n-1) x m
    # 边权设为 1~10 之间的随机正整数
    rand = random.randint
    y_axis = [[rand(1, 10) for _ in range(m)] for _ in range(n)]
    if n > 1:
        x_axis = [[rand(1, 10) for _ in range(m)] for _ in range(n - 1)]
    else:
        # 当 n == 1 时，原代码仍用到 x_axis[i][j] 和 x_axis[i-1][j]，
        # 这里用一行来兼容索引，值同样随机生成
        x_axis = [[rand(1, 10) for _ in range(m)]]

    # 原始算法逻辑
    if k % 2 == 1:
        for _ in range(n):
            print(" ".join(["-1"] * m))
        return

    inf = 10 ** 9
    # dp[x][y][z] : 从 (x,y) 走 z 步（z 总为偶数），回到原点的最小代价
    dp = [[[inf for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]

    # 初始化 z = 2 时的最优值
    for i in range(n):
        for j in range(m):
            # 垂直方向
            if i > 0:
                if i < n - 1:
                    dp[i][j][2] = min(dp[i][j][2],
                                      2 * x_axis[i][j],
                                      2 * x_axis[i - 1][j])
                else:
                    dp[i][j][2] = min(dp[i][j][2],
                                      2 * x_axis[i - 1][j])
            else:
                dp[i][j][2] = min(dp[i][j][2],
                                  2 * x_axis[i][j])
            # 水平方向
            if j > 0:
                if j < m - 1:
                    dp[i][j][2] = min(dp[i][j][2],
                                      2 * y_axis[i][j],
                                      2 * y_axis[i][j - 1])
                else:
                    dp[i][j][2] = min(dp[i][j][2],
                                      2 * y_axis[i][j - 1])
            else:
                dp[i][j][2] = min(dp[i][j][2],
                                  2 * y_axis[i][j])

    # 递推 z = 4..k, step=2
    for z in range(4, k + 1, 2):
        for i in range(n):
            for j in range(m):
                # 上下方向
                if i > 0:
                    if i < n - 1:
                        dp[i][j][z] = min(
                            dp[i][j][z],
                            dp[i - 1][j][z - 2] + 2 * x_axis[i - 1][j],
                            dp[i + 1][j][z - 2] + 2 * x_axis[i][j],
                        )
                    else:
                        dp[i][j][z] = min(
                            dp[i][j][z],
                            dp[i - 1][j][z - 2] + 2 * x_axis[i - 1][j],
                        )
                else:
                    dp[i][j][z] = min(
                        dp[i][j][z],
                        dp[i + 1][j][z - 2] + 2 * x_axis[i][j],
                    )

                # 左右方向
                if j > 0:
                    if j < m - 1:
                        dp[i][j][z] = min(
                            dp[i][j][z],
                            dp[i][j - 1][z - 2] + 2 * y_axis[i][j - 1],
                            dp[i][j + 1][z - 2] + 2 * y_axis[i][j],
                        )
                    else:
                        dp[i][j][z] = min(
                            dp[i][j][z],
                            dp[i][j - 1][z - 2] + 2 * y_axis[i][j - 1],
                        )
                else:
                    dp[i][j][z] = min(
                        dp[i][j][z],
                        dp[i][j + 1][z - 2] + 2 * y_axis[i][j],
                    )

    # 输出结果矩阵：每个格子走 k 步回到原点的最小代价（或 -1）
    for i in range(n):
        row = []
        for j in range(m):
            row.append(str(-1 if dp[i][j][k] == inf else dp[i][j][k]))
        print(" ".join(row))


if __name__ == "__main__":
    # 示例：可以在此处修改 n 进行测试
    main(3)