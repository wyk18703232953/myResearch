def pre(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


def prod(a):
    ans = 1
    for each in a:
        ans = ans * each
    return ans


def lcm(a, b):
    from math import gcd
    return a * b // gcd(a, b)


def binary(x, length=16):
    y = bin(x)[2:]
    return y if len(y) >= length else "0" * (length - len(y)) + y


def solve_one(r, g, b, rr, gg, bb):
    dp = [[[0] * (b + 1) for _ in range(g + 1)] for __ in range(r + 1)]
    def f(a):
        return sorted(a, reverse=True)
    rr, gg, bb = f(rr), f(gg), f(bb)
    ans = 0
    r1 = r + 1
    g1 = g + 1
    b1 = b + 1
    for i in range(r1):
        for j in range(g1):
            for k in range(b1):
                if i + 1 <= r and j + 1 <= g:
                    val = dp[i][j][k] + rr[i] * gg[j]
                    if val > dp[i + 1][j + 1][k]:
                        dp[i + 1][j + 1][k] = val
                if j + 1 <= g and k + 1 <= b:
                    val = dp[i][j][k] + gg[j] * bb[k]
                    if val > dp[i][j + 1][k + 1]:
                        dp[i][j + 1][k + 1] = val
                if i + 1 <= r and k + 1 <= b:
                    val = dp[i][j][k] + rr[i] * bb[k]
                    if val > dp[i + 1][j][k + 1]:
                        dp[i + 1][j][k + 1] = val
                if dp[i][j][k] > ans:
                    ans = dp[i][j][k]
    return ans


def main(n):
    if n <= 0:
        return
    T = 1
    results = []
    for t in range(T):
        r = max(1, n)
        g = max(1, n * 2 // 3 if n >= 2 else 1)
        b = max(1, n // 2 if n >= 2 else 1)
        rr = [i + 1 for i in range(r)]
        gg = [2 * i + 1 for i in range(g)]
        bb = [3 * i + 2 for i in range(b)]
        res = solve_one(r, g, b, rr, gg, bb)
        results.append(res)
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    main(3)