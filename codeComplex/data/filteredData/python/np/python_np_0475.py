from math import gcd

def t_prime(n):
    if n == 1:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        if p < n and pow(p, n - 1, n) != 1:
            return False
    return True

# Precompute primes once; for complexity experiments this cost is part of the program.
primes = [i for i in range(2, 10**5) if t_prime(i)]
pset = set(primes)

def run_algorithm(n, k, l):
    if k == 1:
        return "0"

    # Extend primes set with special factors from l
    for i in range(n):
        for j in range(i):
            u, v = l[i], l[j]
            poss = gcd(u, v)
            poss2 = max(u, v) // poss
            smol = min(poss, poss2)
            if t_prime(smol) and smol not in pset:
                primes.append(smol)
                pset.add(smol)

    powers = set()
    count = 0
    outLs = []
    pgood = []

    for p in primes:
        curr = []
        fp = [v for v in l if v % p == 0]
        for v in fp:
            v2 = v
            while v2 % p == 0:
                v2 //= p
            if v2 == 1:
                curr.append(v)
                powers.add(v)
        if len(curr) > 1:
            count += len(curr)
            outLs.append(curr)
            pgood.append(p)

    order = [(len(lis), lis) for lis in outLs]
    order.sort(key=lambda x: x[0])

    if len(order) == 0:
        return "0"

    if order[-1][0] == 2 and k % 2 and count > k:
        extra = -1
        need = -1
        last = []

        for v in l:
            if v in powers:
                continue

            v2 = v
            primesn = []
            for p in pgood:
                add = 1
                while v2 % p == 0:
                    v2 //= p
                    if add:
                        primesn.append(p)
                    add = 0
            if v2 == 1 and (need == -1 or need > len(primesn)):
                extra = v
                last = primesn
                need = len(last)
                assert need >= 2

        if need == -1 or 2 * need + 1 > k:
            return "0"

        other = []
        out = [extra]

        for lis in outLs:
            a, b = lis[0], lis[1]
            works = False
            for p in last:
                if a % p == 0:
                    works = True
                    break
            if works:
                out.append(a)
                out.append(b)
            else:
                other.append(a)
                other.append(b)

        assert len(out) == 2 * need + 1
        assert (k - 2 * need - 1) % 2 == 0

        ret = out + other[: (k - 2 * need - 1)]
        assert len(ret) == k

        return " ".join(map(str, ret))

    out = []
    need = k
    for i in range(len(order)):
        assert need != 1

        lis = order[i][1]
        if len(lis) < need - 1 or len(lis) == need or (len(lis) == need - 1 and i == len(order) - 1):
            out += lis
            need -= len(lis)
        elif len(lis) == need - 1:
            if len(lis) > 2:
                out += lis[:-1]
                need -= (len(lis) - 1)
                assert need == 2
        else:
            out += lis[:need]
            need = 0

    assert need + len(out) == k
    assert need >= 0
    assert need == 0 or len(out) == count

    for v in l:
        if need == 0:
            break
        if v in powers:
            continue
        v2 = v
        for p in pgood:
            while v2 % p == 0:
                v2 //= p
        if v2 == 1:
            out.append(v)
            need -= 1

    if need == 0:
        return " ".join(map(str, out))
    else:
        return "0"

def generate_input(n):
    # Map n to: length of list = n, and k = max(1, n//2)
    length = max(1, n)
    k = max(1, n // 2)

    # Deterministic construction of l:
    # l[i] are composite / mixed numbers based on i to exercise gcd/prime logic.
    l = []
    for i in range(1, length + 1):
        # Use small primes 2,3,5,7 in structured combinations
        val = 1
        if i % 2 == 0:
            val *= 2
        if i % 3 == 0:
            val *= 3
        if i % 5 == 0:
            val *= 5
        if i % 7 == 0:
            val *= 7
        if val == 1:
            # ensure non-trivial numbers
            val = i + 10
        l.append(val)
    return length, k, l

def main(n):
    n, k, l = generate_input(n)
    result = run_algorithm(n, k, l)
    print(result)

if __name__ == "__main__":
    main(1000)