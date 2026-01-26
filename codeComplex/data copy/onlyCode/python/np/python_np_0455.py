from math import gcd
n, x, y = map(int, input().split())

def solve(n, x, y):
    g = gcd(x, y)
    if gcd(x, y) != 1:
        return solve(n // g + 1, x // g, y // g) * (n % g) + solve(n // g, x // g, y // g) * (g - n % g)
    ans = 0
    for s in [0, 1]:
        dp = [-n, -n]
        dp[s] = 0
        for i in range(x + y):
            dp = [max(dp[0], dp[1]), dp[0] + (n // (x + y)) + (i * x % (x + y) < n % (x + y))]
        ans = max(ans, dp[s])
    return ans
    
print(solve(n, x, y))