import random

def main(n: int) -> int:
    mod = 998244353

    # 3. 生成测试数据：生成 n 个在 1..10^9 之间的随机整数
    a = [random.randint(1, 10**9) for _ in range(n)]

    a.sort()
    dp = [1] + [0] * n
    for i in range(1, n + 1):
        x, pt = 1, i - 2
        while pt >= 0 and 2 * a[pt] > a[i - 1]:
            x = x * (n - pt - 2) % mod
            pt -= 1
        dp[i] = (dp[i - 1] * (n - i) + dp[pt + 1] * x) % mod

    # 原程序是 print(dp[-1])，这里返回结果
    return dp[-1]


if __name__ == "__main__":
    # 示例：调用 main(5)，实际使用时可根据需要自行调用 main(n)
    result = main(5)
    print(result)