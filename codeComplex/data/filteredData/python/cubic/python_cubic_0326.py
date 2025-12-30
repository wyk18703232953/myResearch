import random

def main(n):
    # n 为规模，这里按比例拆分为三类数量
    # 你也可以按需修改这三类的数量分配方式
    x = n
    y = max(1, n // 2)
    z = max(1, n // 3)

    # 生成测试数据：三组正整数，范围可按需调整
    a = []
    for _ in range(3):
        arr = [random.randint(1, 1000) for _ in range(x)]
        a.append(arr)
    # 但原代码中三组长度分别为 n[0], n[1], n[2]，这里分别生成
    a = []
    a.append([random.randint(1, 1000) for _ in range(x)])
    a.append([random.randint(1, 1000) for _ in range(y)])
    a.append([random.randint(1, 1000) for _ in range(z)])

    for i in range(3):
        a[i].sort(reverse=True)

    dp = [[[0 for _ in range(z + 1)] for _ in range(y + 1)] for _ in range(x + 1)]
    ans = 0

    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i < x and j < y:
                    dp[i + 1][j + 1][k] = max(dp[i + 1][j + 1][k],
                                              dp[i][j][k] + a[0][i] * a[1][j])
                if i < x and k < z:
                    dp[i + 1][j][k + 1] = max(dp[i + 1][j][k + 1],
                                              dp[i][j][k] + a[0][i] * a[2][k])
                if j < y and k < z:
                    dp[i][j + 1][k + 1] = max(dp[i][j + 1][k + 1],
                                              dp[i][j][k] + a[1][j] * a[2][k])
                ans = max(ans, dp[i][j][k])

    print(ans)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)