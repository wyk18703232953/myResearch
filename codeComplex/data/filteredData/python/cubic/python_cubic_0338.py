import random

def main(n: int):
    mod = 998244353

    # 1. 生成测试数据：n 个整数
    # 可按需修改生成范围
    a = [random.randint(1, 10**9) for _ in range(n)]

    # 2. 原始逻辑
    a.sort()
    dp = [1] + [0] * n
    for i in range(1, n + 1):
        x, pt = 1, i - 2
        while pt >= 0 and 2 * a[pt] > a[i - 1]:
            x = x * (n - pt - 2) % mod
            pt -= 1
        dp[i] = (dp[i - 1] * (n - i) + dp[pt + 1] * x) % mod

    # 输出结果
    print(dp[-1])


if __name__ == "__main__":
    # 示例：运行规模为 5
    main(5)