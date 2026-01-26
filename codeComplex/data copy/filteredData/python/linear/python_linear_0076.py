def main(n):
    # Deterministically generate two binary strings a and b of length n
    # Pattern: a[i] = '1' if i % 2 == 0 else '0'
    #          b[i] = '1' if (i * 3) % 5 < 2 else '0'
    if n <= 0:
        # print(0)
        pass
        return

    a = ''.join('1' if i % 2 == 0 else '0' for i in range(n))
    b = ''.join('1' if (i * 3) % 5 < 2 else '0' for i in range(n))

    o = []
    z = []
    c0 = 0
    c1 = 0
    for ch in b:
        if ch == "0":
            c0 += 1

        else:
            c1 += 1
        o.append(c1)
        z.append(c0)

    n_b = len(b) - 1
    m_a = len(a) - 1
    ans = 0
    for i in range(len(a)):
        x = a[i]
        if x == "1":
            ans += z[(n_b - (m_a - i))] - z[i]
            if b[i] == "0":
                ans += 1

        else:
            ans += o[(n_b - (m_a - i))] - o[i]
            if b[i] == "1":
                ans += 1

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)