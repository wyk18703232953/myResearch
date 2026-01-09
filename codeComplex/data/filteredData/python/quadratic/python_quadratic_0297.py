def main(n):
    # Generate deterministic input array a of length n
    # Example pattern: a[i] = (i // 2) % (n // 2 + 1) to ensure duplicates
    if n <= 0:
        # print(0)
        pass
        return
    base = max(1, n // 2)
    a = [(i // 2) % base for i in range(n)]

    p = 0
    while p + 1 < len(a) and a[p] == a[p + 1]:
        p += 2
    c = 0
    while p < len(a):
        if p + 1 < len(a):
            i = a.index(a[p], p + 1)
            c += i - p - 1
            tmp = a.pop(i)
            a.insert(p, tmp)
        while p + 1 < len(a) and a[p] == a[p + 1]:
            p += 2
    # print(c)
    pass
if __name__ == "__main__":
    main(10)