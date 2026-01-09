def main(n):
    # Generate deterministic data
    # a: list of n unique strings
    a = [str(i) for i in range(n)]
    # queries: 2n queries; first n match a in order, next n are non-existing keys
    queries = [str(i) for i in range(n)] + [str(i + n) for i in range(n)]

    d = {}
    k = 0
    for i in range(len(a)):
        d[a[i]] = i
    for s in queries:
        if d.get(s, -1) != -1:
            c = d[s]
            # print(c - k + 1, end=' ')
            pass
            for i in range(k, c + 1):
                d[a[i]] = -1
            k = c + 1

        else:
            # print(0, end=' ')
            pass
    # print()
    pass
if __name__ == "__main__":
    main(10)