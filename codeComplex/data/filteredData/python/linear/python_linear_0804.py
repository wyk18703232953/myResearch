def main(n):
    # Deterministic data generation based on n
    # Map n to parameters of the original problem:
    # n -> original n (max value)
    # m -> number of elements in p (here set equal to n)
    # k -> page size (choose a small constant or function of n)
    orig_n = n
    m = n
    k = max(1, n // 5 + 1)

    # Generate a non-trivial, sorted list p of length m with values in [1, orig_n]
    # Use a deterministic arithmetic pattern
    p = [((i * 3) % orig_n) + 1 for i in range(1, m + 1)]
    p.sort()

    i = 0
    ct = 0
    ops = 0
    while i < len(p):
        nm = p[i] - ct
        if nm % k == 0:
            mnm = nm

        else:
            mnm = (nm // k) * k + k
        si = i
        while i < len(p) and p[i] - ct <= mnm:
            i += 1
        ct += i - si
        ops += 1
    # print(ops)
    pass
if __name__ == "__main__":
    main(10)