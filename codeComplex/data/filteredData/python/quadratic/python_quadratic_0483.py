def main(n):
    # Generate deterministic test data based on n
    # Construct a sequence k of length n, then derive l and r exactly as in the original logic.
    # This preserves the algorithm while removing all external input.

    if n <= 0:
        return

    # Deterministically construct k
    # Example: k[i] = (i * 2) % n to keep values in a bounded range and allow comparisons
    k = [(i * 2) % n for i in range(n)]

    # Compute l and r as in the original code's inner logic
    l = []
    r = []
    for i in range(n):
        c = 0
        d = 0
        for j in range(0, i):
            if k[j] > k[i]:
                c += 1
        for j in range(i + 1, n):
            if k[j] > k[i]:
                d += 1
        l.append(c)
        r.append(d)

    # Now run the original algorithm starting from l, r, n
    if l[0] != 0 or r[n - 1] != 0:
        # print("NO")
        pass
        return

    s = [l[i] + r[i] for i in range(n)]
    m = max(s) + 1
    k_reconstructed = [m - s[i] for i in range(n)]

    l1 = []
    r1 = []
    for i in range(n):
        c = 0
        d = 0
        for j in range(0, i):
            if k_reconstructed[j] > k_reconstructed[i]:
                c += 1
        l1.append(c)
        for j in range(i + 1, n):
            if k_reconstructed[j] > k_reconstructed[i]:
                d += 1
        r1.append(d)

    if l1 != l or r1 != r:
        # print("NO")
        pass

    else:
        # print("YES")
        pass
        # print(*k_reconstructed)
        pass
if __name__ == "__main__":
    main(10)