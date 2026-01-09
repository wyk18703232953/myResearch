#!/usr/bin/env python

def main(n):
    MOD = 10 ** 9 + 7

    factorial = [1]
    for i in range(2, n + 1):
        factorial.append(factorial[-1] * i % MOD)
    for i in range(len(factorial)):
        factorial[i] = pow(factorial[i], MOD - 2, MOD)
    DP = []
    for i in range(n):
        DP.append([0] * n)
    for i in range(n):
        DP[i][0] = pow(2, i, MOD) * factorial[i]
        for j in range(1, i // 2 + 1):
            for k in range(0, i - 1):
                DP[i][j] += DP[k][j - 1] * pow(2, i - k - 2, MOD) * factorial[i - k - 2]
            DP[i][j] %= MOD
    ans = 0
    for i in range(len(factorial)):
        factorial[i] = pow(factorial[i], MOD - 2, MOD)
    for i in range(n):
        ans += DP[n - 1][i] * factorial[n - i - 1]
    # print(ans % MOD)
    pass
if __name__ == "__main__":
    main(10)