def main(n):
    # Deterministic input generation based on n
    # Interpret n as: array length; set queries = n for scalability
    if n <= 1:
        # Edge case: minimum meaningful size is 2
        # Construct a simple example with n=2, queries=1
        n_local = 2
        queries = 1
        l = [1, 2]
    else:
        n_local = n
        queries = n
        # Generate a deterministic list of length n_local
        # Example pattern: l[i] = (i * 2) % n_local + 1
        l = [((i * 2) % n_local) + 1 for i in range(n_local)]

    # Core logic from original program (with input removed)
    if queries == 0:
        return

    maxval = max(l)
    pairs = []
    count = 0
    f = l[0]
    secix = 1

    # Build initial sequence of pairs until the maximum value reaches the front
    while f != maxval:
        count += 1
        f = l[0]
        s = l[secix]
        pairs.append([f, s])
        f, s = (f, s) if f >= s else (s, f)
        l[0] = f
        l.append(s)
        secix += 1

    # Compress the list after the maximum is at the front
    l = [l[0]] + l[secix:]

    # Add remaining pairs with maxval
    for i in range(n_local - 1):
        pairs.append([maxval, l[1 + i]])

    # Deterministic queries: q_k = k+1 (1-based), for k in [0, queries-1]
    for m in range(queries):
        q = m + 1
        if q <= count:
            print(str(pairs[q - 1][0]), str(pairs[q - 1][1]))
        else:
            q -= (count + 1)
            pos = count + (q % (n_local - 1))
            print(str(pairs[pos][0]), str(pairs[pos][1]))


if __name__ == "__main__":
    # Example deterministic call
    main(10)