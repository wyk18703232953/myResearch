def main(n):
    # n is the input size N
    N = max(2, n if n % 2 == 0 else n + 1)

    # Deterministically generate zb based on N
    # Ensure zb[0] == 0 so that za1 and za2 remain valid and non-decreasing
    # zb[i] = zb[i-1] + ((i % 3) + 1) for i >= 1
    zb = [0]
    for i in range(1, N // 2):
        zb.append(zb[-1] + (i % 3) + 1)
    # If original algorithm expects length N//2, keep that
    # If need full length N, extend deterministically
    while len(zb) < N:
        i = len(zb)
        zb.append(zb[-1] + (i % 3) + 1)

    za1 = [0]
    za2 = [zb[0]]

    for i in range(1, N // 2):
        t1 = zb[i] - za1[-1]
        if t1 <= za2[-1]:
            za1.append(za1[-1])
            za2.append(t1)
            continue
        t2 = zb[i] - za2[-1]
        if t2 >= za1[-1]:
            za1.append(t2)
            za2.append(za2[-1])
            continue
        # In deterministic test generation we avoid violating conditions,
        # so this should not happen.
        raise ValueError("Generated data violated constraints at index {}".format(i))

    zr = za1 + za2[::-1]
    zs = [str(x) for x in zr]
    r = ' '.join(zs)
    # print(r)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)