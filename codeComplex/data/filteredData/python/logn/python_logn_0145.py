import math
from decimal import Decimal, getcontext

getcontext().prec = 50

def sum2(s, e):
    return sum1(e) - sum1(s - 1) - (e - s)

def sum1(i):
    return i * (i + 1) / 2

def main(n):
    # 确定性生成 n 和 k
    # 映射规则：逻辑当中需要 n >= 1, k >= 1
    N = Decimal(n)
    if N < 1:
        N = Decimal(1)
    # 令 k 在 [1, N+5] 范围内有规律变化
    K = (N // 2) + 1
    if K > N + 5:
        K = N + 5
    k = Decimal(K)
    n_dec = N

    if n_dec == 1:
        # print(0)
        pass
    elif k > n_dec:
        # print(1)
        pass
    elif sum2(Decimal(2), k) < n_dec:
        # print(-1)
        pass

    else:
        c = 2 * n_dec + k - k * k
        discriminant = (Decimal(9) - Decimal(4) * c).sqrt()
        tmp = discriminant / 2
        const = Decimal(3) / 2
        res1 = math.floor(const + tmp)
        res2 = math.floor(const - tmp)
        res1 = max(res1, res2)
        # print(k - res1 + 1)
        pass
if __name__ == "__main__":
    main(10)