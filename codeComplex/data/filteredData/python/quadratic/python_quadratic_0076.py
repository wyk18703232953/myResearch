def main(n):
    # Generate deterministic test data based on n
    # Interpret n as total size parameter; derive:
    # - array length = n
    # - number of queries m = max(1, n // 2)
    a = [(i * 3 + 7) % (n + 5) for i in range(n)]
    m = max(1, n // 2)

    # Precompute initial inversion parity of array a
    c = 0
    for i in range(1, n):
        for j in range(i):
            if a[j] > a[i]:
                c += 1
    c = c % 2

    # Generate deterministic query ranges (l, r) using n and m
    # 1-based indices, similar to original constraints style
    for i in range(m):
        l = (i % n) + 1
        r = ((i * 2) % n) + 1
        if l > r:
            l, r = r, l
        s = (r - l + 1) // 2
        if s % 2 == 1:
            c = (c + 1) % 2
        if c == 0:
            # print("even")
            pass

        else:
            # print("odd")
            pass
if __name__ == "__main__":
    main(10)