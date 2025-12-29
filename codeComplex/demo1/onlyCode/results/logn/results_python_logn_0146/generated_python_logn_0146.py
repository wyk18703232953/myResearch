import math
from decimal import Decimal, ROUND_FLOOR, getcontext
import random

# 提高精度，防止大 n 时精度问题
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
        discriminant = (Decimal(9) - Decimal(4) * c).sqrt()
        res1 = int(((Decimal(3) + discriminant) / 2).to_integral_exact(rounding=ROUND_FLOOR))
        res2 = int(((Decimal(3) - discriminant) / 2).to_integral_exact(rounding=ROUND_FLOOR))
        res1 = max(res1, res2)
        return int(k - res1 + 1)

def main(n: int):
    """
    n: 规模，用于生成测试数据。
    逻辑保持与原程序一致：原程序需要 n, k 两个输入，
    这里根据给定规模 n 自动生成 (N, K) 后求解。
    """
    # 生成测试数据 N, K：
    # N 取 [1, n] 内随机值
    if n <= 0:
        return  # 无有效规模

    N = Decimal(random.randint(1, n))

    # K 取 [1, max(1, 2n)] 内随机值，保证覆盖多种情况
    K_upper = max(1, 2 * n)
    K = Decimal(random.randint(1, K_upper))

    ans = solve(N, K)
    print(ans)

if __name__ == "__main__":
    # 示例：用某个规模调用 main
    main(100)