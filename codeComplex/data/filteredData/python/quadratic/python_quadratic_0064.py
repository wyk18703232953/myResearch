def main(n):
    # n controls the size of array a and the number of queries q (both = n)
    if n <= 0:
        return
    # Deterministic construction of a: a[i] = (i * 37 + 13) % (n + 5)
    a = [(i * 37 + 13) % (n + 5) for i in range(n)]
    s = 0
    for i in range(n):
        for j in range(i):
            s ^= a[j] > a[i]
    q = n
    # Deterministic construction of queries:
    # l = i % n, r = (i * 2 + 3) % n, ensure l <= r
    for i in range(q):
        l = i % n
        r = (i * 2 + 3) % n
        if l > r:
            l, r = r, l
        s ^= (r - l + 1) * (r - l) // 2 % 2
        print(['even', 'odd'][s])


if __name__ == "__main__":
    main(10)