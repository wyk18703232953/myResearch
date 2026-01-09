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
    import math
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
    # print('\n'.join(map(str, a)))
    pass

def sortByFirstAndSecond(A):
    A = sorted(A, key=lambda x: x[0])
    A = sorted(A, key=lambda x: x[1])
    return list(A)

def main(n):
    # Input structure in original code:
    # single test case:
    # n, k
    # s (string of parentheses, length n)
    #
    # Here we interpret the experimental parameter `n` as the string length.
    # k must be an even number <= n and such that a valid balanced substring
    # can be constructed. A simple deterministic choice:
    #   k = 2 * (n // 2)  (largest even <= n)
    if n <= 0:
        return

    k = 2 * (n // 2)
    if k == 0:
        # print("")
        pass
        return

    # Deterministic generation of a valid parentheses string of length n.
    # Pattern: first half '(' then ')', then repeat if necessary.
    base = ['('] * (n // 2) + [')'] * (n - n // 2)
    s = (base * (n // len(base) + 1))[:n]

    cnt = 0
    ans = []
    covered = 0
    for i in range(n):
        if s[i] == '(':
            cnt += 1
            ans.append('(')

        else:
            ans.append(')')
            covered += 1
        if cnt == k // 2:
            break
    ans += [')'] * (k // 2 - covered)
    # print(''.join(ans))
    pass
if __name__ == "__main__":
    main(10)