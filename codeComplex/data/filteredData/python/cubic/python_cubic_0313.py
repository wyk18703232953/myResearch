from math import gcd, ceil
import random

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
    return a * b // gcd(a, b)


def binary(x, length=16):
    y = bin(x)[2:]
    return y if len(y) >= length else "0" * (length - len(y)) + y


def main(n):
    # n 为规模，这里用 n 控制每个颜色数组的最大长度
    # 生成 r, g, b 长度（1 ~ n）
    r = random.randint(1, n)
    g = random.randint(1, n)
    b = random.randint(1, n)

    # 生成 rr, gg, bb 数组，元素范围可根据需要调整
    rr = [random.randint(1, 1000) for _ in range(r)]
    gg = [random.randint(1, 1000) for _ in range(g)]
    bb = [random.randint(1, 1000) for _ in range(b)]

    dp = [[[0] * (b + 1) for __ in range(g + 1)] for ___ in range(r + 1)]

    def f(a):
        return sorted(a, reverse=True)

    rr, gg, bb = f(rr), f(gg), f(bb)
    ans = 0
    r += 1
    g += 1
    b += 1
    for i in range(r):
        for j in range(g):
            for k in range(b):
                try:
                    dp[i + 1][j + 1][k] = max(dp[i + 1][j + 1][k],
                                              dp[i][j][k] + rr[i] * gg[j])
                except IndexError:
                    pass
                try:
                    dp[i][j + 1][k + 1] = max(dp[i][j + 1][k + 1],
                                              dp[i][j][k] + gg[j] * bb[k])
                except IndexError:
                    pass
                try:
                    dp[i + 1][j][k + 1] = max(dp[i + 1][j][k + 1],
                                              dp[i][j][k] + rr[i] * bb[k])
                except IndexError:
                    pass
                ans = max(ans, dp[i][j][k])
    print(ans)


if __name__ == "__main__":
    # 可以在这里指定规模 n
    main(5)