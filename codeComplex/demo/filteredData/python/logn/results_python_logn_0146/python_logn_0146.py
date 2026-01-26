import math
from decimal import Decimal, ROUND_FLOOR


def sum1(i: Decimal) -> Decimal:
    return i * (i + 1) / 2


def sum2(s: Decimal, e: Decimal) -> Decimal:
    return sum1(e) - sum1(s - 1) - (e - s)


def solve(n: Decimal, k: Decimal) -> int:
    if n == 1:
        return 0
    elif k > n:
        return 1
    elif sum2(Decimal(2), k) < n:
        return -1

    else:
        c = 2 * n + k - k * k
        discriminant = (Decimal(9) - Decimal(4) * c).sqrt()
        res1 = int(((Decimal(3) + discriminant) / 2).to_integral_exact(rounding=ROUND_FLOOR))
        res2 = int(((Decimal(3) - discriminant) / 2).to_integral_exact(rounding=ROUND_FLOOR))
        res1 = max(res1, res2)
        return int(k) - res1 + 1


def main(n: int):
    # 根据规模 n 生成测试数据：
    # 令 n_dec = n，k 在 [1, n] 中取一个典型值，这里取 k = max(2, n//2) 作为示例
    n_dec = Decimal(n)
    if n <= 2:
        k_dec = Decimal(2)

    else:
        k_dec = Decimal(max(2, n // 2))

    ans = solve(n_dec, k_dec)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main，规模可修改
    main(10)