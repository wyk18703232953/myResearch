import random

def main(n):
    # 生成规模为 n 的测试数据
    r = g = b = n
    # 生成 n 个 1~100 的随机整数
    s1 = [random.randint(1, 100) for _ in range(r)]
    s2 = [random.randint(1, 100) for _ in range(g)]
    s3 = [random.randint(1, 100) for _ in range(b)]

    # 以下为原逻辑
    s1.sort()
    s2.sort()
    s3.sort()
    s1 = s1[::-1]
    s2 = s2[::-1]
    s3 = s3[::-1]
    s1 = [0] + s1
    s2 = [0] + s2
    s3 = [0] + s3

    dp = []
    for i in range(r + 5):
        H = []
        for j in range(g + 5):
            h = []
            for k in range(b + 5):
                h.append(0)
            H.append(h)
        dp.append(H)

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
    # 示例：规模 n = 3
    main(3)