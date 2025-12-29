import random
from array import array
import typing as Tp  # noqa: F401


def main(n: int) -> None:
    # n 用作规模参数，这里用来控制随机生成 l, r 的范围
    # 例如生成 [1, 10^n] 内的区间
    if n <= 0:
        n = 1
    max_val = 10 ** n - 1

    # 生成测试数据：l, r, k
    # 保证 0 <= k <= 10（因为十进制数字只有 0~9 共 10 个）
    l = random.randint(0, max_val)
    r = random.randint(l, max_val)
    k = random.randint(0, 10)

    valid_bits, is_valid_bits = [], [0] * 1024

    for bit in range(1024):
        if bin(bit).count("1") <= k:
            valid_bits.append(bit)
            is_valid_bits[bit] = 1

    mod = 998244353

    def solve(ub: int) -> int:
        if ub < 0:
            return 0
        dp = array("i", [0]) * 1024
        dp_cnt = array("i", [0]) * 1024
        next_dp = array("i", [0]) * 1024
        next_dp_cnt = array("i", [0]) * 1024
        boundary_dp, b_bit = 0, 0

        s = str(ub)
        for e, digit in zip(range(len(s) - 1, -1, -1), map(int, s)):
            base = pow(10, e, mod)

            for bit in valid_bits:
                val_dp = dp[bit]
                val_cnt = dp_cnt[bit]
                if val_dp == 0 and val_cnt == 0:
                    continue
                for d in range(10):
                    nextbit = bit | (1 << d)
                    if is_valid_bits[nextbit]:
                        next_dp[nextbit] = (
                            next_dp[nextbit] + val_dp + base * d * val_cnt
                        ) % mod
                        tmp_cnt = next_dp_cnt[nextbit] + val_cnt
                        if tmp_cnt >= mod:
                            tmp_cnt -= mod
                        next_dp_cnt[nextbit] = tmp_cnt

            for d in range(digit):
                nextbit = b_bit | (1 << d)
                if is_valid_bits[nextbit]:
                    next_dp[nextbit] = (
                        next_dp[nextbit] + boundary_dp + base * d
                    ) % mod
                    tmp_cnt = next_dp_cnt[nextbit] + 1
                    if tmp_cnt >= mod:
                        tmp_cnt -= mod
                    next_dp_cnt[nextbit] = tmp_cnt

            b_bit |= 1 << digit
            boundary_dp = (boundary_dp + base * digit) % mod

            for i in valid_bits:
                dp[i] = next_dp[i]
                dp_cnt[i] = next_dp_cnt[i]
                next_dp[i] = 0
                next_dp_cnt[i] = 0

            dp[0], dp_cnt[0] = 0, 1
            dp[1] = 0
            dp_cnt[1] = 0

        ans = sum(dp) % mod
        if is_valid_bits[b_bit]:
            ans = (ans + boundary_dp) % mod
        return ans

    result = (solve(r) - solve(l - 1)) % mod
    print(result)


if __name__ == "__main__":
    # 示例：用 n=3 生成规模为 10^3 的随机测试数据
    main(3)