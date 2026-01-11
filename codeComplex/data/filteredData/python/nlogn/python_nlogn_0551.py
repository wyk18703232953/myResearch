def main(n):
    from math import ceil

    # Deterministic data generation:
    # Interpret n as the length of the list r
    # Generate r[i] in [1, n] deterministically
    r = [(i % n) + 1 for i in range(1, n + 1)]

    l = [-1]
    l.extend(r)
    a = [''] * (n + 1)
    d = {}
    rd = {}
    ind = {}

    for i in range(1, n + 1):
        x = l[i]
        ind[x] = i
        d.setdefault(i, [])
        s = x + i
        while s <= n:
            if l[s] > x:
                d[i].append(s)
                if s not in rd:
                    rd[s] = []
                rd[s].append(i)
            s += x
        s = i - x
        while s >= 1:
            if l[s] > x:
                d[i].append(s)
            s -= x

    ans = 0

    for i in d:
        if len(d[i]) == 0:
            a[i] = 'B'
            ans += 1

    while ans != n:
        for i in d:
            dont = False
            if a[i] != '':
                continue
            for j in d[i]:
                if a[j] == 'B':
                    a[i] = 'A'
                    ans += 1
                    break
                if a[j] == '':
                    dont = True

            else:
                if not dont:
                    a[i] = 'B'
                    ans += 1

    # print(''.join(a[1:]))
    pass
if __name__ == "__main__":
    main(10)