def main(n):
    # Generate deterministic inputs based on n
    # Interpret original n as number of elements in y (before the extra 10**9)
    # and original m as number of operations, among which some with a==1 contribute to x.
    orig_n = n
    orig_m = max(1, n)  # ensure at least one operation

    # Generate y values deterministically
    # Example: y[i] = (i * 7) % (10**6) + i
    y = [(i * 7) % (10**6) + i for i in range(orig_n)]
    y.append(10 ** 9)

    # Generate operations deterministically and collect x from those with a == 1
    x = []
    for i in range(orig_m):
        # Deterministic pattern for a, b, c
        a = 1 if i % 3 != 0 else 2  # about 2/3 of operations have a == 1
        b = (i * 5 + 3) % (10**6)
        c = (i * 11 + 7) % (10**6)
        if a == 1:
            x.append(b)

    y.sort()
    x.sort()
    m = len(x)
    ans = m
    k = 0
    for i in range(orig_n + 1):
        ok = True
        for j in range(k, m):
            if y[i] <= x[j]:
                k = j
                ok = False
                break
        if ok:
            k = m
            ans = min(ans, m - k + i)
            break
        ans = min(ans, m - k + i)
    print(ans)


if __name__ == "__main__":
    main(10)