def main(n):
    # Interpret n as the number of bitmasks (nk) and the bit-length (m)
    # To keep it meaningful, set nk = max(2, n), m = max(1, n)
    nk = max(2, n)
    m = max(1, n)

    # Deterministically generate nk binary strings of length m
    # Using simple arithmetic pattern based on index
    a = []
    for i in range(nk):
        # Generate an integer whose bits follow a deterministic pattern
        # Example: bits set where (j + i) % 3 == 0
        val = 0
        for j in range(m):
            if (j + i) % 3 == 0:
                val |= (1 << j)
        a.append(val)

    if nk == 1:
        # print("NO")
        pass
        return

    from functools import reduce
    from operator import ior

    num = reduce(ior, a)
    for i in range(nk):
        k = a.copy()
        k.pop(i)
        n_or = reduce(ior, k)
        if n_or == num:
            # print("YES")
            pass
            return
    # print("NO")
    pass
if __name__ == "__main__":
    # Example call for time-complexity experiment
    main(10)