def main(n):
    # Generate deterministic input data based on n
    # l and r are lists of length n
    # Here we construct l and r so that they are consistent with some s
    # and thus the original algorithm will typically print "YES".
    if n <= 0:
        return

    # Construct a deterministic permutation-like sequence s
    # Example: s[i] = n - 1 - (i % n) gives a decreasing sequence
    s = [n - 1 - (i % n) for i in range(n)]

    # Compute l and r from s exactly as the original logic expects
    l = []
    r = []
    for i in range(n):
        ll = 0
        for j in range(i):
            if s[j] > s[i]:
                ll += 1
        rr = 0
        for j in range(i + 1, n):
            if s[j] > s[i]:
                rr += 1
        l.append(ll)
        r.append(rr)

    # Original core logic, unchanged except for using generated l, r, n
    fl = 0
    m = n
    s_calc = list(range(n))
    for i in range(n):
        s_calc[i] = m - (l[i] + r[i])
        if fl != 1 and s_calc[i] == m:
            fl = 1
    for i in range(n):
        ll = 0
        for j in range(i):
            if s_calc[j] > s_calc[i]:
                ll += 1
        rr = 0
        for j in range(i + 1, n):
            if s_calc[j] > s_calc[i]:
                rr += 1
        if l[i] != ll or rr != r[i]:
            fl = 0
            break

    if fl == 1 and l[0] == 0 and r[n - 1] == 0:
        print('YES')
        print(*s_calc)
    else:
        print('NO')


if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(10)