import math
from decimal import Decimal, ROUND_FLOOR
import random


def sum1(i: Decimal) -> Decimal:
    return i * (i + 1) / 2


def sum2(s: Decimal, e: Decimal) -> Decimal:
    # sum_{i=s}^{e} (i-1) = sum1(e) - sum1(s-1) - (e-s+1)
    return sum1(e) - sum1(s - 1) - (e - s)


def solve(n: Decimal, k: Decimal) -> int:
    if n == 1:
        return 0
    if k > n:
        return 1
    if sum2(Decimal(2), k) < n:
        return -1

    c = 2 * n + k - k * k
    discriminant = (Decimal(9) - Decimal(4) * c).sqrt()
    res1 = ((Decimal(3) + discriminant) / 2).to_integral_exact(rounding=ROUND_FLOOR)
    res2 = ((Decimal(3) - discriminant) / 2).to_integral_exact(rounding=ROUND_FLOOR)
    res = max(res1, res2)
    return int(k - res + 1)


def main(n: int):
    # 按规模 n 生成一组 (N, K) 测试数据
    # 这里令 N 在 [1, n] 之间，K 在 [1, N] 之间
    if n <= 0:
        return
    N = Decimal(random.randint(1, n))
    K = Decimal(random.randint(1, int(N)))
    ans = solve(N, K)
    print(ans)


if __name__ == "__main__":
    # 示例：使用规模参数 10
    main(10)