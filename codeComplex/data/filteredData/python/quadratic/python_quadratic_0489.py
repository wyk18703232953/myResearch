def main(n):
    # Ensure n is at least 1
    if n <= 0:
        return

    # Deterministic construction of l and r based on n
    # Pattern: l[i] = i % (n // 2 + 1), r[i] = (n - 1 - i) % (n // 2 + 1)
    base = n // 2 + 1
    l = [i % base for i in range(n)]
    r = [(n - 1 - i) % base for i in range(n)]

    items = [(-l[i] - r[i], i) for i in range(n)]
    items.sort()
    vals = [1] * n
    m = 1
    for i in range(1, n):
        if items[i - 1][0] != items[i][0]:
            m += 1
        vals[items[i][1]] = m

    for i in range(n):
        ln = sum(1 for x in vals[:i] if x - vals[i] > 0)
        lr = sum(1 for x in vals[i:] if x - vals[i] > 0)
        if ln != l[i] or lr != r[i]:
            print('NO')
            break
    else:
        print('YES')
        print(' '.join(str(i) for i in vals))


if __name__ == "__main__":
    main(10)