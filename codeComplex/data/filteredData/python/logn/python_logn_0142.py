import math
from decimal import Decimal, getcontext
import random

# 提高精度，防止 sqrt 等运算精度不足
getcontext().prec = 50

def sum1(i: Decimal) -> Decimal:
    return i * (i + 1) / 2

def sum2(s: Decimal, e: Decimal) -> Decimal:
    return sum1(e) - sum1(s - Decimal(1)) - (e - s)

def solve(n: int, k: int) -> int:
    dn = Decimal(n)
    dk = Decimal(k)

    if dn == 1:
        return 0
    elif dk > dn:
        return 1
    elif sum2(Decimal(2), dk) < dn:
        return -1
    else:
        c = 2 * dn + dk - dk * dk
        discriminant = (Decimal(9) - Decimal(4) * c).sqrt()
        res1 = math.floor((Decimal(3) + discriminant) / 2)
        res2 = math.floor((Decimal(3) - discriminant) / 2)
        res1 = max(res1, res2)
        return int(dk - res1 + 1)

def main(n: int):
    """
    n 为规模参数，用来生成测试数据:
    - 真实的 n 使用 1..n 的随机整数
    - k 使用 1..n 的随机整数（可按需要调整生成策略）
    """
    if n <= 0:
        return

    # 生成一组测试数据 (N, K)
    N = random.randint(1, n)
    K = random.randint(1, n)

    ans = solve(N, K)
    print(ans)

if __name__ == "__main__":
    # 示例：用规模 100 运行一次
    main(100)