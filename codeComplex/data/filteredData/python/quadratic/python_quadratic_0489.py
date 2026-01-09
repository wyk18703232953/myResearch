def main(n):
    # Deterministically generate l and r based on n
    # Here we choose a simple pattern that scales with n
    # l[i] and r[i] are constructed so that l[i] + r[i] is non-decreasing
    l = [i // 2 for i in range(n)]
    r = [((n - 1 - i) // 2) for i in range(n)]

    items = [(-l[i] - r[i], i) for i in range(n)]
    items.sort()
    vals = [1] * n
    m = 1
    for i in range(1, n):
        if items[i - 1][0] != items[i][0]:
            m += 1
        vals[items[i][1]] = m

    for i in range(n):
        ln = sum(map(lambda x: x - vals[i] > 0, vals[:i]))
        lr = sum(map(lambda x: x - vals[i] > 0, vals[i:]))
        if ln != l[i] or lr != r[i]:
            # print('NO')
            pass
            break

    else:
        # print('YES')
        pass
        # print(' '.join(str(i) for i in vals))
        pass
if __name__ == "__main__":
    main(10)