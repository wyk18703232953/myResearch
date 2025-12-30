import random

def main(n):
    # 生成测试数据
    # m: 列大小（至少 1），k: 惩罚参数
    m = max(1, n // 3)          # 可按需要调整生成策略
    k = max(1, n // 5)

    # 生成数组 a，长度为 n
    a = [random.randint(-10, 10) for _ in range(n)]

    # 原逻辑开始
    dp = [[float('-inf')] * m for _ in range(n)]
    dp[0][0] = a[0]

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i - 1][j - 1] + a[i]
        dp[i][0] = max(dp[i - 1][m - 1] - k, 0) + a[i]

    ans = max(max(row) for row in dp)
    ans = max(ans - k, 0)
    print(ans)

# 简单自测
if __name__ == "__main__":
    main(10)