import random

def main(n: int):
    mod = 998244353

    # 3. 生成测试数据：a 为长度为 n 的随机整数数组
    # 可根据需要调整数据范围
    a = [random.randint(1, 10**9) for _ in range(n)]

    a.sort()
    dp = [1] + [0] * n
    for i in range(1, n + 1):
        x, pt = 1, i - 2
        while pt >= 0 and 2 * a[pt] > a[i - 1]:
            x = x * (n - pt - 2) % mod
            pt -= 1
        dp[i] = (dp[i - 1] * (n - i) + dp[pt + 1] * x) % mod

    print(dp[-1])


if __name__ == "__main__":
    # 示例：运行规模为 5 的测试
    main(5)