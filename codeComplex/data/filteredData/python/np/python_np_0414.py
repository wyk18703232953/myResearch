def main(n):
    m = max(1, n // 5)
    n_rows = n
    arr = [[(i * m + j) % (n + 7) + 1 for j in range(m)] for i in range(n_rows)]

    x = 1
    N = 2 ** m - 1
    lo = 1
    hi = 1000000009
    ind = [0, 0]

    while True:
        l = {}
        freq = [0] * (2 ** m)
        for i in range(n_rows):
            an = 0
            row = arr[i]
            for j in range(m):
                if row[j] >= x:
                    an += 2 ** (m - j - 1)
            if freq[an] == 0:
                l[i] = an
            freq[an] = 1
        ch = 0
        for k1, v1 in l.items():
            for k2, v2 in l.items():
                if v1 | v2 == N:
                    ch = 1
                    ind[0] = k1 + 1
                    ind[1] = k2 + 1
                    break
            if ch:
                break
        if ch:
            lo = x
            x = x * 2
        else:
            hi = x
            break

    ans = lo
    while hi - lo > 1:
        x = (lo + hi) // 2
        l = {}
        freq = [0] * (2 ** m)
        for i in range(n_rows):
            an = 0
            row = arr[i]
            for j in range(m):
                if row[j] >= x:
                    an += 2 ** (m - j - 1)
            if freq[an] == 0:
                l[i] = an
            freq[an] = 1
        ch = 0
        for k1, v1 in l.items():
            for k2, v2 in l.items():
                if v1 | v2 == N:
                    ch = 1
                    ind[0] = k1 + 1
                    ind[1] = k2 + 1
                    break
            if ch:
                break
        if ch:
            lo = x
        else:
            hi = x
    ans = lo

    if ind[0] == 0:
        print("1 1")
    else:
        print(*ind)


if __name__ == "__main__":
    main(10)