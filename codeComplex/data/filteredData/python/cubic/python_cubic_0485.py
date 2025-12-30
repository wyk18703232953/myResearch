import math
import random


def main(n: int):
    # 这里将 m 与 n 相同；也可以按需修改为其他函数关系
    m = n

    # 随机生成 kk（偶数更有意义，否则全为 -1）
    # 生成范围 [2, 2*(n+m)]，保证不会太大
    kk = random.randint(1, 2 * (n + m))

    # 生成测试数据：right 为 n 行 m-1 或 m 列的边权
    # 原代码假设：
    #   right[i][j]  存在于 (i, j) -> (i, j+1) 的边（j <= m-2）
    #   down[i][j]   存在于 (i, j) -> (i+1, j) 的边（i <= n-2）
    # 但原输入是 n 行 m 列 right 和 n-1 行 m 列 down，全填充。
    # 我们保持相同规模：right: n x m, down: (n-1) x m

    max_w = 10  # 边权最大值
    right = [[random.randint(1, max_w) for _ in range(m)] for _ in range(n)]
    down = [[random.randint(1, max_w) for _ in range(m)] for _ in range(n - 1)]

    # 动态规划数组
    dp = [[math.inf] * m for _ in range(n)]
    dpCopy = [[math.inf] * m for _ in range(n)]

    # 按原逻辑进行 kk//2 轮更新
    for step in range(1, (kk // 2) + 1):
        for j in range(n):
            for k in range(m):
                if step == 1:
                    if j == 0:
                        if k == 0:
                            dp[j][k] = min(dp[j][k], down[j][k], right[j][k])
                        elif k == m - 1:
                            dp[j][k] = min(dp[j][k], right[j][k - 1], down[j][k])
                        else:
                            dp[j][k] = min(dp[j][k],
                                           right[j][k - 1], right[j][k],
                                           down[j][k])
                    elif j == n - 1:
                        if k == 0:
                            dp[j][k] = min(dp[j][k], down[j - 1][k], right[j][k])
                        elif k == m - 1:
                            dp[j][k] = min(dp[j][k], right[j][k - 1], down[j - 1][k])
                        else:
                            dp[j][k] = min(dp[j][k],
                                           right[j][k - 1], right[j][k],
                                           down[j - 1][k])
                    elif k == 0:
                        dp[j][k] = min(dp[j][k],
                                       right[j][k],
                                       down[j - 1][k], down[j][k])
                    elif k == m - 1:
                        dp[j][k] = min(dp[j][k],
                                       right[j][k - 1],
                                       down[j - 1][k], down[j][k])
                    else:
                        dp[j][k] = min(dp[j][k],
                                       right[j][k - 1], right[j][k],
                                       down[j - 1][k], down[j][k])
                    continue

                # step >= 2
                if j == 0:
                    if k == 0:
                        dp[j][k] = min(
                            dpCopy[j][k + 1] + right[j][k],
                            dpCopy[j + 1][k] + down[j][k]
                        )
                    elif k == m - 1:
                        dp[j][k] = min(
                            dpCopy[j][k - 1] + right[j][k - 1],
                            dpCopy[j + 1][k] + down[j][k]
                        )
                    else:
                        dp[j][k] = min(
                            dpCopy[j][k - 1] + right[j][k - 1],
                            dpCopy[j][k + 1] + right[j][k],
                            dpCopy[j + 1][k] + down[j][k]
                        )
                elif j == n - 1:
                    if k == 0:
                        dp[j][k] = min(
                            dpCopy[j - 1][k] + down[j - 1][k],
                            dpCopy[j][k + 1] + right[j][k]
                        )
                    elif k == m - 1:
                        dp[j][k] = min(
                            dpCopy[j - 1][k] + down[j - 1][k],
                            dpCopy[j][k - 1] + right[j][k - 1]
                        )
                    else:
                        dp[j][k] = min(
                            dpCopy[j - 1][k] + down[j - 1][k],
                            dpCopy[j][k - 1] + right[j][k - 1],
                            dpCopy[j][k + 1] + right[j][k]
                        )
                elif k == 0:
                    dp[j][k] = min(
                        dpCopy[j - 1][k] + down[j - 1][k],
                        dpCopy[j + 1][k] + down[j][k],
                        dpCopy[j][k + 1] + right[j][k]
                    )
                elif k == m - 1:
                    dp[j][k] = min(
                        dpCopy[j - 1][k] + down[j - 1][k],
                        dpCopy[j + 1][k] + down[j][k],
                        dpCopy[j][k - 1] + right[j][k - 1]
                    )
                else:
                    dp[j][k] = min(
                        dpCopy[j - 1][k] + down[j - 1][k],
                        dpCopy[j + 1][k] + down[j][k],
                        dpCopy[j][k - 1] + right[j][k - 1],
                        dpCopy[j][k + 1] + right[j][k]
                    )

        # 拷贝到 dpCopy
        for ii in range(n):
            for jj in range(m):
                dpCopy[ii][jj] = dp[ii][jj]

    # 输出结果
    if kk % 2 == 1:
        for i in range(n):
            print(*([-1] * m))
        return

    for i in range(n):
        row = [2 * dp[i][j] for j in range(m)]
        print(*row)


if __name__ == "__main__":
    # 示例：调用 main(n)，可根据需要修改 n
    main(4)