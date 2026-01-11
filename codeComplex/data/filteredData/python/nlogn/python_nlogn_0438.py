def main(n):
    # Precompute powers of 2 up to 2^31 (since original loop used i < 32)
    ans = [2 ** i for i in range(32)]

    # Deterministically generate input: list l of length n
    # Example pattern: l[i] = (i * 3) % (2 * n + 1)
    # This creates repeated values and a spread over a deterministic range.
    l = [(i * 3) % (2 * n + 1) for i in range(n)]

    # Build frequency dictionary
    d = {}
    for x in l:
        if x in d:
            d[x] += 1

        else:
            d[x] = 1

    # Core logic from original code
    c = 0
    for i in d.keys():
        for j in ans:
            if j - i in d and (j - i != i or d[j - i] > 1):
                break

        else:
            c += d[i]
    # print(c)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(1000)