import random

def main(n: int):
    # 生成规模为 n 的测试数据
    # r, g, b 的值之和与 n 同数量级，这里简单设置为 n, n, n
    r = n
    g = n
    b = n

    # 生成随机数组，元素值在 1~1000 之间
    rr = sorted(random.randint(1, 1000) for _ in range(r))
    gg = sorted(random.randint(1, 1000) for _ in range(g))
    bb = sorted(random.randint(1, 1000) for _ in range(b))

    # 原逻辑
    dp = [[[0] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]
    res = 0
    for i in range(r, -1, -1):
        for j in range(g, -1, -1):
            for k in range(b, -1, -1):
                if i > 0 and j > 0:
                    dp[i - 1][j - 1][k] = max(
                        dp[i - 1][j - 1][k],
                        dp[i][j][k] + rr[i - 1] * gg[j - 1]
                    )
                if i > 0 and k > 0:
                    dp[i - 1][j][k - 1] = max(
                        dp[i - 1][j][k - 1],
                        dp[i][j][k] + rr[i - 1] * bb[k - 1]
                    )
                if j > 0 and k > 0:
                    dp[i][j - 1][k - 1] = max(
                        dp[i][j - 1][k - 1],
                        dp[i][j][k] + gg[j - 1] * bb[k - 1]
                    )
                if i > 0 and j > 0 and k > 0:
                    res = max(res,
                              dp[i - 1][j - 1][k],
                              dp[i - 1][j][k - 1],
                              dp[i][j - 1][k - 1])
    print(res)


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n
    main(3)