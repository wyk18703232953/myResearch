import random
import math as mt
from collections import Counter


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a * b) / gcd(a, b)


mod = int(1e9) + 7


def power(k, n):
    if n == 0:
        return 1
    if n % 2:
        return (power(k, n - 1) * k) % mod
    t = power(k, n // 2)
    return (t * t) % mod


def totalPrimeFactors(n):
    count = 0
    if (n % 2) == 0:
        count += 1
        while (n % 2) == 0:
            n //= 2

    i = 3
    while i * i <= n:
        if (n % i) == 0:
            count += 1
            while (n % i) == 0:
                n //= i
        i += 2
    if n > 2:
        count += 1
    return count


def main(n):
    # 生成测试数据：n 个非负整数，范围可根据需要调整
    # 这里生成 [0, n] 范围内的随机数
    random.seed(0)
    a = [random.randint(0, n) for _ in range(n)]

    a.sort()
    same = 0
    ind = -1
    poss = 1
    for i in range(1, n):
        same += (a[i] == a[i - 1])
        if a[i] == a[i - 1]:
            ind = i - 1
            if a[i] == 0:
                poss = 0
    if same > 1 or poss == 0:
        print('cslnb')
    else:
        if ind > 0:
            if a[ind] - a[ind - 1] == 1:
                print('cslnb')
                return
        c = 0
        for i in range(n):
            c += a[i] - i
        if c % 2:
            print('sjfnb')
        else:
            print('cslnb')


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)