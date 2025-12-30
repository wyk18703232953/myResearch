import random

def zeta_super(val, n):
    # len(val) == 2^n
    out = val[:]
    for i in range(n):
        for j in range(1 << n):
            if not (j >> i) & 1:
                out[j] += out[j ^ (1 << i)]
    return out

def main(n):
    """
    n: problem size (length of array a)

    This main generates test data as follows:
    - Chooses m so that values fit in [0, 2^m - 1]
    - Generates n random integers in [0, 2^m - 1]
    Then runs the original logic on this generated data.
    """
    # You can adjust m generation strategy as needed.
    # Here we roughly match the scale of n (at least 1 bit).
    if n <= 0:
        print(0)
        return

    # Choose m so that 2^m is on the same order as n, at least 1.
    m = max(1, (n - 1).bit_length())

    # Generate test data: a list of n integers in [0, 2^m - 1]
    a = [random.randrange(1 << m) for _ in range(n)]

    MOD = 10**9 + 7

    # Adjust m in case max(a) is smaller (to match original code's behavior)
    m = max(a).bit_length() or 1

    v = [0] * (1 << m)
    for item in a:
        v[item] += 1

    # Precompute powers of 2 modulo MOD: v2[i] = 2^i (mod MOD), for i=0..n
    v2 = [1]
    for _ in range(n + 1):
        v2.append(v2[-1] * 2 % MOD)

    nv = zeta_super(v, m)

    ans = 0
    for b in range(1 << m):
        # nv[b] is count; use v2[nv[b]] = 2^(nv[b]) (mod MOD)
        term = (v2[nv[b]] - 1) * pow(-1, bin(b).count("1"))
        ans = (ans + term) % MOD

    print(ans % MOD)


if __name__ == "__main__":
    # Example: run with n = 10
    main(10)