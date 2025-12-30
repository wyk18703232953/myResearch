import math
from decimal import Decimal, ROUND_FLOOR, getcontext
import random

# 提高精度，避免大 n 时精度问题
getcontext().prec = 50

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
        discriminant = (Decimal(9) - 4 * c).sqrt()
        res1 = ((Decimal(3) + discriminant) / 2).to_integral_exact(rounding=ROUND_FLOOR)
        res2 = ((Decimal(3) - discriminant) / 2).to_integral_exact(rounding=ROUND_FLOOR)
        res = max(res1, res2)
        return int(k - res + 1)

def main(n: int):
    """
    n: 规模参数，用于生成测试数据。
       这里生成 n 的值为 Decimal(n)，k 取 [1, n] 之间的随机整数。
    """
    if n <= 0:
        return

    # 生成测试数据
    N = Decimal(n)
    K = Decimal(random.randint(1, max(1, n)))

    ans = solve(N, K)
    print(ans)

if __name__ == "__main__":
    # 示例：以 n=10 运行一次
    main(10)