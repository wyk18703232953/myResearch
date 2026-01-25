def main(n):
    # Interpret n as the number of binary strings (nk).
    # We deterministically generate nk binary strings of length nk.
    nk = max(2, n)
    m = nk

    a = []
    for i in range(nk):
        val = 0
        for j in range(m):
            # Deterministic pattern: bit j of string i is 1 if (i + j) is even
            if (i + j) % 2 == 0:
                val |= (1 << (m - 1 - j))
        a.append(val)

    if nk == 1:
        print("NO")
        return

    from functools import reduce
    from operator import ior

    num = reduce(ior, a)
    for i in range(nk):
        k = a.copy()
        k.pop(i)
        n_or = reduce(ior, k)
        if n_or == num:
            print("YES")
            return
    print("NO")


if __name__ == "__main__":
    main(5)