def prod(a, mod=10**9+7):
    ans = 1
    for each in a:
        ans = (ans * each) % mod
    return ans

def lcm(a, b):
    from math import gcd
    return a * b // gcd(a, b)

def binary(x, length=16):
    y = bin(x)[2:]
    return y if len(y) >= length else "0" * (length - len(y)) + y

def core_logic(a):
    n = len(a)
    dp = [[False]*(n+2) for _ in range(n+2)]
    dp2 = [[600]*(n+2) for _ in range(n+2)]
    for i in range(n):
        dp[i][i] = a[i]
        dp2[i][i] = 1
    for diff in range(1, n):
        for i in range(n-diff):
            for j in range(i, i+diff):
                if dp[i][j] == dp[j+1][i+diff] and dp[i][j]:
                    dp[i][i+diff] = dp[i][j] + 1
                    dp2[i][i+diff] = 1
                dp2[i][i+diff] = min(dp2[i][i+diff], dp2[i][j] + dp2[j+1][i+diff])
            if not dp2[i][i+diff]:
                dp2[i][i+diff] = min(dp2[i+1][i+diff] + 1, dp2[i][i+diff-1] + 1)
    return dp2[0][n-1]

def generate_data(n):
    if n <= 0:
        return [1]
    return [(i % 3) + 1 for i in range(n)]

def main(n):
    a = generate_data(n)
    res = core_logic(a)
    # print(res)
    pass
if __name__ == "__main__":
    main(10)