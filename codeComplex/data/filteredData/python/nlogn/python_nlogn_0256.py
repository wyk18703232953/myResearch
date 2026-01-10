def main(n):
    import bisect

    # Map n to problem scale:
    # Let array length = n, number of queries = n
    size = n
    if size <= 0:
        return

    # Deterministically generate array a of length size
    # Example pattern: a[i] = (i % 5) + 1 to keep values small and positive
    a = [(i % 5) + 1 for i in range(size)]

    # Deterministically generate queries qu of length size
    # Example pattern: qu[i] = (i % (5 * size)) + 1 to give a variety w.r.t prefix sums
    qu = [(i % (5 * size)) + 1 for i in range(size)]

    # Original logic
    pre = []
    s = 0
    for i in a:
        s += i
        pre.append(s)

    lost = 0
    val_lost = 0
    ans = []

    for i in qu:
        val = i + val_lost
        b = bisect.bisect_left(pre, val, lost, size)
        val_lost = min(val, pre[-1])
        if b == size:
            lost = 0
            val_lost = 0
            ans.append(size)
            continue
        if pre[b] == val:
            lost = b + 1
        else:
            lost = b
        if lost == size:
            lost = 0
            val_lost = 0
        ans.append(size - lost)

    for x in ans:
        print(x)


if __name__ == "__main__":
    main(10)