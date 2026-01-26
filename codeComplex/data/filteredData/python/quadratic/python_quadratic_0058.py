def main(n):
    # n controls the size of array a and the number of queries m
    if n <= 0:
        return

    # Construct array a of length n deterministically
    # Example pattern: a[i] = (i * 2 + 3) % n
    a = [(i * 2 + 3) % n for i in range(n)]

    # Compute initial parity (inversion parity)
    parity = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[j] < a[i]:
                parity ^= 1

    # Set number of queries m proportional to n (at least 1)
    m = max(1, n)

    # Generate m deterministic queries [l, r]
    # Example pattern: l = i % n, r = (l + (i // 2) + 1) % n, ensure l <= r
    queries = []
    for i in range(m):
        l = i % n
        r = (l + (i // 2) + 1) % n
        if l > r:
            l, r = r, l
        # ensure at least length 1 segment
        if l == r:
            r = min(n - 1, l + 1) if l + 1 < n else l
        queries.append((l, r))

    # Process each query with the original logic
    for l, r in queries:
        # convert to 1-based interval as in typical competitive problems:
        # but original code used input directly, so treat l,r as 1-based there
        # Here we generate l,r as 0-based and shift to 1-based for the formula
        l1 = l + 1
        r1 = r + 1

        dist = (r1 - l1 + 1)
        pairs = (dist - 1) * (dist) // 2

        if pairs & 1:
            parity ^= 1

        if parity:
            # print("odd")
            pass

        else:
            # print("even")
            pass
if __name__ == "__main__":
    # Example: run main with a chosen scale
    main(10)