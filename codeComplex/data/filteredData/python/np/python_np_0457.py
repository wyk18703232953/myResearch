import math

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
    # 由规模 n 决定原始输入 (N, X, Y)
    # 映射方式：N = n，X = n // 2 + 1，Y = n // 3 + 1，保证 X,Y >= 1 且随 n 线性增长
    N = n
    X = n // 2 + 1
    Y = n // 3 + 1
    result = solve(N, X, Y)
    print(result)

if __name__ == "__main__":
    # 示例：使用 n = 10 作为规模
    main(10)