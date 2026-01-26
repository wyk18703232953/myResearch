if __name__ == '__main__':
    cin = input
    n, m = map(int, cin().split())
    s, l, f = [[] for _ in range(n)], [0] * m, 0

    for i in range(n):
        t = cin()
        for j in range(m):
            if t[j] == "1":
                l[j] += int(t[j])
                s[i].append(j)
    for i in range(n):
        r = set(l[c] - 1 for c in s[i])
        if not 0 in r:
            f = not f
            break
    print("YNEOS"[not f::2])