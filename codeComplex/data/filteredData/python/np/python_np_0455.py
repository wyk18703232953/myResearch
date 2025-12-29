from math import gcd
import random

def solve(n, x, y):
    g = gcd(x, y)
    if g != 1:
        return solve(n // g + 1, x // g, y // g) * (n % g) + solve(n // g, x // g, y // g) * (g - n % g)
    ans = 0
    for s in [0, 1]:
        dp = [-n, -n]
        dp[s] = 0
        for i in range(x + y):
            dp = [max(dp[0], dp[1]),
                  dp[0] + (n // (x + y)) + (i * x % (x + y) < n % (x + y))]
        ans = max(ans, dp[s])
    return ans

def main(n):
    # 根据规模 n 生成测试数据：
    # 保证 x, y 为正整数，并与 n 存在一定大小关系
    # 这里简单选取 1 <= x, y <= max(2, n)
    upper = max(2, n)
    x = random.randint(1, upper)
    y = random.randint(1, upper)
    # 避免 x 和 y 同时特别大且完全相同（非必须，仅示例）
    if x == y and x > 1:
        y = max(1, y - 1)
    return solve(n, x, y)

if __name__ == "__main__":
    # 示例运行：可修改这里的 n 进行测试
    test_n = 100
    ans = main(test_n)
    print(ans)