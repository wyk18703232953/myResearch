def main(n):
    from collections import Counter

    # Deterministic generation of P (parent array of size n-1 with values in [1, n])
    # This mimics a tree-like parent structure in a deterministic way.
    P = [(i % n) + 1 for i in range(1, n)]

    LIST = [0] * (n + 1)
    LEAF = [1] * (n + 1)

    for p in P:
        LEAF[p] = 0

    for i in range(1, n + 1):
        if LEAF[i] == 1:
            LIST[i] = 1

    for i in range(n, 1, -1):
        LIST[P[i - 2]] += LIST[i]

    counter = Counter(LIST[1:])

    SUM = [0]
    SC = sorted(counter.keys())

    for j in SC:
        SUM.append(SUM[-1] + counter[j])

    i = 1
    j = 0
    out = []
    while j < len(SUM):
        if i <= SUM[j]:
            out.append(str(SC[j - 1]))
        else:
            j += 1
            continue
        i += 1

    if out:
        print(" ".join(out))


if __name__ == "__main__":
    main(10)