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
            dp = [max(dp[0], dp[1]),
                  dp[0] + (n // (x + y)) + (i * x % (x + y) < n % (x + y))]
        ans = max(ans, dp[s])
    return ans

def main(n):
    # Deterministically generate x, y based on n
    x = n + 1
    y = n + 2
    # Ensure gcd(x, y) can vary with n and keeps problem meaningful
    return solve(n, x, y)

if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    print(main(10))