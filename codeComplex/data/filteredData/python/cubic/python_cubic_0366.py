#!/usr/bin/env python
import random


def main(n: int):
    # 1. 生成测试数据：根据规模 n 生成一个模数 MOD
    # 要求 MOD > n 且为奇数（保证存在逆元），这里随机取 [10^9+7, 10^9+7 + 2n] 区间内的奇数
    base_mod = 10 ** 9 + 7
    MOD = base_mod + 2 * n + 1  # 一定是奇数且 > 10^9+7

    # 2. 原逻辑开始（去掉 input，使用 n 和 MOD）

    factorial = [1]
    for i in range(2, n + 1):
        factorial.append(factorial[-1] * i % MOD)

    # factorial[i] <- (i!)^{-1} mod MOD
    for i in range(len(factorial)):
        factorial[i] = pow(factorial[i], MOD - 2, MOD)

    # DP 初始化
    DP = [[0] * n for _ in range(n)]

    for i in range(n):
        DP[i][0] = pow(2, i, MOD) * factorial[i] % MOD
        for j in range(1, i // 2 + 1):
            cur = 0
            for k in range(0, i - 1):
                cur += (
                    DP[k][j - 1]
                    * pow(2, i - k - 2, MOD)
                    * factorial[i - k - 2]
                )
            DP[i][j] = cur % MOD

    ans = 0

    # 把 factorial[i] 还原为 i! （因为上面存的是逆元）
    # 注意：原代码是做了两次 pow(inv_fact, MOD-2, MOD)，
    # 对于合法 MOD（质数或与 i! 互素的模数）相当于还原回 i!
    for i in range(len(factorial)):
        factorial[i] = pow(factorial[i], MOD - 2, MOD)

    for i in range(n):
        ans += DP[n - 1][i] * factorial[n - i - 1]
    ans %= MOD

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)