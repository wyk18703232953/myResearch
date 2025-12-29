import random

def main(n):
    # 根据规模 n 生成 r,g,b 的长度（1 到 n 之间）
    r = random.randint(1, n)
    g = random.randint(1, n)
    b = random.randint(1, n)

    # 生成并排序三种颜色的数组，元素取值范围可根据需要调整
    ls_r = sorted(random.randint(1, 1000) for _ in range(r))
    ls_g = sorted(random.randint(1, 1000) for _ in range(g))
    ls_b = sorted(random.randint(1, 1000) for _ in range(b))

    dp = [[[0 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]

    # 主循环
    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                if i == 0 and j == 0 and k == 0:
                    continue
                res1 = 0
                res2 = 0
                res3 = 0
                if i > 0 and j > 0:
                    res1 = dp[i - 1][j - 1][k] + ls_r[i - 1] * ls_g[j - 1]
                if i > 0 and k > 0:
                    res2 = dp[i - 1][j][k - 1] + ls_r[i - 1] * ls_b[k - 1]
                if j > 0 and k > 0:
                    res3 = dp[i][j - 1][k - 1] + ls_g[j - 1] * ls_b[k - 1]
                dp[i][j][k] = max(dp[i][j][k], res1, res2, res3)

    print(dp[r][g][b])

if __name__ == "__main__":
    # 示例调用：规模设为 5
    main(5)