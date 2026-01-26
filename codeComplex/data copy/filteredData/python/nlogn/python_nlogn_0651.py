from bisect import bisect

def main(n):
    # Map n to problem size deterministically
    # Let number of elements and number of operations both depend on n
    num_elements = max(1, n)
    num_ops = max(1, 2 * n)

    # Deterministic generation of vv (sorted list of integers)
    # Example: vv = [2*i + 1 for i in range(num_elements)]
    vv = sorted([2 * i + 1 for i in range(num_elements)])

    # Deterministic generation of operations
    # We simulate m operations; each operation is (one, x, dummy)
    # one alternates between 1 and 2; only one == 1 is used in original logic
    # x is chosen deterministically based on index; sometimes equals 1_000_000_000
    ops = []
    for i in range(num_ops):
        one = 1 if i % 3 != 0 else 2  # some ones, some non-ones
        if i % 10 == 0:
            x = 1000000000

        else:
            # Spread x around and inside vv's range
            x = i + (i // 3)
        dummy = 0
        ops.append((one, x, dummy))

    n_local = num_elements
    m_local = num_ops

    hh = [0] * n_local
    rr = 0
    for i in range(m_local):
        one, x, _ = ops[i]
        if one == 1:
            if x == 1000000000:
                rr += 1

            else:
                ind = bisect(vv, x)
                if ind:
                    hh[ind - 1] += 1

    r = n_local
    s = 0
    for i, h in reversed(list(enumerate(hh))):
        s += h
        r = min(r, s + i)
    result = r + rr
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)