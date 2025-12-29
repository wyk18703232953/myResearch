import random

def solve(rn, gn, bn, r, g, b):
    r = sorted(r, reverse=True)
    g = sorted(g, reverse=True)
    b = sorted(b, reverse=True)

    dp = [[[0 for _ in range(bn + 1)] for _ in range(gn + 1)] for _ in range(rn + 1)]

    ans = 0
    for i in range(rn + 1):
        for j in range(gn + 1):
            for k in range(bn + 1):
                if i < rn and j < gn:
                    dp[i + 1][j + 1][k] = max(dp[i + 1][j + 1][k],
                                              dp[i][j][k] + r[i] * g[j])
                if i < rn and k < bn:
                    dp[i + 1][j][k + 1] = max(dp[i + 1][j][k + 1],
                                              dp[i][j][k] + r[i] * b[k])
                if j < gn and k < bn:
                    dp[i][j + 1][k + 1] = max(dp[i][j + 1][k + 1],
                                              dp[i][j][k] + g[j] * b[k])

                ans = max(ans, dp[i][j][k])

    print(ans)


def main(n):
    # 根据规模 n 生成测试数据
    # 这里令 rn, gn, bn 与 n 相等，你也可以按需调整比例
    rn = n
    gn = n
    bn = n

    # 随机生成正整数数据，可按需求修改范围
    r = [random.randint(1, 1000) for _ in range(rn)]
    g = [random.randint(1, 1000) for _ in range(gn)]
    b = [random.randint(1, 1000) for _ in range(bn)]

    solve(rn, gn, bn, r, g, b)


if __name__ == "__main__":
    # 示例：使用 n = 5 进行测试
    main(5)