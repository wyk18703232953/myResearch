def main(n):
    # Interpret n as the number of elements in the list.
    # Generate deterministic list l of length n.
    # Example: l = [1, 2, ..., n]
    l = [i + 1 for i in range(n)]

    # Deterministically set ll, r, x based on n to keep logic meaningful and scalable.
    ll = n  # minimal sum threshold
    r = n * (n + 1) // 2  # maximal possible sum of all elements
    x = max(1, n // 4)  # minimal required difference between max and min in subset

    subset = []
    for mask in range(1, 2 ** n):
        sub = []
        for j in range(n):
            if (1 << j) & mask:
                sub.append(l[j])
        subset.append(sub)

    c = 0
    for s in subset:
        if len(s) > 1:
            su = sum(s)
            if ll <= su <= r and (max(s) - min(s)) >= x:
                c += 1

    print(c)


if __name__ == "__main__":
    main(10)