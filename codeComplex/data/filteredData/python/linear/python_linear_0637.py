def main(n):
    # n is the size of array a
    if n <= 0:
        return
    # Deterministic construction of a:
    # mix 1s and non-1s so the algorithm has something to work with
    # Example pattern: a[i] = 1 if i % 3 == 0 else (i % 5) + 2
    a = [1 if i % 3 == 0 else (i % 5) + 2 for i in range(n)]

    b = []
    c = []
    e = []
    for i in range(n):
        if a[i] == 1:
            b.append(i)
    for i in range(n):
        if a[i] != 1:
            c.append([a[i], i])
    if not c:
        print("NO")
        return
    ans = len(c)
    for i in range(len(c) - 1):
        e.append((c[i][1], c[i + 1][1]))
        c[i][0] -= 1
        c[i + 1][0] -= 1
    if b:
        e.append((b[-1], c[-1][1]))
        c[-1][0] -= 1
        b.pop()
        ans += 1
    if b:
        e.append((b[-1], c[0][1]))
        c[0][0] -= 1
        b.pop()
        ans += 1
    i = 0
    while b:
        while i < len(c) and c[i][0] == 0:
            i += 1
        if i == len(c):
            print("NO")
            return
        e.append((b[-1], c[i][1]))
        c[i][0] -= 1
        b.pop()

    print("YES", ans - 1)
    print(len(e))
    for (x, y) in e:
        print(x + 1, y + 1)


if __name__ == "__main__":
    main(10)