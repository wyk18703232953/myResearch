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
    # Interpret n as the input size parameter.
    # We deterministically construct (n, k) as in the original logic requiring two integers.
    # Here we keep the "problem scale" as n, and choose k in a deterministic way:
    # k ranges around n to cover both branches of the original condition.
    # For time complexity experiments, we can run the core logic once on such a pair.
    if n <= 0:
        return

    # Deterministic construction of k from n, ensuring variation:
    # For small n, keep k within a simple range; for larger n, let k depend on n.
    # Example choice: k = (3*n)//2 (so k > n for n>0) to exercise the second branch,
    # but we can also run both branches by using two k's.
    # To keep it scalable but still aligned with original single-test-case structure,
    # we run once with a k derived from n.
    k = (3 * n) // 2

    if k <= n:
        result = (k - 1) // 2

    else:
        result = max((2 * n - k + 1) // 2, 0)

    # print(result)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n here when running experiments
    main(10)