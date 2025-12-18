import os, sys
from io import BytesIO, IOBase


def bit_count(x):
    ans = 0
    while x:
        x &= x - 1
        ans += 1
    return ans


def main():
    n = input().strip()
    x = len(n)
    k = int(input())
    if n == '1':
        print(int(k == 0))
        exit()
    if not k:
        print(1)
        exit()
    mod = 10 ** 9 + 7
    dp = [0] * (x + 1)
    dp[1] = 1
    for i in range(2, x + 1):
        dp[i] = dp[bit_count(i)] + 1
    dp1 = [[0] * (x + 1) for _ in range(x + 1)]
    # length ; set bits
    for i in range(x + 1):
        dp1[i][0] = 1
    for i in range(1, x + 1):
        for j in range(1, i + 1):
            dp1[i][j] = (dp1[i - 1][j - 1] + dp1[i - 1][j]) % mod
    ans = 0
    cou = n.count('1')
    for i in range(1, x + 1):
        if dp[i] != k:
            continue
        se = i
        for j in range(x):
            if n[j] == '0':
                continue
            ans = (ans + dp1[x - 1 - j][se] - (se == 1 and k == 1)) % mod
            se -= 1
            if se < 0:
                break
        if cou == i:
            ans = (ans + 1) % mod
    print(ans)
main()