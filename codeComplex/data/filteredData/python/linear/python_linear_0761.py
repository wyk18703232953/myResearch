def main(n):
    """
    Deterministic, non-interactive version of the original program.
    n controls the size of the array a and the number of queries q.
    """

    if n <= 1:
        # Degenerate case: nothing meaningful to simulate, mirror original behavior as no output
        return

    # Deterministic construction of n, q, a, Q
    # Original input structure:
    #   first line: n q
    #   second line: list a of length n
    #   next q lines: each a single integer query
    #
    # Here we:
    #   - keep the same n passed into main
    #   - set q = n (so total input scale is O(n))
    #   - construct a and Q deterministically from n

    q = n

    # Build array a of size n, deterministic pattern
    # Make it non-trivial but simple and reproducible
    # Example: a[i] = (i * 2 + 3) % n + 1  (1..n)
    a = [((i * 2 + 3) % n) + 1 for i in range(n)]

    # Build query list Q of size q, with values in 1..(2n) to exercise both branches i<=n and i>n
    # Example sequence:
    #   Q[i] = (i % (2*n)) + 1
    Q = [(i % (2 * n)) + 1 for i in range(q)]

    # Core algorithm logic from original code (without any input calls)
    if q == 0:
        return

    sq = set(Q)
    mx = max(Q)
    d = dict()
    ch = 1

    # Simulate the pairings as in original
    limit = min(mx, n + 1)
    for i in range(limit):
        if ch == n:
            ch = 1
        if i + 1 in sq:
            d[i + 1] = [a[0], a[ch]]
        if a[0] < a[ch]:
            a[0], a[ch] = a[ch], a[0]
        ch += 1

    # Produce outputs for all queries
    for i in Q:
        if i > n:
            x = n - 1 if i % (n - 1) == 0 else i % (n - 1)
            print(a[0], a[x])
        else:
            # some queries may not be in d if mx < i or the loop limit prevented filling them
            # to keep behavior defined and deterministic, fall back to a fixed pair if missing
            if i in d:
                print(*d[i])
            else:
                # fallback pair uses current a[0] and a[1] (or a[0] twice if n==1, but n>1 here)
                second_index = 1 if n > 1 else 0
                print(a[0], a[second_index])


if __name__ == "__main__":
    # Example deterministic call; adjust n to probe different scales
    main(10)