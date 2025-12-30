import random
import math
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop

def ncr(n, r, p):  # using fermat's little theorem
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

def prefix_sum(arr):
    r = [0] * (len(arr) + 1)
    for i, el in enumerate(arr):
        r[i + 1] = r[i] + el
    return r

def divideCeil(n, x):
    if n % x == 0:
        return n // x
    return n // x + 1

def main(n):
    # 生成长度为 n 的测试字符串，只包含两种字符 '0' 和 '1'
    if n <= 0:
        print(0)
        return

    chars = ['0', '1']
    s_list = [random.choice(chars) for _ in range(n)]
    s = ''.join(s_list)

    # 原始逻辑开始
    s = s * 3
    m = 0
    c = 1
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            c += 1
        else:
            m = max(m, c)
            c = 1
    m = max(m, c)
    m = min(m, len(s) // 3)
    print(m)

if __name__ == "__main__":
    # 示例：可调整 n 测试规模
    main(10)