import math
import random
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right

alphabets = list('abcdefghijklmnopqrstuvwxyz')


def isPrime(x):
    for i in range(2, x):
        if i * i > x:
            break
        if x % i == 0:
            return False
    return True


def ncr(n, r, p):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p


def primeFactors(n):
    l = []
    while n % 2 == 0:
        l.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            l.append(int(i))
            n = n / i
    if n > 2:
        l.append(n)
    return list(set(l))


def power(x, y, p):
    res = 1
    x = x % p
    if x == 0:
        return 0
    while y > 0:
        if (y & 1) == 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res


def SieveOfEratosthenes(n):
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] is True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return prime


def countdig(n):
    c = 0
    while n > 0:
        n //= 10
        c += 1
    return c


def prefix_sum(arr):
    r = [0] * (len(arr) + 1)
    for i, el in enumerate(arr):
        r[i + 1] = r[i] + el
    return r


def divideCeil(n, x):
    if n % x == 0:
        return n // x
    return n // x + 1


def ws(s):
    print(s)


def wi(n):
    print(n)


def wia(a):
    print(' '.join([str(x) for x in a]))


def power_set(L):
    cardinality = len(L)
    n = 2 ** cardinality
    powerset = []

    for i in range(n):
        a = bin(i)[2:]
        subset = []
        for j in range(len(a)):
            if a[-j - 1] == '1':
                subset.append(L[j])
        powerset.append(subset)

    powerset_orderred = []
    for k in range(cardinality + 1):
        for w in powerset:
            if len(w) == k:
                powerset_orderred.append(w)

    return powerset_orderred


def fastPlrintNextLines(a):
    print('\n'.join(map(str, a)))


def sortByFirstAndSecond(A):
    A = sorted(A, key=lambda x: x[0])
    A = sorted(A, key=lambda x: x[1])
    return list(A)


def main(n):
    """
    根据规模 n 生成一组 (n, k)，并输出原逻辑的结果。
    原逻辑：
        - 读入 n, k
        - 若 k <= n: 输出 (k-1)//2
        - 否则:      输出 max((2*n-k+1)//2, 0)

    这里的 n 为规模参数，用来生成测试数据：
        - 真实使用的 n_test = n
        - k 在 [1, 2*n] 范围内随机生成（若 n=0，则固定为 0）
    """
    if n < 0:
        n_test = 0
    else:
        n_test = n

    # 生成测试数据 k
    if n_test == 0:
        k = 0
    else:
        k = random.randint(1, 2 * n_test)

    # 按原题逻辑计算答案
    if k <= n_test:
        ans = (k - 1) // 2
    else:
        ans = max((2 * n_test - k + 1) // 2, 0)

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)