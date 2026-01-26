def main(n):
    # Interpret n as total number of key-value pairs
    # First half for the first loop, second half for the second loop
    m1 = n // 2
    m2 = n - m1

    k = {}

    # Deterministic generation for the first set of pairs
    # Keys and values constructed from simple arithmetic on indices
    for i in range(m1):
        a = i  # key
        x = i * 2 + 1  # value
        k[a] = x

    # Deterministic generation for the second set of pairs
    for j in range(m2):
        b = j  # key (may overwrite or create new)
        y = j * 3 + 2  # value
        if b in k:
            k[b] = max(k[b], y)

        else:
            k[b] = y

    s = 0
    for h in k.values():
        s += h
    # print(s)
    pass
if __name__ == "__main__":
    main(10)