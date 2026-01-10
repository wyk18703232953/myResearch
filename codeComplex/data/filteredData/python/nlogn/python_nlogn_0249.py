def main(n):
    from bisect import bisect_right

    if n < 2:
        n = 2
    m = n
    q = n

    a = [i + 1 for i in range(m)]
    k = [i * 2 + 1 for i in range(q)]

    for i in range(1, m):
        a[i] += a[i - 1]

    an = 0
    for j in k:
        j += an
        x = bisect_right(a, j)
        if x == m:
            print(m)
            an = 0
        else:
            print(m - x)
            an = j


if __name__ == "__main__":
    main(10)