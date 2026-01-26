import math
from decimal import Decimal

def sum1(i):
    return i * (i + 1) / 2

def sum2(s, e):
    return sum1(e) - sum1(s - 1) - (e - s)

def core(n, k):
    if n == 1:
        return 0
    elif k > n:
        return 1
    elif sum2(Decimal(2), k) < n:
        return -1

    else:
        c = 2 * n + k - k * k
        discriminant = (9 - 4 * c).sqrt()
        res1 = math.floor((3 + discriminant) / 2)
        res2 = math.floor((3 - discriminant) / 2)
        res1 = max(res1, res2)
        return int(k - res1 + 1)

def main(n):
    results = []
    # 生成 n 组测试数据：(n_i, k_i)
    # n_i 从 1 到 n，k_i = n_i // 2 + 1，保证 k_i 在 [1, n_i] 范围内变化
    for i in range(1, n + 1):
        ni = Decimal(i)
        ki = Decimal(i // 2 + 1)
        results.append(core(ni, ki))
    # 输出汇总结果，避免输出过大
    # print(sum(results))
    pass
if __name__ == "__main__":
    main(1000)