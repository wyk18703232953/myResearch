def main(n):
    d = {}
    # Use n as base size; define number of pairs in first and second phase
    m = n

    # First set of pairs: keys 0..n-1, values = i % 10
    for i in range(n):
        a = i
        x = i % 10
        d[a] = x

    # Second set of pairs: keys = i // 2, values = (i * 3) % 7
    for i in range(m):
        b = i // 2
        y = (i * 3) % 7
        if b in d:
            d[b] = max(y, d[b])
        else:
            d[b] = y

    count = 0
    for key in d:
        count += d[key]
    print(count)


if __name__ == "__main__":
    main(10)