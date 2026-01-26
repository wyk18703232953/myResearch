import sys
from array import array
import typing as Tp


def main(n):
    # 将 n 映射为 (l, r, k)，保证确定性
    # n >= 1
    if n < 1:
        n = 1
    l = 1
    r = 10 ** (n if n < 9 else 9)
    if r < l:
        r = l
    k = (n % 10) + 1  # 1 到 10 之间
    if k > 10:
        k = 10

    valid_bits, is_valid_bits = [], [0] * 1024

    for bit in range(1024):
        if bin(bit).count('1') <= k:
            valid_bits.append(bit)
            is_valid_bits[bit] = 1

    mod = 998244353

    def solve(ub):
        dp = array('i', [0]) * 1024
        dp_cnt = array('i', [0]) * 1024
        next_dp = array('i', [0]) * 1024
        next_dp_cnt = array('i', [0]) * 1024
        boundary_dp, b_bit = 0, 0

        s = str(ub)
        length = len(s)

        for e, digit in zip(range(length - 1, -1, -1), map(int, s)):
            base = pow(10, e, mod)

            for bit in valid_bits:
                for d in range(10):
                    nextbit = bit | (1 << d)
                    if is_valid_bits[nextbit]:
                        next_dp[nextbit] = (
                            next_dp[nextbit] + dp[bit]
                            + base * d * dp_cnt[bit]
                        ) % mod

                        next_dp_cnt[nextbit] += dp_cnt[bit]
                        if next_dp_cnt[nextbit] >= mod:
                            next_dp_cnt[nextbit] -= mod

            for d in range(digit):
                nextbit = b_bit | (1 << d)
                if is_valid_bits[nextbit]:
                    next_dp[nextbit] = (
                        next_dp[nextbit] + boundary_dp + base * d
                    ) % mod
                    next_dp_cnt[nextbit] += 1
                    if next_dp_cnt[nextbit] >= mod:
                        next_dp_cnt[nextbit] -= mod

            b_bit |= (1 << digit)
            boundary_dp = (boundary_dp + base * digit) % mod

            for i in valid_bits:
                dp[i] = next_dp[i]
                dp_cnt[i] = next_dp_cnt[i]
                next_dp[i] = 0
                next_dp_cnt[i] = 0

            dp[0], dp_cnt[0] = 0, 1
            dp[1] = 0
            dp_cnt[1] = 0

        return (sum(dp) + (boundary_dp if is_valid_bits[b_bit] else 0)) % mod

    if l <= 0:
        ans = solve(r)

    else:
        ans = (solve(r) - solve(l - 1)) % mod
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：使用 n = 5 作为规模参数
    main(5)