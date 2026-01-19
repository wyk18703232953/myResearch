import sys
from array import array  # noqa: F401


def main(n):
    mod = 998244353
    k = n // 2
    if k < 0:
        k = 0
    if k > 2 * n + 2:
        k = 2 * n + 2

    dp = [[[0] * (2 * n + 3) for _ in range(n)] for _ in range(4)]
    dp[0][0][1] = 1
    dp[3][0][1] = 1
    if 2 < 2 * n + 3:
        dp[1][0][2] = 1
        dp[2][0][2] = 1

    for i in range(n - 1):
        for j in range(k + 1):
            for sbit in range(4):
                v = dp[sbit][i][j]
                if v == 0:
                    continue
                for tbit in range(4):
                    add = (
                        1 if (sbit == 3 and tbit == 0) or (sbit == 0 and tbit == 3) else
                        (1 if (sbit & 2) != (tbit & 2) and (tbit == 1 or tbit == 2) else 0)
                        + (1 if (sbit & 1) != (tbit & 1) and (tbit == 1 or tbit == 2) else 0)
                    )
                    idx = j + add
                    if idx >= 2 * n + 3:
                        continue
                    nv = dp[tbit][i + 1][idx] + v
                    if nv >= mod:
                        nv -= mod
                    dp[tbit][i + 1][idx] = nv

    if k >= 2 * n + 3:
        ans = 0
    else:
        ans = sum(dp[bit][n - 1][k] for bit in range(4)) % mod
    print(ans)


if __name__ == "__main__":
    main(10)