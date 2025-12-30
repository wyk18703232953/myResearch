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
        tmp = discriminant / 2
        const = Decimal(3) / 2
        res1 = math.floor(const + tmp)
        res2 = math.floor(const - tmp)
        res1 = max(res1, res2)
        return int(k - res1 + 1)


def main(n: int):
    """
    n 为规模参数，用于生成测试数据。
    这里约定：
      - 随机生成 1 <= N <= n
      - 随机生成 1 <= K <= n
    然后调用原算法逻辑并输出结果。
    """
    # 提高精度，避免 sqrt 等运算带来误差
    getcontext().prec = 50

    # 生成测试数据：N, K 都在 [1, n] 内
    if n < 1:
        n = 1
    N = random.randint(1, n)
    K = random.randint(1, n)

    N_dec = Decimal(N)
    K_dec = Decimal(K)

    ans = solve(N_dec, K_dec)
    print(ans)


if __name__ == "__main__":
    # 示例：用规模 100 生成一组测试数据并运行
    main(100)