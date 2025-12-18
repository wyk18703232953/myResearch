import sys
from array import array  # noqa: F401
import typing as Tp  # noqa: F401


def input():
    return sys.stdin.buffer.readline().decode('utf-8')


def main():
    l, r, k = map(int, input().split())

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

        for e, digit in zip(range(len(str(ub)) - 1, -1, -1), map(int, str(ub))):
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

            b_bit |= (1 << digit)
            boundary_dp = (boundary_dp + base * digit) % mod

            for i in valid_bits:
                dp[i] = next_dp[i]
                dp_cnt[i] = next_dp_cnt[i]
                next_dp[i] = next_dp_cnt[i] = 0

            dp[0], dp_cnt[0] = 0, 1
            dp[1] = dp_cnt[1] = 0

        return (sum(dp) + (boundary_dp if is_valid_bits[b_bit] else 0)) % mod

    # print(solve(r), solve(l - 1))
    print((solve(r) - solve(l - 1)) % mod)


if __name__ == '__main__':
    main()
