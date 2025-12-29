import math
from decimal import Decimal, getcontext
import random

# 提高精度，避免 sqrt 等操作精度不够
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
        res1 = math.floor((Decimal(3) + discriminant) / 2)
        res2 = math.floor((Decimal(3) - discriminant) / 2)
        res1 = max(res1, res2)
        return int(k - res1 + 1)

def main(n: int):
    """
    规模 n 用来生成测试数据 (n, k)：
    - 令 n_value = n
    - 随机生成 1 <= k <= n_value+5，覆盖 k<n, k==n, k>n 等情况
    """
    if n <= 0:
        raise ValueError("n must be positive for test generation")

    n_value = Decimal(n)
    # 让 k 在 [1, n+5] 内随机，保证既可能有 k<n，也可能 k>n
    k_int = random.randint(1, n + 5)
    k_value = Decimal(k_int)

    ans = solve(n_value, k_value)
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10)，真实使用时由外部指定 n
    main(10)