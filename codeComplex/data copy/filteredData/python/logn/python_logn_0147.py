import math
from decimal import Decimal, ROUND_FLOOR

def sum2(s, e):
    return sum1(e) - sum1(s - 1) - (e - s)

def sum1(i):
    return i * (i + 1) / 2

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
        res1 = int(((3 + discriminant) / 2).to_integral_exact(rounding=ROUND_FLOOR))
        res2 = int(((3 - discriminant) / 2).to_integral_exact(rounding=ROUND_FLOOR))
        res1 = max(res1, res2)
        return int(k - res1 + 1)

def main(n):
    n_dec = Decimal(n)
    k = n_dec // 2 + 1
    result = core(n_dec, k)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)