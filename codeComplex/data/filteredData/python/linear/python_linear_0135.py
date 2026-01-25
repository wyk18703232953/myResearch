import os, sys
from io import BytesIO, IOBase


def bit_count(x):
    ans = 0
    while x:
        x &= x - 1
        ans += 1
    return ans


def core(n_str, k):
    x = len(n_str)
    if n_str == '1':
        return int(k == 0)
    if not k:
        return 1
    mod = 10 ** 9 + 7
    dp = [0] * (x + 1)
    dp[1] = 1
    for i in range(2, x + 1):
        dp[i] = dp[bit_count(i)] + 1
    dp1 = [[0] * (x + 1) for _ in range(x + 1)]
    for i in range(x + 1):
        dp1[i][0] = 1
    for i in range(1, x + 1):
        for j in range(1, i + 1):
            dp1[i][j] = (dp1[i - 1][j - 1] + dp1[i - 1][j]) % mod
    ans = 0
    cou = n_str.count('1')
    for i in range(1, x + 1):
        if dp[i] != k:
            continue
        se = i
        for j in range(x):
            if n_str[j] == '0':
                continue
            ans = (ans + dp1[x - 1 - j][se] - (se == 1 and k == 1)) % mod
            se -= 1
            if se < 0:
                break
        if cou == i:
            ans = (ans + 1) % mod
    return ans


def generate_input(n):
    if n <= 0:
        n = 1
    # n_str: binary string of length n with a simple deterministic pattern
    # pattern: first bit '1', then bits determined by (i % 3)
    bits = []
    for i in range(n):
        if i == 0:
            bits.append('1')
        else:
            bits.append('1' if i % 3 != 0 else '0')
    n_str = ''.join(bits)
    # k: derived deterministically from n, but small relative to n
    # ensure k is non-negative and not too large
    if n == 1:
        k = 0
    else:
        k = (n % 5) + 1
    return n_str, k


def main(n):
    n_str, k = generate_input(n)
    ans = core(n_str, k)
    print(ans)


if __name__ == "__main__":
    # example: run with n = 10
    main(10)