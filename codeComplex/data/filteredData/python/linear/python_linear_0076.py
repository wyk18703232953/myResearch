def main(n):
    # Deterministically generate two binary strings a and b of length n
    # Pattern: alternating '0' and '1', shifted for b
    a = ''.join('0' if i % 2 == 0 else '1' for i in range(n))
    b = ''.join('1' if i % 2 == 0 else '0' for i in range(n))

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

    length_b = len(b) - 1
    length_a = len(a) - 1
    ans = 0
    for i in range(len(a)):
        x = a[i]
        if x == "1":
            ans += z[(length_b - (length_a - i))] - z[i]
            if b[i] == "0":
                ans += 1

        else:
            ans += o[(length_b - (length_a - i))] - o[i]
            if b[i] == "1":
                ans += 1

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)