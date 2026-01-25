import sys
import os
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


def ws(s):
    sys.stdout.write(s + '\n')


def wi(n):
    sys.stdout.write(str(n) + '\n')


def wia(a):
    sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


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


def solve_single_case(n, m, s, t):
    if '*' not in s:
        if s == t:
            print("YES")
        else:
            print("NO")
        return
    i = s.index('*')
    if s[:i] == t[:i]:
        s_suffix = s[i:]
        t_suffix = t[i:]
        s_rev = s_suffix[::-1]
        t_rev = t_suffix[::-1]
        i2 = s_rev.index('*')
        if len(t_rev) >= i2 and s_rev[:i2] == t_rev[:i2]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")


def generate_case(n):
    # Input structure: single test case, two integers n,m then two strings s,t
    # Here experimental "n" controls the length of s and t.
    # Ensure length >= 1
    length = max(1, n)

    # Place '*' at a deterministic position
    # For variety, position cycles with length
    star_pos = length // 3
    if star_pos >= length:
        star_pos = length - 1

    # Build s with exactly one '*'
    base_chars = alphabets
    s_chars = []
    for i in range(length):
        if i == star_pos:
            s_chars.append('*')
        else:
            # deterministic letter based on i and length
            idx = (i * 7 + length) % len(base_chars)
            s_chars.append(base_chars[idx])
    s = ''.join(s_chars)

    # Build t so that for even n it matches the pattern rules, for odd n it does not
    if n % 2 == 0:
        # Make t match s under the original algorithm logic
        # prefix equal
        t_prefix = s[:star_pos]
        # suffix after '*' equal as well
        t_suffix = s[star_pos + 1:]
        t = t_prefix + t_suffix  # remove '*', will still satisfy algorithm's checks
        # To keep same length as s, append a deterministic char
        if len(t) < length:
            extra_idx = (length * 5 + n) % len(base_chars)
            t += base_chars[extra_idx]
        t = t[:length]
    else:
        # Force mismatch in prefix
        t_chars = []
        for i in range(length):
            idx = (i * 11 + n) % len(base_chars)
            ch = base_chars[idx]
            if i < star_pos and ch == s[i]:
                # change deterministically to a different char
                ch = base_chars[(idx + 1) % len(base_chars)]
            t_chars.append(ch)
        t = ''.join(t_chars)

    return length, length, s, t


def main(n):
    # n controls the length of strings s and t in a single test case
    m, m2, s, t_str = generate_case(n)
    # m and m2 are both "length" in this deterministic generator; keep first as m
    solve_single_case(m, m2, list(s), list(t_str))


if __name__ == "__main__":
    # Example deterministic runs for different scales
    for scale in (1, 5, 10, 20):
        main(scale)