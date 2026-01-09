def main(n):
    # Deterministic data generation
    # Interpret n as the size of arrays l and r
    # Example pattern: l[i] = number of greater elements to the left in a descending array
    #                  r[i] = number of greater elements to the right in a descending array
    # This matches what the original algorithm expects in "YES" cases.
    l = [i for i in range(n)]          # in descending array, at position i, i elements before are greater
    r = [n - 1 - i for i in range(n)]  # in descending array, n-1-i elements after are greater

    fl = 0
    m = n
    s = list(range(n))
    for i in range(n):
        s[i] = m - (l[i] + r[i])
        if fl != 1 and s[i] == m:
            fl = 1
    for i in range(n):
        ll = 0
        for j in range(i):
            if s[j] > s[i]:
                ll += 1
        rr = 0
        for j in range(i + 1, n):
            if s[j] > s[i]:
                rr += 1
        if l[i] != ll or rr != r[i]:
            fl = 0
            break

    if fl == 1 and l[0] == 0 and r[n - 1] == 0:
        # print('YES')
        pass
        # print(*s)
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(10)