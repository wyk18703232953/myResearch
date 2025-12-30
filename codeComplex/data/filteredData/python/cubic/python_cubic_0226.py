import random

def main(n: int):
    # 根据规模 n 生成随机数据
    # 约束：r + g + b ≈ n，且每个颜色数量 >= 1
    if n < 3:
        raise ValueError("n 应该至少为 3，用于生成三种颜色的数组")

    # 将 n 划分为 r, g, b 三部分
    r = random.randint(1, n - 2)
    g = random.randint(1, n - r - 1)
    b = n - r - g

    # 生成随机值（可根据需要调整范围）
    R = [random.randint(1, 10**4) for _ in range(r)]
    G = [random.randint(1, 10**4) for _ in range(g)]
    B = [random.randint(1, 10**4) for _ in range(b)]

    R.sort(reverse=True)
    G.sort(reverse=True)
    B.sort(reverse=True)

    # 三维 DP，大小为 (r+1) x (g+1) x (b+1)
    dp = [[[0] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]

    # 自底向上填表
    for i in range(r, -1, -1):
        for j in range(g, -1, -1):
            for k in range(b, -1, -1):
                if i < r and j < g:
                    dp[i][j][k] = max(dp[i][j][k],
                                      R[i] * G[j] + dp[i + 1][j + 1][k])
                if i < r and k < b:
                    dp[i][j][k] = max(dp[i][j][k],
                                      R[i] * B[k] + dp[i + 1][j][k + 1])
                if j < g and k < b:
                    dp[i][j][k] = max(dp[i][j][k],
                                      G[j] * B[k] + dp[i][j + 1][k + 1])

    # 输出结果
    print(dp[0][0][0])


if __name__ == "__main__":
    # 示例：使用 n=9 运行一次
    main(9)