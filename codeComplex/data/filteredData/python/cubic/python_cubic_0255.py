import random

def main(n):
    # 生成规模：r, g, b 总和约为 n，且都至少为 1
    if n < 3:
        n = 3
    r = random.randint(1, n - 2)
    g = random.randint(1, n - r - 1)
    b = n - r - g

    # 生成测试数据：随机正整数
    s1 = [random.randint(1, 100) for _ in range(r)]
    s2 = [random.randint(1, 100) for _ in range(g)]
    s3 = [random.randint(1, 100) for _ in range(b)]

    # 按原逻辑排序并反转
    s1.sort()
    s2.sort()
    s3.sort()
    s1 = s1[::-1]
    s2 = s2[::-1]
    s3 = s3[::-1]
    s1 = [0] + s1
    s2 = [0] + s2
    s3 = [0] + s3

    # 初始化三维 DP 数组
    dp = [[[0] * (b + 5) for _ in range(g + 5)] for _ in range(r + 5)]

    for i in range(0, r + 1):
        for j in range(0, g + 1):
            for k in range(0, b + 1):
                t1 = t2 = t3 = t4 = t5 = t6 = 0
                if i - 1 >= 0 and j - 1 >= 0:
                    t1 = dp[i - 1][j - 1][k] + (s1[i] * s2[j])
                if i - 1 >= 0 and k - 1 >= 0:
                    t2 = dp[i - 1][j][k - 1] + (s1[i] * s3[k])
                if k - 1 >= 0 and j - 1 >= 0:
                    t3 = dp[i][j - 1][k - 1] + (s2[j] * s3[k])
                if i - 1 >= 0:
                    t4 = dp[i - 1][j][k]
                if j - 1 >= 0:
                    t5 = dp[i][j - 1][k]
                if k - 1 >= 0:
                    t6 = dp[i][j][k - 1]

                dp[i][j][k] = max(t1, t2, t3, t4, t5, t6)

    print(dp[r][g][b])


if __name__ == "__main__":
    # 示例：调用 main，n 为规模参数
    main(10)