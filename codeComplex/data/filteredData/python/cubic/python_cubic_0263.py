import random

def main(n):
    # 规模 n：三种颜色的数量均为 n，且不超过 200
    R = G = B = min(n, 200)

    # 生成测试数据：随机正整数
    # 可根据需要调整数值范围
    r = [random.randint(1, 1000) for _ in range(R)]
    g = [random.randint(1, 1000) for _ in range(G)]
    b = [random.randint(1, 1000) for _ in range(B)]

    r.sort()
    g.sort()
    b.sort()

    # dp 的索引最多到 R,G,B，原代码固定为 202
    max_size = 202
    dp = [[[0] * max_size for _ in range(max_size)] for _ in range(max_size)]

    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                if i and j:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i - 1][j - 1][k] + r[i - 1] * g[j - 1]
                    )
                if i and k:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i - 1][j][k - 1] + r[i - 1] * b[k - 1]
                    )
                if j and k:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i][j - 1][k - 1] + g[j - 1] * b[k - 1]
                    )

    ans = 0
    for i in dp:
        for j in i:
            ans = max(ans, max(j))

    print(ans)


if __name__ == "__main__":
    # 示例：规模 10
    main(10)