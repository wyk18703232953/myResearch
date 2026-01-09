def main(n):
    # Deterministically generate a and s based on n
    # Example scheme:
    # a[q] = q % 3
    # s[q] = (n - 1 - q) % 3
    a = [(i % 3) for i in range(n)]
    s = [((n - 1 - i) % 3) for i in range(n)]

    d = []
    for q in range(n):
        d.append(a[q] + s[q])
    d = [n - q for q in d]
    for q in range(n):
        f = 0
        for q1 in range(q):
            if d[q1] > d[q]:
                f += 1
        g = 0
        for q1 in range(q + 1, n):
            if d[q1] > d[q]:
                g += 1
        if f != a[q] or g != s[q]:
            # print('NO')
            pass
            break

    else:
        # print('YES')
        pass
        # print(*d)
        pass
if __name__ == "__main__":
    main(10)