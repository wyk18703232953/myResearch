def main(n):
    # Generate deterministic input list 'l' of size n
    # Pattern: l[i] = i % (max(1, n//3)) + 1 to keep values bounded but dependent on n
    if n <= 0:
        print(0)
        return

    base = max(1, n // 3)
    l = [(i % base) + 1 for i in range(n)]

    # Original core logic starts here
    i = 0
    p = []
    while 2**i <= 10**18:
        p.append(2**i)
        i = i + 1

    d = {}
    s = set()
    for i in l:
        s.add(i)
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    z = set()
    for i in s:
        f = 1
        for j in p:
            e = j - i
            if e in s:
                if e == i and d[e] == 1:
                    continue
                f = 0
                break
        if f:
            z.add(i)

    ans = 0
    for i in z:
        ans += d[i]

    print(ans)


if __name__ == "__main__":
    main(10)