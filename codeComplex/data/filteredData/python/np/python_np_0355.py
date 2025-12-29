import random

def main(n):
    # 生成测试数据：n 行 n 列矩阵（原代码里 m 可以为任意，这里令 m = n）
    m = n
    # 为了可重复性，可以设定随机种子（如需真正随机，可去掉这一行）
    random.seed(0)
    a = [[random.randint(0, 100) for _ in range(m)] for _ in range(n)]

    # 原始逻辑开始
    x = [[a[i][j] for i in range(n)] for j in range(m)]
    x.sort(key=lambda xx: -max(xx))
    dp = [[0 for _ in range(1 << n)] for _ in range(m + 1)]

    for i in range(m):
        for prev in range(1 << n):
            for pres in range(1 << n):
                if (prev ^ pres) != (prev + pres):
                    continue

                for j in range(n):
                    ma = 0
                    for st in range(n):
                        if pres & (1 << st):
                            ma += x[i][(st + j) % n]

                    dp[i + 1][pres ^ prev] = max(dp[i + 1][pres ^ prev],
                                                 dp[i][prev] + ma)

    print(dp[m][(1 << n) - 1])


if __name__ == "__main__":
    # 示例：规模 n = 3
    main(3)