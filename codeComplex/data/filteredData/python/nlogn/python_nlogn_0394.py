def main(n):
    # Interpret n as the number of elements; keep k deterministic as a function of n
    if n <= 0:
        return
    k = max(1, n // 3)

    # Deterministic generation of p and c
    # p will have values in [1, max(1, n//4)] to ensure some grouping
    group_mod = max(1, n // 4)
    p = [(i % group_mod) + 1 for i in range(n)]
    c = [(i * 2 + 3) // 2 for i in range(n)]

    m = {}
    for i in range(n):
        if p[i] not in m:
            m[p[i]] = []
        m[p[i]].append(c[i])

    a = {}
    t = []
    for key, val in sorted(m.items()):
        a[key] = sum(t)
        t += val
        t.sort()
        t = t[max(0, len(t) - k):len(t)]

    result = " ".join(str(a[p[i]] + c[i]) for i in range(n))
    print(result)


if __name__ == "__main__":
    main(10)