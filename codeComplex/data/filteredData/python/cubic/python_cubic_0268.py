import random

def main(n):
    # 生成规模为 n 的测试数据：
    # 为了保持与原题类似的结构，令 r, g, b 均与 n 相关
    # 这里简单设置为 r = g = b = n
    r = g = b = n

    # 生成随机的正整数序列，数值范围可以调整
    R = [random.randint(1, 1000) for _ in range(r)]
    G = [random.randint(1, 1000) for _ in range(g)]
    B = [random.randint(1, 1000) for _ in range(b)]

    # 原逻辑开始
    R.sort(reverse=True)
    G.sort(reverse=True)
    B.sort(reverse=True)

    dp = [[[0] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]

    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                if i < r and j < g:
                    dp[i + 1][j + 1][k] = max(
                        dp[i + 1][j + 1][k],
                        dp[i][j][k] + R[i] * G[j]
                    )
                if i < r and k < b:
                    dp[i + 1][j][k + 1] = max(
                        dp[i + 1][j][k + 1],
                        dp[i][j][k] + R[i] * B[k]
                    )
                if j < g and k < b:
                    dp[i][j + 1][k + 1] = max(
                        dp[i][j + 1][k + 1],
                        dp[i][j][k] + B[k] * G[j]
                    )

    ans = 0
    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                ans = max(ans, dp[i][j][k])

    return ans


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n
    n = 3
    print(main(n))