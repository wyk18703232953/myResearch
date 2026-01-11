def merge(a, b):
    inda = 0
    indb = 0
    lena = len(a)
    lenb = len(b)
    d = [a[-1] + b[-1] + 1000]
    a = a + d
    b = b + d
    c = []
    inversions = 0
    for _ in range(lena + lenb):
        if a[inda] < b[indb]:
            c.append(a[inda])
            inda += 1

        else:
            c.append(b[indb])
            indb += 1
            inversions += lena - inda
    return (c, inversions)


def mergesort(a):
    if len(a) <= 1:
        return (a, 0)
    split = len(a) // 2
    b = a[:split]
    c = a[split:]
    d = mergesort(b)
    e = mergesort(c)
    f = merge(d[0], e[0])
    return (f[0], f[1] + d[1] + e[1])


def main(n):
    # Deterministic generation of input array `a` of length n
    # Values in [1, n] and -1 interleaved deterministically
    a = [(-1 if i % 3 == 0 else (i % n) + 1) for i in range(n)]

    b = []
    for guy in a:
        if guy != -1:
            b.append(guy)
    invs = mergesort(b)[1]
    negs = len(a) - len(b)
    pairs = (negs * (negs - 1)) // 2
    used = [0] * n
    for guy in a:
        if guy != -1:
            used[guy - 1] += 1
    unused = [0]
    for i in range(n - 1):
        unused.append(unused[-1] + 1 - used[i])
    negsseen = 0
    mix = 0
    for i in range(n):
        if a[i] == -1:
            negsseen += 1

        else:
            mix += unused[a[i] - 1] * (negs - negsseen) + negsseen * (negs - unused[a[i] - 1])
    num = invs * 2 * negs + pairs * negs + mix * 2
    denom = 2 * negs
    MOD = 998244353
    if negs == 0:
        # print(invs % MOD)
        pass

    else:
        # Compute modular inverse of denom modulo MOD using extended Euclid
        def egcd(a, b):
            if b == 0:
                return a, 1, 0
            g, x1, y1 = egcd(b, a % b)
            return g, y1, x1 - (a // b) * y1

        g, x, _ = egcd(denom, MOD)
        if g != 1:
            inv = 1

        else:
            inv = x % MOD
        # print((num * inv) % MOD)
        pass
if __name__ == "__main__":
    main(1000)