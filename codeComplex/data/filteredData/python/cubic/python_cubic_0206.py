import random

def main(n: int):
    # 使用 n 作为三个数组的规模（可按需修改为不同规模）
    r = g = b = n

    # 生成测试数据：1 到 1000 的随机整数
    rs = sorted(random.randint(1, 1000) for _ in range(r))
    gs = sorted(random.randint(1, 1000) for _ in range(g))
    bs = sorted(random.randint(1, 1000) for _ in range(b))

    # 三维 DP：dp[i][j][k] 表示使用前 i, j, k 个元素的最大值
    dp = [[[0] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]
    ans = 0

    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                if i > 0 and k > 0:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i - 1][j][k - 1] + rs[i - 1] * bs[k - 1]
                    )
                if i > 0 and j > 0:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i - 1][j - 1][k] + rs[i - 1] * gs[j - 1]
                    )
                if j > 0 and k > 0:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i][j - 1][k - 1] + gs[j - 1] * bs[k - 1]
                    )
                if dp[i][j][k] > ans:
                    ans = dp[i][j][k]

    print(ans)


if __name__ == "__main__":
    # 示例：n = 3
    main(3)