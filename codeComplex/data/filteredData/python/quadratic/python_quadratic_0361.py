def main(n):
    # Interpret n as both number of rows and columns
    # Ensure at least 1x1 grid
    n = max(1, int(n))
    m = n

    res = []
    a = [None] * n
    l = [None] * n
    r = [None] * n
    s = [0] * n

    # Deterministic grid generation based on n, m
    # Pattern: '*' where (i+j) % 3 == 0, else '.'
    for i in range(n):
        row = ['*' if (i + j) % 3 == 0 else '.' for j in range(m)]
        a[i] = row
        l[i] = [x for x in range(m)]
        r[i] = [x for x in range(m)]
        s[i] = [0] * m

    # Original logic with deterministically generated a, l, r, s
    for i in range(n):
        j = 0
        b = a[i]
        ll = l[i]
        rr = r[i]
        while j < m:
            if b[j] == '*':
                jj = j + 1
                while jj < m and b[jj] == '*':
                    jj += 1
                jj -= 1
                for k in range(j, jj + 1):
                    ll[k] = j
                    rr[k] = jj
                j = jj + 1

            else:
                j += 1

    for i in range(m):
        j = 0
        while j < n:
            if a[j][i] == '*':
                jj = j + 1
                while jj < n and a[jj][i] == '*':
                    jj += 1
                jj -= 1
                for k in range(j, jj + 1):
                    x = min(i - l[k][i], r[k][i] - i, k - j, jj - k)
                    s[k][i] = x
                    if x > 0:
                        res.append((k + 1, i + 1, x))
                j = jj + 1

            else:
                j += 1

    for i in range(n):
        j = 0
        ss = s[i]
        rr = r[i]
        c = -1
        while j < m:
            if ss[j] > 0 and c < ss[j]:
                c = ss[j]
            if c >= 0:
                rr[j] = '*'

            else:
                rr[j] = '.'
            j += 1
            c -= 1
        j = m - 1
        c = -1
        while j >= 0:
            if ss[j] > 0 and c < ss[j]:
                c = ss[j]
            if c >= 0:
                rr[j] = '*'
            c -= 1
            j -= 1

    for i in range(m):
        j = 0
        c = -1
        while j < n:
            x = s[j][i]
            if x > 0 and c < x:
                c = x
            if c >= 0:
                r[j][i] = '*'
            j += 1
            c -= 1
        j = n - 1
        c = -1
        while j >= 0:
            x = s[j][i]
            if x > 0 and c < x:
                c = x
            if c >= 0:
                r[j][i] = '*'
            if r[j][i] != a[j][i]:
                # print(-1)
                pass
                return
            c -= 1
            j -= 1

    # print(len(res))
    pass
    for i in res:
        # print(*i)
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)