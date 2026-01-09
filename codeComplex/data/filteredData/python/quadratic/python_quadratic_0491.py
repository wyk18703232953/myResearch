def main(n):
    # Deterministically generate l and r based on n
    # Example: l[i] = i % 3, r[i] = (i * 2) % 5
    l = [(i % 3) for i in range(n)]
    r = [((i * 2) % 5) for i in range(n)]

    a = [0 for _ in range(n)]
    m = []
    m_ = []
    for i in range(n):
        m_val = l[i] + r[i]
        m.append(m_val)
        m_.append(m_val)
    m.sort()
    ma = m[-1] + 1 if n > 0 else 1

    for i in range(n):
        a[i] = ma - m_[i]

    l_ = []
    r_ = []
    for i in range(n):
        c = 0
        d = 0
        for j in range(i + 1):
            if a[j] > a[i]:
                c += 1
        for j in range(i, n):
            if a[j] > a[i]:
                d += 1
        l_.append(c)
        r_.append(d)

    res = True
    for i in range(n):
        if l[i] != l_[i] or r[i] != r_[i]:
            res = False
            break

    if res:
        # print("YES")
        pass
        # print(" ".join(str(x) for x in a))
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)