import math
import random

def solve(n, x, y):
    g = math.gcd(x, y)
    if g != 1:
        return solve(n // g + 1, x // g, y // g) * (n % g) + solve(n // g, x // g, y // g) * (g - n % g)
    p = x + y
    weights = [n // p] * p
    for i in range(p):
        if (i * x) % p < n % p:
            weights[i] += 1
    ans = -n
    for i in range(2):
        dp = [-n, -n]
        dp[i] = 0
        for w in weights:
            dp = [max(dp[0], dp[1]), dp[0] + w]
        ans = max(ans, dp[i])
    return ans

def main(n):
    # 根据规模 n 生成测试数据：
    # 约束：x, y 为正整数，且 gcd(x, y) 随机，不强制为 1。
    # 为避免 x + y 过大（使数组过大），让 x, y 与 n 同阶。
    if n <= 0:
        raise ValueError("n must be positive")

    # 随机生成 x, y，使得 1 <= x, y <= n
    x = random.randint(1, n)
    y = random.randint(1, n)

    # 确保 x + y 不为 0（由范围保证），并调用算法
    result = solve(n, x, y)
    print(n, x, y, result)

if __name__ == "__main__":
    # 示例调用：可根据需要修改规模
    main(10**5)