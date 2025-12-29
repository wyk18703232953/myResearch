import random

def main(n: int):
    # 这里用 n 控制三种颜色数组的规模
    # 为了简单，生成长度都为 n 的数组
    R = G = B = n

    # 生成测试数据（元素值可按需调整范围）
    r = [random.randint(1, 1000) for _ in range(R)]
    g = [random.randint(1, 1000) for _ in range(G)]
    b = [random.randint(1, 1000) for _ in range(B)]

    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)

    dp = [[[0 for _ in range(B + 1)] for _ in range(G + 1)] for _ in range(R + 1)]
    ans = 0

    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                if i < R and j < G:
                    dp[i + 1][j + 1][k] = max(
                        dp[i + 1][j + 1][k],
                        r[i] * g[j] + dp[i][j][k]
                    )
                if i < R and k < B:
                    dp[i + 1][j][k + 1] = max(
                        dp[i + 1][j][k + 1],
                        r[i] * b[k] + dp[i][j][k]
                    )
                if k < B and j < G:
                    dp[i][j + 1][k + 1] = max(
                        dp[i][j + 1][k + 1],
                        b[k] * g[j] + dp[i][j][k]
                    )
                ans = max(ans, dp[i][j][k])

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(3)