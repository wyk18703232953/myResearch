def main(n):
    # Generate deterministic test data based on n
    # l[i] = i % (n // 2 + 1)
    # r[i] = (n - 1 - i) % (n // 2 + 1)
    l = [(i % (n // 2 + 1)) for i in range(n)]
    r = [((n - 1 - i) % (n // 2 + 1)) for i in range(n)]

    c = [n] * n
    for i in range(n):
        c[i] -= (r[i] + l[i])

    for i in range(n):
        m = 0
        for j in range(0, i):
            if c[j] > c[i]:
                m += 1
        if m != l[i]:
            # print('NO')
            pass
            return

    for i in range(n):
        m = 0
        for j in range(i + 1, n):
            if c[j] > c[i]:
                m += 1
        if m != r[i]:
            # print('NO')
            pass
            return

    # print('YES')
    pass
    # print(*c)
    pass
if __name__ == "__main__":
    main(10)