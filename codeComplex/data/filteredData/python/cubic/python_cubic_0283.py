import random

def main(n: int):
    # 生成规模：r, g, b 总体规模为 n，尽量均匀分配
    r = n // 3
    g = (n - r) // 2
    b = n - r - g

    # 生成测试数据：随机整数（可以根据需要调整范围）
    # 保持与原题语义一致，三个颜色各自有一组数字
    a = [[], [], []]
    a[0] = sorted(random.randint(1, 1000) for _ in range(r))
    a[1] = sorted(random.randint(1, 1000) for _ in range(g))
    a[2] = sorted(random.randint(1, 1000) for _ in range(b))

    # 动态规划
    dp = [[[0 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]
    odp = 0
    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                if i < r and j < g:
                    dp[i + 1][j + 1][k] = max(
                        dp[i + 1][j + 1][k],
                        dp[i][j][k] + a[0][i] * a[1][j]
                    )
                if i < r and k < b:
                    dp[i + 1][j][k + 1] = max(
                        dp[i + 1][j][k + 1],
                        dp[i][j][k] + a[0][i] * a[2][k]
                    )
                if j < g and k < b:
                    dp[i][j + 1][k + 1] = max(
                        dp[i][j + 1][k + 1],
                        dp[i][j][k] + a[1][j] * a[2][k]
                    )
                odp = max(odp, dp[i][j][k])

    print(odp)


# 示例：当作为脚本运行时，用某个默认规模测试
if __name__ == "__main__":
    main(9)