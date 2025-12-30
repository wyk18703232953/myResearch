import random

def main(n: int):
    # 可以根据需要调整 m 和 k 的生成方式
    m = n                      # 这里简单设为与 n 相同的列数
    k = 2 * n                  # 设为偶数，保证有解（原题 k 为步数）

    # 生成测试数据：lr 为 n 行 m-1 列，ud 为 n-1 行 m 列
    # 边权取值范围可根据需求调整
    max_w = 10
    lr = [[random.randint(1, max_w) for _ in range(m - 1)] for _ in range(n)]
    ud = [[random.randint(1, max_w) for _ in range(m)] for _ in range(n - 1)]

    if k % 2:
        arr = [-1] * m
        for _ in range(n):
            print(*arr)
        return

    kk = k // 2
    INF = 10**10
    dp = [[[INF] * (kk + 1) for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            dp[i][j][0] = 0

    for z in range(1, kk + 1):
        for i in range(n):
            for j in range(m):
                if i > 0:
                    dp[i][j][z] = min(dp[i][j][z], dp[i - 1][j][z - 1] + ud[i - 1][j])
                if i < n - 1:
                    dp[i][j][z] = min(dp[i][j][z], dp[i + 1][j][z - 1] + ud[i][j])
                if j > 0:
                    dp[i][j][z] = min(dp[i][j][z], dp[i][j - 1][z - 1] + lr[i][j - 1])
                if j < m - 1:
                    dp[i][j][z] = min(dp[i][j][z], dp[i][j + 1][z - 1] + lr[i][j])

    ans = [[dp[i][j][kk] * 2 for j in range(m)] for i in range(n)]
    for i in range(n):
        print(*ans[i])


# 示例调用
if __name__ == "__main__":
    main(4)