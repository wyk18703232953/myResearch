import random

def main(n: int):
    # 生成规模：三种颜色数量之和约为 n
    # 这里简单设定为尽量平均分配
    nr = n // 3
    ng = (n - nr) // 2
    nb = n - nr - ng

    # 生成测试数据：值域可以自行调整
    r = sorted(random.randint(1, 1000) for _ in range(nr))
    g = sorted(random.randint(1, 1000) for _ in range(ng))
    b = sorted(random.randint(1, 1000) for _ in range(nb))

    # DP 逻辑与原程序一致
    dp = [[[0 for _ in range(nb + 1)] for _ in range(ng + 1)] for _ in range(nr + 1)]
    for i in range(nr + 1):
        for j in range(ng + 1):
            for k in range(nb + 1):
                val = 0
                if i - 1 >= 0 and j - 1 >= 0 and i > 0 and j > 0:
                    val = max(val, r[i - 1] * g[j - 1] + dp[i - 1][j - 1][k])
                if i - 1 >= 0 and k - 1 >= 0 and i > 0 and k > 0:
                    val = max(val, r[i - 1] * b[k - 1] + dp[i - 1][j][k - 1])
                if j - 1 >= 0 and k - 1 >= 0 and j > 0 and k > 0:
                    val = max(val, g[j - 1] * b[k - 1] + dp[i][j - 1][k - 1])
                dp[i][j][k] = val

    print(dp[nr][ng][nb])


if __name__ == "__main__":
    # 示例：n = 9
    main(9)