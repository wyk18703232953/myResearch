import math
from decimal import Decimal, getcontext
import random

# 提高精度，避免 Decimal sqrt 精度不足
getcontext().prec = 50

def sum1(i: Decimal) -> Decimal:
    return i * (i + 1) / 2

def sum2(s: Decimal, e: Decimal) -> Decimal:
    return sum1(e) - sum1(s - Decimal(1)) - (e - s)

def solve(n_dec: Decimal, k_dec: Decimal) -> int:
    if n_dec == 1:
        return 0
    elif k_dec > n_dec:
        return 1
    elif sum2(Decimal(2), k_dec) < n_dec:
        return -1
    else:
        c = 2 * n_dec + k_dec - k_dec * k_dec
        discriminant = (Decimal(9) - Decimal(4) * c).sqrt()
        res1 = math.floor((Decimal(3) + discriminant) / 2)
        res2 = math.floor((Decimal(3) - discriminant) / 2)
        res1 = max(res1, res2)
        return int(k_dec - Decimal(res1) + Decimal(1))

def main(n: int):
    """
    n 为规模参数，用于生成测试数据：
    - 生成 n_dec = n（直接使用 n）
    - 生成 k_dec：在 [1, n+5] 范围内随机取值，覆盖 k<n、k==n、k>n 情形
    """
    if n <= 0:
        # 对于非正规模，给一个默认示例
        n_dec = Decimal(1)
        k_dec = Decimal(1)
    else:
        n_dec = Decimal(n)
        # k 在 [1, n+5] 内随机取值
        k_raw = random.randint(1, n + 5)
        k_dec = Decimal(k_raw)

    ans = solve(n_dec, k_dec)
    print(ans)

# 示例：需要时可手动调用 main
# if __name__ == "__main__":
#     main(10)