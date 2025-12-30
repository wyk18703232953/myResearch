import random

def main(n):
    # 1. 生成测试数据：随机生成 r, g, b，约在 [1, n]
    r = random.randint(1, n)
    g = random.randint(1, n)
    b = random.randint(1, n)

    # 2. 生成三个长度分别为 r, g, b 的随机数组
    # 元素值范围可以根据需要调整，这里取 [1, 100]
    l1 = [random.randint(1, 100) for _ in range(r)]
    l2 = [random.randint(1, 100) for _ in range(g)]
    l3 = [random.randint(1, 100) for _ in range(b)]

    l1.sort(reverse=True)
    l2.sort(reverse=True)
    l3.sort(reverse=True)

    # dp[i][j][k]：在使用了前 i 个红色、前 j 个绿色、前 k 个蓝色的情况下的最大值
    dp = [[[0 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]
    ans = 0

    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                # 跳过 (0,0,0) 的初始状态
                if i == 0 and j == 0 and k == 0:
                    continue

                best = dp[i][j][k]

                if i > 0 and j > 0:
                    best = max(best, dp[i - 1][j - 1][k] + l1[i - 1] * l2[j - 1])
                if i > 0 and k > 0:
                    best = max(best, dp[i - 1][j][k - 1] + l1[i - 1] * l3[k - 1])
                if j > 0 and k > 0:
                    best = max(best, dp[i][j - 1][k - 1] + l2[j - 1] * l3[k - 1])

                dp[i][j][k] = best
                ans = max(ans, best)

    print(ans)


if __name__ == "__main__":
    # 示例：n = 5
    main(5)