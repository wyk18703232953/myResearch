import sys

sys.setrecursionlimit(2 * 10**5 + 10)

def zeta_super(val, n):
    out = val[:]
    for i in range(n):
        for j in range(1 << n):
            if not (j >> i) & 1:
                out[j] += out[j ^ (1 << i)]
    return out

def main(n):
    # Deterministic data generation:
    # Interpret n as the length of array a.
    # Ensure all elements are within a reasonable bit-size range.
    if n <= 0:
        print(0)
        return

    # Generate a deterministic array a of length n.
    # Example pattern: a[i] cycles through values in [0, 2^k)
    # where k = max(1, (n.bit_length() // 2)) to get varying bit lengths.
    k = max(1, n.bit_length() // 2)
    max_val = (1 << k) - 1
    a = [(i * 3 + 1) & max_val for i in range(n)]

    M = 10**9 + 7
    if not a:
        print(0)
        return

    m = max(a).bit_length()
    if m == 0:
        # All zeros
        v2 = [1]
        for _ in range(n + 1):
            v2.append(v2[-1] * 2 % M)
        # Only subset formed by zeros
        ans = (v2[n] - 1) % M
        print(ans)
        return

    v = [0] * (1 << m)
    for item in a:
        v[item] += 1

    v2 = [1]
    for _ in range(n + 1):
        v2.append(v2[-1] * 2 % M)

    nv = zeta_super(v, m)
    ans = 0
    for b in range(1 << m):
        cnt = bin(b).count("1")
        sgn = -1 if cnt % 2 == 1 else 1
        ans += (v2[nv[b]] - 1) * sgn
        ans %= M
    print(ans % M)

if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)