def main(n):
    # For this refactoring, we remove interactive input and simulate answers deterministically.
    # We treat n as the number of bits for x and y (up to 30 in original code).
    # For determinism, define hidden x and y based on n.
    # Example deterministic construction:
    #   x = integer composed of alternating bits starting from LSB, masked to n bits
    #   y = bitwise complement of x within n bits
    # This guarantees a fixed, reproducible pair (x, y) for each n.
    n_bits = max(1, min(30, n))  # original code uses 30 bits
    mask = (1 << n_bits) - 1
    # Deterministic hidden numbers
    x = 0
    for i in range(n_bits):
        if i % 2 == 0:
            x |= (1 << i)
    x &= mask
    y = (~x) & mask

    def query(c, d):
        # Simulate the interactive oracle:
        # compare (x ^ c) and (y ^ d)
        val1 = x ^ c
        val2 = y ^ d
        if val1 < val2:
            return -1
        elif val1 > val2:
            return 1

        else:
            return 0

    # The original algorithm works with 30 bits; we adapt to n_bits
    s = [0] * (n_bits + 1)

    # Initial query corresponds to c = 0, d = 0
    t = query(0, 0)
    if t == 1:
        s[n_bits] = 1

    else:
        s[n_bits] = -1

    a = 0
    b = 0
    for i in range(n_bits, 0, -1):
        c = (1 << (i - 1)) + a
        d = b
        ans1 = query(c, d)
        c = a
        d = (1 << (i - 1)) + b
        ans2 = query(c, d)
        if ans1 == -1 and ans2 == 1:
            a += 1 << (i - 1)
            b += 1 << (i - 1)
            s[i - 1] = s[i]
        elif ans1 == 1 and ans2 == -1:
            a += 0 << (i - 1)
            b += 0 << (i - 1)
            s[i - 1] = s[i]

        else:
            s[i - 1] = ans1
            if s[i] == 1:
                a += 1 << (i - 1)
                b += 0 << (i - 1)

            else:
                a += 0 << (i - 1)
                b += 1 << (i - 1)

    # Output the reconstructed values and the hidden ones for verification
    # print(a, b, x, y)
    pass
if __name__ == "__main__":
    main(30)