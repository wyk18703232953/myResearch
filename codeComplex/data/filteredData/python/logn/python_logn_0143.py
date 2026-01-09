import math
from decimal import Decimal, getcontext

getcontext().prec = 50  # 提高精度，防止大数误差

def sum1(i: Decimal) -> Decimal:
    return i * (i + 1) / 2

def sum2(s: Decimal, e: Decimal) -> Decimal:
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
    res1 = Decimal(math.floor((Decimal(3) + discriminant) / 2))
    res2 = Decimal(math.floor((Decimal(3) - discriminant) / 2))
    res1 = max(res1, res2)
    return int(k - res1 + 1)

def main(n: int):
    """
    n: 规模参数，用来生成测试数据。
    测试数据策略（可按需要调整）：
    - n_data = n
    - k_data = max(2, n // 2)
    """
    n_data = Decimal(n)
    # 简单生成一个与 n 相关的 k，确保 k >= 2
    k_data = Decimal(max(2, n // 2))

    ans = solve(n_data, k_data)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)