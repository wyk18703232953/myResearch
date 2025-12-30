import sys
import math
import itertools
import functools
import collections
import operator
import copy


ORDA = 97
def lcm(a, b): return abs(a * b) // math.gcd(a, b)
def revn(n): return str(n)[::-1]
def dd(): return collections.defaultdict(int)
def ddl(): return collections.defaultdict(list)
def sieve(n):
    if n < 2: return list()
    prime = [True for _ in range(n + 1)]
    p = 3
    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 2
    r = [2]
    for p in range(3, n + 1, 2):
        if prime[p]:
            r.append(p)
    return r
def divs(n, start=2):
    r = []
    for i in range(start, int(math.sqrt(n) + 1)):
        if (n % i == 0):
            if (n / i == i):
                r.append(i)
            else:
                r.extend([i, n // i])
    return r
def divn(n, primes):
    divs_number = 1
    for i in primes:
        if n == 1:
            return divs_number
        t = 1
        while n % i == 0:
            t += 1
            n //= i
        divs_number *= t
def prime(n):
    if n == 2: return True
    if n % 2 == 0 or n <= 1: return False
    sqr = int(math.sqrt(n)) + 1
    for d in range(3, sqr, 2):
        if n % d == 0: return False
    return True
def convn(number, base):
    newnumber = 0
    while number > 0:
        newnumber += number % base
        number //= base
    return newnumber
def cdiv(n, k): return n // k + (n % k != 0)


def main(n: int):
    """
    n: 生成测试字符串的长度
    这里根据 n 生成一个由 'a'..'z' 组成的周期性字符串，
    然后对其执行原始逻辑。
    """
    if n <= 0:
        print(0)
        return

    # 生成测试数据：周期性的字母串，例如 n=10 -> "abcdefghij"
    # 长度为 n，字符来自小写字母
    letters = "abcdefghijklmnopqrstuvwxyz"
    s = "".join(letters[i % 26] for i in range(n))

    lens = len(s)
    max_ = 0
    for i in range(1, lens):
        d = {}
        for j in range(lens - i + 1):
            sub = s[j: j + i]
            if sub in d:
                d[sub] += 1
            else:
                d[sub] = 1
        if max(d.values()) > 1:
            max_ = i
    print(max_)


if __name__ == "__main__":
    # 示例：可以修改这里的 n 来测试不同规模
    main(20)