def main(n):
    mod = (10**9) + 7  # kept to mirror original environment, though unused
    q = []

    # Deterministic generation of T (number of test cases) and per-case sizes
    # Here: T = n, and for test case i (0-based), length a = max(1, i+1)
    T = n
    for tc in range(T):
        a = max(1, tc + 1)

        # Deterministic array generation of length a
        # Pattern: b[i] = (i % 10) + (tc % 5)
        b = [(i % 10) + (tc % 5) for i in range(a)]

        # Core logic from original program
        w = {}
        for i in range(a):
            key = b[i]
            if key in w:
                w[key] += 1
            else:
                w[key] = 1

        s = -1
        l = 0
        mi = 2325234324324234.0
        d = []
        for key in w:
            if w[key] >= 4:
                t = [str(key), str(key), str(key), str(key)]
                q.append(" ".join(t))
                l = 1
                break
            if w[key] >= 2:
                d.append(key)
        if l == 1:
            continue

        d.sort()
        p = []
        for i in range(len(d)):
            if s == -1:
                s = d[i]
            else:
                r = float(s) / float(d[i])
                r += float(d[i]) / float(s)
                if r < mi:
                    p = [str(d[i]), str(s)]
                    mi = r
                s = d[i]
        p = p * 2
        if p:
            q.append(" ".join(p))
        else:
            # Fallback if there is no element with frequency >= 2
            # Deterministic placeholder: repeat first element if exists
            if a >= 1:
                val = str(b[0])
                q.append(" ".join([val, val, val, val]))
            else:
                q.append("")

    print("\n".join(q))


if __name__ == "__main__":
    main(5)