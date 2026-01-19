from math import gcd

def solve(n, x, y):
    g = gcd(x, y)
    if g != 1:
        return solve(n // g + 1, x // g, y // g) * (n % g) + solve(n // g, x // g, y // g) * (g - n % g)
    ans = 0
    for s in [0, 1]:
        dp = [-n, -n]
        dp[s] = 0
        for i in range(x + y):
            dp = [max(dp[0], dp[1]), dp[0] + (n // (x + y)) + (i * x % (x + y) < n % (x + y))]
        ans = max(ans, dp[s])
    return ans

def main(n):
    # 将 n 解释为输入规模：同时生成依赖于 n 的 (N, X, Y)
    # 保证 x,y 为正整数，且与 n 有一定关系，便于规模化实验
    if n <= 0:
        N = 1
    else:
        N = n

    x = N + 1          # 随规模线性增长
    y = 2 * N + 1      # 与 x 同阶但不同系数

    result = solve(N, x, y)
    print(result)

if __name__ == "__main__":
    main(10)