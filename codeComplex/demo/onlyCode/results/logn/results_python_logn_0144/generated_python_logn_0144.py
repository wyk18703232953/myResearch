import math
from decimal import Decimal, getcontext

def sum2(s, e):
    return sum1(e) - sum1(s - 1) - (e - s)

def sum1(i):
    return i * (i + 1) / 2

def main(n):
    getcontext().prec = 50
    n = Decimal(n)
    k = Decimal(n)
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

if __name__ == "__main__":
    print(main(10))