def main(n):
    # Map n to number of bitmasks and bit-length
    rows = max(1, n)
    bits = max(1, n)

    # Deterministically generate m from bits, but keep interface
    m = bits

    # Deterministically generate 'a' as list of integers represented by m-bit binary strings
    # Example pattern: a[i] = ((i + 1) * 3) mod (2^m), ensuring non-trivial overlaps
    limit = 1 << m
    a = [(((i + 1) * 3) % limit) for i in range(rows)]

    s = 0
    t = 0
    for x in a:
        t |= s & x
        s |= x

    # Keep output logic identical in effect
    # print(("YES", "NO")[all(x & s & ~t for x in a)])
    pass
if __name__ == "__main__":
    main(10)