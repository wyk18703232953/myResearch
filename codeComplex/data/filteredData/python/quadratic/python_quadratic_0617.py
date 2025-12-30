import random

def main(n):
    # 生成测试数据：n 的规模给定，m 和 k 以及数组 a 自动生成
    # 这里设置 m 在 [1, n] 范围内，k 和 a[i] 是非负整数
    if n <= 0:
        print(0)
        return

    m = random.randint(1, n)          # 区间最大长度
    k = random.randint(0, 10)         # 每段固定代价
    a = [random.randint(0, 10) for _ in range(n)]

    # 原逻辑开始
    a = [0] + a                       # 前缀和方便从 1 开始
    dp = [0] * 300005
    ans = 0
    for i in range(1, n + 1):
        a[i] += a[i - 1]
        for j in range(1, m + 1):
            if i - j >= 0:
                dp[i] = max(dp[i], a[i] - a[i - j] - k)
        if i - m >= 0:
            dp[i] = max(dp[i], a[i] - a[i - m] + dp[i - m] - k)
        ans = max(ans, dp[i])

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10) 进行一次测试
    main(10)