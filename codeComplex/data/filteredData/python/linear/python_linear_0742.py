def main(n):
    # Interpret n as both the array length and the number of queries
    size = max(2, n)

    # Deterministically generate the initial list l of length size
    # Example pattern: l[i] = (i * 2 + 1) % (2 * size) + 1
    l = [((i * 2 + 1) % (2 * size)) + 1 for i in range(size)]

    queries = size  # number of queries, also deterministic and based on n

    if queries == 0:
        return

    maxval = max(l)
    pairs = []
    count = 0
    f = l[0]
    secix = 1
    while f != maxval:
        count += 1
        f = l[0]
        s = l[secix]
        pairs.append([f, s])
        f, s = max(f, s), min(f, s)
        l[0] = f
        l.append(s)
        secix += 1

    l = [l[0]] + l[secix:]

    for i in range(size - 1):
        pairs.append([maxval, l[1 + i]])

    # Deterministically generate the query list qs of length queries
    # Example pattern: cover range around [1, count + size] cyclically
    max_query_val = count + size
    if max_query_val <= 0:
        max_query_val = 1
    qs = [(i % max_query_val) + 1 for i in range(queries)]

    # Process queries deterministically
    outputs = []
    for q in qs:
        if q <= count:
            a, b = pairs[q - 1]
            outputs.append(f"{a} {b}")

        else:
            q -= (count + 1)
            pos = count + (q % (size - 1))
            a, b = pairs[pos]
            outputs.append(f"{a} {b}")

    # For time-complexity experiments: ensure some output is produced
    for line in outputs:
        # print(line)
        pass
if __name__ == "__main__":
    main(10)