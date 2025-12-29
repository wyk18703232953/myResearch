from array import array
import random


def main(n: int):
    # 生成测试数据：k 在 [0, 2n] 范围内任选
    k = random.randint(0, 2 * n)

    mod = 998244353
    # dp[4][n][2n+3]
    dp = [[[0] * (2 * n + 3) for _ in range(n)] for _ in range(4)]

    dp[0][0][1] = dp[3][0][1] = 1
    dp[1][0][2] = dp[2][0][2] = 1

    for i in range(n - 1):
        for j in range(k + 1):
            for sbit in range(4):
                if dp[sbit][i][j] == 0:
                    continue
                base_val = dp[sbit][i][j]
                for tbit in range(4):
                    add = (
                        1 if (sbit == 3 and tbit == 0) or (sbit == 0 and tbit == 3) else
                        (1 if (sbit & 2) != (tbit & 2) and (tbit == 1 or tbit == 2) else 0)
                        + (1 if (sbit & 1) != (tbit & 1) and (tbit == 1 or tbit == 2) else 0)
                    )
                    nxt = j + add
                    if nxt > k:
                        continue
                    val = dp[tbit][i + 1][nxt] + base_val
                    if val >= mod:
                        val -= mod
                    dp[tbit][i + 1][nxt] = val

    ans = sum(dp[bit][n - 1][k] for bit in range(4)) % mod
    print(ans)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)