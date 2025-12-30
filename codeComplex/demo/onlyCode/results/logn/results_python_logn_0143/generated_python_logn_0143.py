import math
from decimal import Decimal, getcontext
import random

# 提高精度，避免 sqrt 等运算误差
getcontext().prec = 50

def sum1(i: Decimal) -> Decimal:
    return i * (i + 1) / 2

def sum2(s: Decimal, e: Decimal) -> Decimal:
    return sum1(e) - sum1(s - 1) - (e - s)

def main(n: int):
    """
    n 为规模参数，这里使用 n 生成测试数据：
    - 将原程序中的 n 限制在 [1, n]
    - 将 k 限制在 [1, n] 内随机生成
    """
    if n <= 0:
        return

    # 生成测试数据：n_val, k_val 都为 1..n 之间的整数
    n_val = Decimal(random.randint(1, n))
    k_val = Decimal(random.randint(1, n))

    if n_val == 1:
        print(0)
    elif k_val > n_val:
        print(1)
    elif sum2(Decimal(2), k_val) < n_val:
        print(-1)
    else:
        c = 2 * n_val + k_val - k_val * k_val
        discriminant = (Decimal(9) - Decimal(4) * c).sqrt()
        res1 = math.floor((Decimal(3) + discriminant) / 2)
        res2 = math.floor((Decimal(3) - discriminant) / 2)
        res1 = max(res1, res2)
        print(int(k_val - res1 + 1))

if __name__ == "__main__":
    # 示例：以 n = 10 作为规模运行一次
    main(10)