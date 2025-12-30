import random
import string
import math
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
        if prime[p]:
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


def generate_test_case(n):
    """
    生成一组 (n, m, s, t)
    - n: 用作 s 的长度
    - m: 用作 t 的长度，随机在 [max(1, n-3), n+3] 内波动
    - s: 含恰好一个或零个 '*' 的模式串
    - t: 普通字符串
    """
    # 决定是否生成带 '*' 的模式
    with_star = random.choice([True, False])

    # 生成 t 的长度
    m = max(1, n + random.randint(-3, 3))

    # 基础字符集
    chars = string.ascii_lowercase

    if not with_star:
        # 无 '*'：s 和 t 都为普通串
        s = ''.join(random.choice(chars) for _ in range(n))
        t = ''.join(random.choice(chars) for _ in range(m))
        return n, m, s, t

    # 有 '*' 的情况
    # 选择前缀长度和后缀长度，使前缀 + 后缀 <= n-1
    max_pref = max(0, n - 1)
    pref_len = random.randint(0, max_pref)
    max_suf = max(0, n - 1 - pref_len)
    suf_len = random.randint(0, max_suf)

    prefix = ''.join(random.choice(chars) for _ in range(pref_len))
    suffix = ''.join(random.choice(chars) for _ in range(suf_len))
    s = prefix + '*' + suffix

    # 随机决定是否构造一个必然匹配的 t
    make_match = random.choice([True, False])

    if make_match:
        # 保证匹配：
        # t 至少要有 prefix + suffix 长度
        min_len = pref_len + suf_len
        m = max(m, min_len)
        # 构造 t：前缀相同，中间任意，后缀相同
        middle_len = m - pref_len - suf_len
        middle = ''.join(random.choice(chars) for _ in range(middle_len))
        t = prefix + middle + suffix
    else:
        # 随机生成 t，不保证匹配
        t = ''.join(random.choice(chars) for _ in range(m))

    # 更新 m 为真实长度
    m = len(t)
    return len(s), m, s, t


def solve_one_case(n, m, s, t_str):
    s = list(s)
    t = list(t_str)

    if '*' not in s:
        if s == t:
            return "YES"
        else:
            return "NO"

    i = s.index('*')
    if s[:i] == t[:i]:
        s = s[i:]
        t = t[i:]
        s = s[::-1]
        t = t[::-1]
        i = s.index('*')

        if len(t) >= i and s[:i] == t[:i]:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


def main(n):
    # 生成一组基于规模 n 的测试数据
    n_s, m, s, t_str = generate_test_case(n)

    # 求解并输出
    ans = solve_one_case(n_s, m, s, t_str)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)