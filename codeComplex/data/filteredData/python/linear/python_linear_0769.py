def main(n):
    # Interpret n as:
    # a = n           length of sequence A
    # b = n           number of queries
    a = max(2, n)
    b = max(1, n)

    # Deterministic generation of A (length a)
    # Example: A[i] = (i * 2 + 1) % (2 * a + 1)
    A = [(i * 2 + 1) % (2 * a + 1) for i in range(a)]

    # Deterministic generation of query values w (length b)
    # Make them cover both w <= len(Z) and w > len(Z) cases reasonably.
    # We don't know len(Z) beforehand; use a simple formula based on a and i.
    queries = []
    base = max(1, a - 1)
    for i in range(b):
        # This produces numbers in a pattern that can be <= base and > base
        w = (i % (2 * base)) + 1
        queries.append(w)

    A.append(-1)
    B = []
    Z = []
    AN = []
    x, y = A[0], A[1]
    for i in range(a - 1):
        Z.append((x, y))
        if x > y:
            B.append(y)
            y = A[i + 2]
        else:
            B.append(x)
            x, y = y, A[i + 2]
    for w in queries:
        if w <= len(Z):
            AN.append(Z[w - 1])
        else:
            w = w % len(B)
            if w == 0:
                w = len(B)
            AN.append((x, B[w - 1]))
    for W in AN:
        print(*W)


if __name__ == "__main__":
    main(10)