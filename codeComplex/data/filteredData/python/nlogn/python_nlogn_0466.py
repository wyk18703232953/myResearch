def main(n):
    # Interpret n as both the array length and k (top-k elements),
    # with a minimum of 1 for k to keep behavior defined.
    if n <= 0:
        return

    k = n

    # Deterministic generation of array a of length n
    # Example pattern: a[i] = (i * 7) % (n + 5) + 1
    a = [((i * 7) % (n + 5)) + 1 for i in range(n)]

    b = list(a)
    b.sort()
    c = []
    total = 0
    upper_k = min(k, n)
    for i in range(1, upper_k + 1):
        c.append(b[-i])
        total += b[-i]
    # print(total)
    pass

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
    # print(" ".join(map(str, e)))
    pass
if __name__ == "__main__":
    main(10)