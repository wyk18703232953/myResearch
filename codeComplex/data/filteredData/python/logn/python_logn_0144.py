import math
from decimal import Decimal, getcontext
import random


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
    # 设置更高精度，避免 Decimal 运算精度问题
    getcontext().prec = 50

    # 根据规模 n 生成一组测试数据 (n, k)
    # 规则：1 <= n <= n，1 <= k <= n
    n_val = Decimal(random.randint(1, max(1, n)))
    k_val = Decimal(random.randint(1, int(n_val)))

    ans = solve(n_val, k_val)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10) 生成规模为 10 的测试数据并执行
    main(10)