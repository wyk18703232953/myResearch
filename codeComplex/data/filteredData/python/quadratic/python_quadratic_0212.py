def main(n):
    # Interpret n as the number of bitmasks; derive m (bit-length) deterministically from n
    m = max(1, n % 20 + 1)  # m in [1, 20], deterministic function of n

    # Deterministically generate n bitmasks of length m
    # bit i of number j is set if (j >> (i % max(1, n))) & 1 == 1
    a = []
    for j in range(n):
        x = 0
        for i in range(m):
            if (j >> (i % max(1, n))) & 1:
                x |= 1 << (m - 1 - i)
        a.append(x)

    s = 0
    t = 0
    for x in a:
        t |= s & x
        s |= x
    result = ("YES", "NO")[all(x & s & ~t for x in a)]
    print(result)
    return result


if __name__ == "__main__":
    # Example deterministic call
    main(10)