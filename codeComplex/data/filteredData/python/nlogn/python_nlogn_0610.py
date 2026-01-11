def main(n):
    from bisect import bisect_right
    # Deterministically generate x, y based on n
    x = n + 5
    y = (2 * n + 3) or 1

    # Generate intervals s, e deterministically
    s = [i * 2 for i in range(n)]
    e = [s[i] + (i % 5 + 1) for i in range(n)]

    v = [0] * n
    c = 0
    for i in range(n):
        c += x + (e[i] - s[i]) * y

    s.sort()
    e.sort()
    for i in range(n - 2, -1, -1):
        k = bisect_right(s, e[i])
        while (k < n) and (v[k] == 1) and (s[k] - e[i]) * y < x:
            k += 1
        if k == n:
            continue
        if (s[k] - e[i]) * y < x:
            v[k] = 1
            c += (s[k] - e[i]) * y - x

    # print(c % (10 ** 9 + 7))
    pass
if __name__ == "__main__":
    main(10)