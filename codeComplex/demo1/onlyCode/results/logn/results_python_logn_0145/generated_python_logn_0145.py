import math
from decimal import Decimal, getcontext
import random

# 提高精度，避免 sqrt 等运算精度不够
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
        discriminant = (9 - 4 * c).sqrt()
        tmp = discriminant / 2
        const = Decimal(3) / 2
        res1 = math.floor(const + tmp)
        res2 = math.floor(const - tmp)
        res1 = max(res1, res2)
        return int(k - res1 + 1)

def main(n: int):
    """
    n 为规模参数，用来生成测试数据。
    此处约定：
      - 实际问题中的 n (Decimal) 在 [1, n]
      - k 在 [1, n] 范围内随机生成
    """
    if n <= 0:
        raise ValueError("n must be positive")

    # 生成测试数据：随机 n_val, k_val
    n_val_int = random.randint(1, n)
    k_val_int = random.randint(1, n)

    n_val = Decimal(n_val_int)
    k_val = Decimal(k_val_int)

    ans = solve(n_val, k_val)
    print(ans)

# 示例：如果你想在本文件直接运行，可以取消下面两行注释
# if __name__ == "__main__":
#     main(10)