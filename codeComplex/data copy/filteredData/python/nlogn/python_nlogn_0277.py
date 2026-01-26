def main(n):
    d = {}
    # Interpret n as total number of operations; split into two phases
    m = n // 2
    k = n - m

    # First phase: build initial dictionary with m entries
    for i in range(m):
        a = i  # key
        x = (i * 3 + 1) % (n + 1)  # value
        d[a] = x

    # Second phase: update dictionary with k operations
    for j in range(k):
        b = j  # key
        y = (j * 5 + 2) % (n + 1)  # value
        d[b] = max(y, d.get(b, 0))

    # print(sum(d.values()))
    pass
if __name__ == "__main__":
    main(10)