def main(n):
    # n: length of array a
    if n <= 0:
        return
    # define k as a deterministic function of n
    k = max(1, n // 3)
    if k > n:
        k = n

    # deterministic generation of a
    a = [(i * 7 + 3) % (2 * n + 1) for i in range(n)]

    b = list(a)
    b.sort()
    c = []
    total = 0
    for i in range(1, k + 1):
        c.append(b[-i])
        total += b[-i]
    print(total)
    d = []
    for i in range(n):
        if a[i] in c:
            d.append(i)
            c.remove(a[i])
        else:
            pass
    d.insert(0, -1)
    d[-1] = n - 1
    e = []
    for i in range(1, len(d)):
        e.append(d[i] - d[i - 1])
    print(" ".join(map(str, e)))


if __name__ == "__main__":
    main(10)