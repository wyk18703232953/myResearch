def main(n):
    # Generate deterministic input array of length n
    # Pattern: a[i] = i % 3 to ensure many duplicates
    a = [i % 3 for i in range(n)]

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